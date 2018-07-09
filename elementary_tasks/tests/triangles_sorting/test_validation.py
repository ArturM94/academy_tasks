import unittest
from elementary_tasks.triangles_sorting import validation


class ValidationTest(unittest.TestCase):
    """Validation tests"""
    def setUp(self):
        """Set up for test"""
        print('\nSet up for [' + self.shortDescription() + ']')
        print(self)
        self.triangle_1 = 'triangle 1, 3, 4, 5'
        self.triangle_2 = 'triangle 2, 3.7, 4.2, 6.5'
        self.triangle_3 = 'triangle 3, 5, 8, 20'

    def tearDown(self):
        """Tear down for test"""
        print('Tear down for [' + self.shortDescription() + ']\n')

    def test_correct_validation_1(self):
        """Validation function test"""
        result = validation(self.triangle_1)
        self.assertEqual(result, ('triangle 1', 3.0, 4.0, 5.0))

    def test_correct_validation_2(self):
        """Validation function test"""
        result = validation(self.triangle_2)
        self.assertEqual(result, ('triangle 2', 3.7, 4.2, 6.5))

    def test_incorrect_validation_1(self):
        """Validation function test"""
        result = validation(self.triangle_3)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
