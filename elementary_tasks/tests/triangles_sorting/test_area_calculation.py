import unittest
from elementary_tasks.triangles_sorting import Triangle


class TriangleTest(unittest.TestCase):
    """Area Calculation tests"""
    def setUp(self):
        """Set up for test"""
        print('\nSet up for [' + self.shortDescription() + ']')
        print(self)
        self.triangle_1 = Triangle('triangle 1', 3, 4, 5)
        self.triangle_2 = Triangle('triangle 2', 3.7, 4.2, 6.5)

    def tearDown(self):
        """Tear down for test"""
        print('Tear down for [' + self.shortDescription() + ']\n')

    def test_area_calculation_1(self):
        """Area Calculation function test"""
        result = self.triangle_1.area_calculation()
        self.assertEqual(result, {'triangle 1': 6.0})

    def test_area_calculation_2(self):
        """Area Calculation function test"""
        result = self.triangle_2.area_calculation()
        self.assertEqual(result, {'triangle 2': 7.27})


if __name__ == '__main__':
    unittest.main()
