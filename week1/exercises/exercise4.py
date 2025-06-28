from __future__ import annotations
from dataclasses import dataclass

from secrets import randbelow

from unitsmodp import UnitsModP, G
from exercise1 import fast_exp
from exercise3 import inverse

class SecretKey:
    SIZE = UnitsModP.ORDER

    def __init__(self, val: int) -> None:
        assert isinstance(val, int)
        assert (val % self.SIZE != 0)
        self._val = val % self.SIZE

    def __int__(self) -> int:
        return self._val

    @classmethod
    def random(cls) -> SecretKey:
        return cls(randbelow(cls.SIZE - 1) + 1) # 1 ≤ x ≤ ORDER-1

@dataclass(frozen=True, slots=True)
class PublicKey:
    val: UnitsModP

    @classmethod
    def from_secret(cls, sk: SecretKey) -> PublicKey:
        return cls(fast_exp(G, int(sk)))

    @classmethod
    def random(cls) -> PublicKey:
        sk = SecretKey.random()
        return cls.from_secret(sk)

@dataclass(frozen=True, slots=True)
class Message:
    val: UnitsModP

    def encrypt(self, pk: PublicKey) -> CipherText:
        k = SecretKey.random()
        return self.encrypt_with_k(k, pk)

    def encrypt_with_k(self, k: SecretKey, pk: PublicKey) -> CipherText:
        """
        (g^k, m · pk^k)
        """
        return CipherText(
            fast_exp(G, int(k)),
            self.val * fast_exp(pk.val, int(k))
        )

@dataclass(frozen=True, slots=True)
class CipherText:
    c1: UnitsModP
    c2: UnitsModP

    def decrypt(self, sk: SecretKey) -> Message:
        """
        m = c2 · (c1^sk)⁻¹
        """
        shared = fast_exp(self.c1, int(sk))
        msg = self.c2 * inverse(shared)
        return Message(msg)

# unit tests
import unittest
from unittest.mock import patch
from collections import namedtuple

Vector = namedtuple('Vector', ['p', 'g', 'x', 'k', 'm', 'a', 'b'])

TEST_VECTORS = [
    Vector(71,33,62,31,15,62,18),
    Vector(23,11,6,3,10,20,22),
    Vector(809,3,68,89,100,345,517),
    Vector(17,6,5,10,13,15,9),
    Vector(
        84265675725482892459719348378630146162719620409152809167814480007059199482163,
        5,
        2799014790424892046701478888900891009403869701173893426,
        23517683968368899022119256606644551548285683288848885921,
        87521618088882658227876453,
        22954586883013884818653063688294540134886732496160582262267014428782771199687,
        56046128113101346099694619669629128017849277484825379502821514323706183544424
    ),
    Vector(
        12658517083168187407924345155971956101250996576825115113297001855799796437288935576230034157578333666497170430505565580165565829633685607504706642034926119,
        7,
        2001688878140630728014209681954697141876038523595247208,
        5446024688717452254835115775456957961297236108858862823,
        87521618088882658227876453,
        2150519483988769855483983776372336742288374425191291528256965705108393490638750082340115568718132372731853110762124400441550538499580316268601341087676203,
        1540471266850557563382406324432354117072109094950140952195099581066490559252112349492583688225692526496193879919152401794896907007394565292272866724291488,
    ),
]

class TestElGamal(unittest.TestCase):
    def test_correctness(self):
        msg = Message(UnitsModP.random())
        sk = SecretKey.random()
        pk = PublicKey.from_secret(sk)
        # encrypt
        enc_msg = msg.encrypt(pk)
        # decrypt
        dec_msg = enc_msg.decrypt(sk)
        self.assertEqual(dec_msg, msg)

    def test_vector(self):
        for vec in TEST_VECTORS:
            with (
                patch('unitsmodp.UnitsModP.P', vec.p),
                patch('unitsmodp.UnitsModP.ORDER', vec.p - 1),
                patch(__name__ + '.G', UnitsModP(vec.g)),
            ):
                sk = SecretKey(vec.x)
                pk = PublicKey.from_secret(sk)
                msg = Message(UnitsModP(vec.m))
                enc_msg = msg.encrypt_with_k(SecretKey(vec.k), pk)

                self.assertEqual(enc_msg.c1._val, vec.a)
                self.assertEqual(enc_msg.c2._val, vec.b)

                self.assertEqual(enc_msg.decrypt(sk), msg)


if __name__ == "__main__":
    unittest.main()