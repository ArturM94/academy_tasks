class ChessBoard:
    def __init__(self,  h, w):
        self.height = h
        self.width = w

    def calc_row(self):
        half_width = self.width // 2
        if self.width % 2 == 0:
            row_odd = '* ' * half_width
            row_even = ' *' * half_width
            self.print_board(row_odd, row_even)
        else:
            row_odd = '* ' * half_width + '*'
            row_even = ' *' * half_width + ' '
            self.print_board(row_odd, row_even)

    def print_board(self, row_odd, row_even):
        half_height = self.height // 2
        if self.height % 2 == 0:
            for i in range(half_height):
                print(row_odd)
                print(row_even)
        else:
            for i in range(half_height):
                print(row_odd)
                print(row_even)
                if i == half_height - 1:
                    print(row_odd)


print('Введите поочередно высоту и ширину: ')
height = int(input())
width = int(input())
board = ChessBoard(height, width)
board.calc_row()
