from unittest import TestCase

from elementary_tasks.fibonacci_range import FibonacciRange


class TestFibonacciGeneration(TestCase):
    """Fibonacci Generation tests"""
    def setUp(self):
        """Set up for test"""
        print('\nSet up for [' + self.shortDescription() + ']')
        print(self)

    def tearDown(self):
        """Tear down for test"""
        print('Tear down for [' + self.shortDescription() + ']\n')

    def test_fibonacci_generation_from_1_to_5(self):
        """Fibonacci Generation method test"""
        fr = FibonacciRange(0, 5)
        result = fr.fibonacci_generation()
        self.assertEqual(result, [0, 1, 1, 2, 3, 5])

    def test_fibonacci_generation_from_6_to_11(self):
        """Fibonacci Generation method test"""
        fr = FibonacciRange(6, 11)
        result = fr.fibonacci_generation()
        self.assertEqual(result, [8, 13, 21, 34, 55, 89])


if __name__ == '__main__':
    TestFibonacciGeneration()
