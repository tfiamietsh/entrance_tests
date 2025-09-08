from unittest import TestCase
from math import pi
from shape import Circle


class TestCircle(TestCase):
    def test_calc_area(self):
        self.assertAlmostEqual(Circle(1).calc_area(), pi)
