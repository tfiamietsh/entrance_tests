from math import sqrt, isclose
from .base import Shape


class Triangle(Shape):
    @staticmethod
    def _validate(a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError('Invalid triangle')

    def __init__(self, a: float, b: float, c: float):
        Triangle._validate(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def calc_area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self) -> bool:
        min_side, max_side = min(self.a, self.b, self.c), max(self.a, self.b, self.c)
        mid_side = self.a + self.b + self.c - min_side - max_side
        return isclose(min_side ** 2 + mid_side ** 2, max_side ** 2, rel_tol=1e-9)
