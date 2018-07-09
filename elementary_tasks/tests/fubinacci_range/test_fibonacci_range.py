import unittest
from elementary_tasks.fibonacci_range import FibonacciRange


class FibonacciRangeTest(unittest.TestCase):
    """FibonacciRange tests"""
    def setUp(self):
        """Set up for test"""
        print('\nSet up for [' + self.shortDescription() + ']')
        print(self)
        self.fr = FibonacciRange(5, 10)

    def tearDown(self):
        """Tear down for test"""
        print('Tear down for [' + self.shortDescription() + ']\n')

    def test_fibonacci_0(self):
        """Fibonacci function test"""
        result = self.fr.fibonacci(0)
        self.assertEqual(result, 0)

    def test_fibonacci_1(self):
        """Fibonacci function test"""
        result = self.fr.fibonacci(1)
        self.assertEqual(result, 1)

    def test_fibonacci_2(self):
        """Fibonacci function test"""
        result = self.fr.fibonacci(2)
        self.assertEqual(result, 1)

    def test_fibonacci_generation(self):
        """Fibonacci generation function test"""
        result = self.fr.fibonacci_generation()
        self.assertEqual(result, [5, 8, 13, 21, 34, 55])


if __name__ == '__main__':
    unittest.main()
