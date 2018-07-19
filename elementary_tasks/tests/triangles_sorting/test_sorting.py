from unittest import TestCase

from elementary_tasks import sorting
from elementary_tasks import Triangle


class TestSorting(TestCase):
    """Sorting tests"""
    def setUp(self):
        """Set up for test"""
        print('\nSet up for [' + self.shortDescription() + ']')
        print(self)
        self.triangle1 = Triangle('1', 3.7, 4.2, 6.5)
        self.triangle2 = Triangle('2', 2.0, 3.0, 4.0)
        self.triangle3 = Triangle('3', 3.7, 5.0, 6.0)

    def tearDown(self):
        """Tear down for test"""
        print('Tear down for [' + self.shortDescription() + ']\n')

    def test_sorting_for_float_areas(self):
        """Sorting function test"""

        unsorted_triangles = [self.triangle1,
                              self.triangle2,
                              self.triangle3]
        result = sorting(unsorted_triangles)
        self.assertEqual(result, [self.triangle3,
                                  self.triangle1,
                                  self.triangle2])


if __name__ == '__main__':
    TestSorting()
