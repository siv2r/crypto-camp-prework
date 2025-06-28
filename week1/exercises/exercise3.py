import unittest
from secrets import randbits
from unitsmodp import UnitsModP, G
from exercise1 import fast_exp

def inverse(a: UnitsModP) -> UnitsModP:
    exp = UnitsModP.P - 2
    return fast_exp(a, exp)


# unit tests
class TestInverse(unittest.TestCase):
    def test_rand_inverse(self):
        A = UnitsModP(randbits(2048))
        self.assertEqual(
            inverse(A),
            UnitsModP(pow(A._val, UnitsModP.P - 2, UnitsModP.P))
        )

if __name__ == "__main__":
    unittest.main()