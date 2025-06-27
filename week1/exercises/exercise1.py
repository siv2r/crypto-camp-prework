import unittest
from secrets import randbits
from unitsmodp import UnitsModP, G

def fast_exp(a: UnitsModP, exp: int) -> UnitsModP:
    assert exp >= 0
    res = UnitsModP()
    for i in range(exp.bit_length() - 1, -1, -1):
        res = res * res
        if (exp >> i) & 1:
            res = res * a
    return res

# unit tests
class TestFastExp(unittest.TestCase):
    def test_zero_exp(self):
        self.assertEqual(fast_exp(G, 0), UnitsModP())

    def test_small_exp(self):
        self.assertEqual(
            fast_exp(G, 65537),
            UnitsModP(pow(G._val, 65537, UnitsModP.P))
        )

    def test_half_exp(self):
        exp_half = UnitsModP.P // 2
        self.assertEqual(
            fast_exp(G, exp_half),
            UnitsModP(pow(G._val, exp_half, UnitsModP.P))
        )

    def test_rand_exp(self):
        exp_rand = randbits(2048)
        self.assertEqual(
            fast_exp(G, exp_rand),
            UnitsModP(pow(G._val, exp_rand, UnitsModP.P))
        )

if __name__ == "__main__":
    unittest.main()

