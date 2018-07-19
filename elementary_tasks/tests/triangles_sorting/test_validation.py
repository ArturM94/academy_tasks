from unittest import TestCase

from elementary_tasks import Triangle
from elementary_tasks import validation
from elementary_tasks import ValidationError


class TestValidation(TestCase):
    """Validation tests"""
    def setUp(self):
        """Set up for test"""
        print('\nSet up for [' + self.shortDescription() + ']')
        print(self)

    def tearDown(self):
        """Tear down for test"""
        print('Tear down for [' + self.shortDescription() + ']\n')

    def test_validation_instance_for_int_sides(self):
        """Validation function test"""
        triangle_data = 'triangle, 3, 4, 5'
        result = validation(triangle_data)
        self.assertIsInstance(result, Triangle)

    def test_validation_instance_for_float_sides(self):
        """Validation function test"""
        triangle_data = 'triangle, 3.7, 4.2, 6.5'
        result = validation(triangle_data)
        self.assertIsInstance(result, Triangle)

    def test_validation_instance_for_mixed_sides(self):
        """Validation function test"""
        triangle_data = 'triangle, 3.7, 4, 6'
        result = validation(triangle_data)
        self.assertIsInstance(result, Triangle)

    def test_validation_instance_for_single_name(self):
        """Validation function test"""
        triangle_data = 'singlename, 3.7, 4.2, 6.5'
        result = validation(triangle_data)
        self.assertIsInstance(result, Triangle)

    def test_validation_instance_for_double_name(self):
        """Validation function test"""
        triangle_data = 'double name, 3.7, 4.2, 6.5'
        result = validation(triangle_data)
        self.assertIsInstance(result, Triangle)

    def test_validation_for_each_value_of_int_sides(self):
        """Validation function test"""
        triangle_data = 'triangle, 3, 4, 5'
        result = validation(triangle_data)
        self.assertEqual(result.side_a, 3.0)
        self.assertEqual(result.side_b, 4.0)
        self.assertEqual(result.side_c, 5.0)

    def test_validation_for_each_value_of_float_sides(self):
        """Validation function test"""
        triangle_data = 'triangle, 3.7, 4.2, 6.5'
        result = validation(triangle_data)
        self.assertEqual(result.side_a, 3.7)
        self.assertEqual(result.side_b, 4.2)
        self.assertEqual(result.side_c, 6.5)

    def test_validation_for_each_value_of_mixed_sides(self):
        """Validation function test"""
        triangle_data = 'triangle, 3.7, 4, 6'
        result = validation(triangle_data)
        self.assertEqual(result.side_a, 3.7)
        self.assertEqual(result.side_b, 4.0)
        self.assertEqual(result.side_c, 6.0)

    def test_validation_for_single_name(self):
        """Validation function test"""
        triangle_data = 'singlename, 3.7, 4.2, 6.5'
        result = validation(triangle_data)
        self.assertEqual(result.name, 'singlename')

    def test_validation_for_double_name(self):
        """Validation function test"""
        triangle_data = 'double name, 3.7, 4.2, 6.5'
        result = validation(triangle_data)
        self.assertEqual(result.name, 'double name')

    def test_validation_for_nonexistent_triangle(self):
        """Validation function test"""
        with self.assertRaises(ValidationError):
            triangle = 'triangle, 5, 8, 20'
            validation(triangle)


if __name__ == '__main__':
    TestValidation()
