from elementary_tasks import do_continue


class ChessBoard:
    def __init__(self, h, w):
        self.height = h
        self.width = w

    def row_generation(self):
        """Row generation

        Row generation for chessboard. If the width has an even value,
        than a row consists of an even number of white and black
        squares ('■□' or '□■'). If the width has an odd value,
        then to the already known scenario, adds one white or black square.

        :return: Odd and even rows
        """
        half_width = self.width // 2
        if self.width % 2 == 0:
            row_odd = '■□' * half_width
            row_even = '□■' * half_width
            return row_odd, row_even
        else:
            row_odd = '■□' * half_width + '■'
            row_even = '□■' * half_width + '□'
            return row_odd, row_even


def print_board(height, row_odd, row_even):
    """Prints a chessboard in console

    The output is performed by a pair of odd and even rows.
    If the number of rows is odd, then an odd row is output
    additionally at the last iteration.

    :param height: -- Height of chessboard
    :param row_odd: -- Squares for odd row
    :param row_even: -- Squares for even row
    :return:
    """
    half_height = height // 2
    if height % 2 == 0:
        for i in range(half_height):
            print(row_odd)
            print(row_even)
    else:
        for i in range(half_height):
            print(row_odd)
            print(row_even)
            if i == half_height - 1:
                print(row_odd)


def main():
    is_continue = True

    while is_continue:
        print('Enter the size of chessboard.')

        try:
            height = int(input('Height:\n'))
            width = int(input('Width:\n'))
        except ValueError:
            print('Invalid value. Entries must contain only integer numbers.')
            continue

        chess_board = ChessBoard(height, width)
        r_odd, r_even = chess_board.row_generation()
        print_board(height, r_odd, r_even)
        answer = str(input('Do you want to continue? [y / yes]\n'))
        is_continue = do_continue(answer)


if __name__ == '__main__':
    main()
