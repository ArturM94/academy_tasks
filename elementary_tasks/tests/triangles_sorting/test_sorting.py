from unittest import TestCase

from elementary_tasks.triangles_sorting import sorting


class TestSorting(TestCase):
    """Sorting tests"""
    def setUp(self):
        """Set up for test"""
        print('\nSet up for [' + self.shortDescription() + ']')
        print(self)

    def tearDown(self):
        """Tear down for test"""
        print('Tear down for [' + self.shortDescription() + ']\n')

    def test_sorting_for_float_areas(self):
        """Sorting function test"""
        unsorted_triangles = {'triangle 1': 7.27,
                              'triangle 2': 2.9,
                              'triangle 3': 8.74}
        result = sorting(unsorted_triangles)
        self.assertEqual(result, {'triangle 3': 8.74,
                                  'triangle 1': 7.27,
                                  'triangle 2': 2.9})


if __name__ == '__main__':
    TestSorting()
