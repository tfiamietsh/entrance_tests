from unittest import TestCase
from math import pi
from shape import Circle, Triangle, calc_area


class TestUtils(TestCase):
    def test_calc_area_circle(self):
        self.assertAlmostEqual(calc_area(Circle(1)), pi)

    def test_calc_area_triangle(self):
        self.assertAlmostEqual(calc_area(Triangle(3, 4, 5)), 6)
