from unittest import TestCase
from shape import Triangle


class TestTriangle(TestCase):
    def test_validate_exception(self):
        with self.assertRaises(ValueError):
            Triangle._validate(1, 2, 3)

    def test_validate_no_exception(self):
        try:
            Triangle._validate(3, 4, 5)
        except Exception as e:
            self.fail(e)

    def test_calc_area(self):
        self.assertAlmostEqual(Triangle(3, 4, 5).calc_area(), 6)

    def test_is_right_true(self):
        self.assertTrue(Triangle(3, 4, 5).is_right())

    def test_is_right_false(self):
        self.assertFalse(Triangle(4, 5, 6).is_right())
