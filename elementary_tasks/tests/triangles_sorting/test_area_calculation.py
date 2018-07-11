from unittest import TestCase

from elementary_tasks.triangles_sorting import Triangle


class TestAreaCalculation(TestCase):
    """Area Calculation tests"""
    def setUp(self):
        """Set up for test"""
        print('\nSet up for [' + self.shortDescription() + ']')
        print(self)

    def tearDown(self):
        """Tear down for test"""
        print('Tear down for [' + self.shortDescription() + ']\n')

    def test_area_calculation_for_float_values(self):
        """Area Calculation function test"""
        triangle = Triangle('triangle', 3.7, 4.2, 6.5)
        result = triangle.area_calculation()
        self.assertEqual(result, {'triangle': 7.27})

    def test_area_calculation_for_int_values(self):
        """Area Calculation function test"""
        triangle = Triangle('triangle', 3.7, 4.2, 6.5)
        result = triangle.area_calculation()
        self.assertEqual(result, {'triangle': 7.27})

    def test_area_calculation_for_mixed_values(self):
        """Area Calculation function test"""
        triangle = Triangle('triangle', 3.7, 4.2, 6.5)
        result = triangle.area_calculation()
        self.assertEqual(result, {'triangle': 7.27})


if __name__ == '__main__':
    TestAreaCalculation()
