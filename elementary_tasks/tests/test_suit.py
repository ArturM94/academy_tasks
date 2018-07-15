from unittest import TestLoader, TestSuite, TextTestRunner

from .chessboard import TestChessboard
from .do_continue import TestDoContinue
from .envelopes_analysis import TestEnvelopeEntry
from .fibonacci_range import TestFibonacci
from .fibonacci_range import TestFibonacciGeneration


if __name__ == '__main__':
    loader = TestLoader()
    suit = TestSuite((
        loader.loadTestsFromTestCase(TestChessboard),
        loader.loadTestsFromTestCase(TestDoContinue),
        loader.loadTestsFromTestCase(TestEnvelopeEntry),
        loader.loadTestsFromTestCase(TestFibonacci),
        loader.loadTestsFromTestCase(TestFibonacciGeneration),
    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suit)
