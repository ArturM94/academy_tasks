from unittest import TestCase

from elementary_tasks import Triangle


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
        """Area Calculation method test"""
        triangle = Triangle('triangle', 3.7, 4.2, 6.5)
        result = triangle.area_calculation()
        self.assertEqual(result, 7.27)


if __name__ == '__main__':
    TestAreaCalculation()
