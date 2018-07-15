from unittest import TestCase

from elementary_tasks import ChessBoard


class TestChessboard(TestCase):
    """ChessBoard tests"""
    def setUp(self):
        """Set up for test"""
        print('\nSet up for [' + self.shortDescription() + ']')
        print(self)

    def tearDown(self):
        """Tear down for test"""
        print('Tear down for [' + self.shortDescription() + ']\n')

    def test_even_row_generation(self):
        """Row Generation method test"""
        board = ChessBoard(5, 8)
        result = board.row_generation()
        self.assertEqual(result, ('■□■□■□■□', '□■□■□■□■'))

    def test_odd_row_generation(self):
        """Row Generation method test"""
        board = ChessBoard(5, 7)
        result = board.row_generation()
        self.assertEqual(result, ('■□■□■□■', '□■□■□■□'))


if __name__ == '__main__':
    TestChessboard()
