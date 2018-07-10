from unittest import TestCase

from elementary_tasks.fibonacci_range import FibonacciRange


class TestFibonacci(TestCase):
    """Fibonacci tests"""
    def setUp(self):
        """Set up for test"""
        print('\nSet up for [' + self.shortDescription() + ']')
        print(self)

    def tearDown(self):
        """Tear down for test"""
        print('Tear down for [' + self.shortDescription() + ']\n')

    def test_fibonacci_for_0(self):
        """Fibonacci function test"""
        result = FibonacciRange.fibonacci(0)
        self.assertEqual(result, 0)

    def test_fibonacci_for_1(self):
        """Fibonacci function test"""
        result = FibonacciRange.fibonacci(1)
        self.assertEqual(result, 1)

    def test_fibonacci_for_2(self):
        """Fibonacci function test"""
        result = FibonacciRange.fibonacci(2)
        self.assertEqual(result, 1)

    def test_fibonacci_for_8(self):
        """Fibonacci function test"""
        result = FibonacciRange.fibonacci(8)
        self.assertEqual(result, 21)


if __name__ == '__main__':
    TestFibonacci()
