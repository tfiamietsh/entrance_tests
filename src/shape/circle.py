from math import pi
from .base import Shape


class Circle(Shape):
    def __init__(self, r: float):
        self.r = r

    def calc_area(self) -> float:
        return pi * self.r * self.r
