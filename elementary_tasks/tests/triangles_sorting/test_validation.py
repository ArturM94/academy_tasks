from unittest import TestCase

from elementary_tasks.triangles_sorting import validation
from elementary_tasks.triangles_sorting import ValidationError


class TestValidation(TestCase):
    """Validation tests"""
    def setUp(self):
        """Set up for test"""
        print('\nSet up for [' + self.shortDescription() + ']')
        print(self)

    def tearDown(self):
        """Tear down for test"""
        print('Tear down for [' + self.shortDescription() + ']\n')

    def test_validation_for_int(self):
        """Validation function test"""
        triangle = 'triangle, 3, 4, 5'
        result = validation(triangle)
        self.assertEqual(result, ('triangle', 3.0, 4.0, 5.0))

    def test_validation_for_float(self):
        """Validation function test"""
        triangle = 'triangle, 3.7, 4.2, 6.5'
        result = validation(triangle)
        self.assertEqual(result, ('triangle', 3.7, 4.2, 6.5))

    def test_validation_for_double_name(self):
        """Validation function test"""
        triangle = 'double name, 3.7, 4.2, 6.5'
        result = validation(triangle)
        self.assertEqual(result, ('double name', 3.7, 4.2, 6.5))

    def test_validation_for_nonexistent_triangle(self):
        """Validation function test"""
        with self.assertRaises(ValidationError):
            triangle = 'triangle, 5, 8, 20'
            validation(triangle)


if __name__ == '__main__':
    TestValidation()
