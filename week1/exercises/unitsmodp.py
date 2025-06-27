"""
Unit group (ℤ/pℤ)* implementation.
"""

from __future__ import annotations

class UnitsModP:
    P = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE65381FFFFFFFFFFFFFFFF
    ORDER = P - 1

    def __init__(self, val: int = 1) -> None:
        assert isinstance(val, int)
        if val == 0:
            raise ValueError("cannot be 0")
        self._val = val % self.P

    def __add__(self, other: UnitsModP) -> UnitsModP:
        return NotImplemented

    def __mul__(self, other: UnitsModP) -> UnitsModP:
        assert isinstance(other, type(self))
        val = (self._val * other._val) % self.P
        return type(self)(val)

    def __eq__(self, other: UnitsModP) -> bool:
        assert isinstance(other, type(self))
        return self._val == other._val

# Generator Point
G = UnitsModP(2)