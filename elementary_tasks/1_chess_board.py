class ChessBoard:
    def __init__(self, h, w):
        self.height = h
        self.width = w

    def row_generation(self):
        # Генерация строк шахматной доски.
        # Строка состоит из четного количества пар клеток
        # звездочка-пробел '* ' или пробел-звездочка ' *',
        # если сама ширина имеет четное значение.
        # Генерация происходит для нечетных и четных строк.
        half_width = self.width // 2
        if self.width % 2 == 0:
            row_odd = '* ' * half_width
            row_even = ' *' * half_width
            return row_odd, row_even
        # Если ширина имеет нечетное значение, то к уже известному
        # сценарию необходимо добавить либо звездочку '*', либо пробел ' '.
        else:
            row_odd = '* ' * half_width + '*'
            row_even = ' *' * half_width + ' '
            return row_odd, row_even

    def print_board(self, row_odd, row_even):
        # Вывод доски в консоль.
        # Вывод производится парой нечетной и четной строки.
        half_height = self.height // 2
        if self.height % 2 == 0:
            for i in range(half_height):
                print(row_odd)
                print(row_even)
        # Если количество строк нечетное, то дополнительно
        # на последней итерации выводится нечетная строка.
        else:
            for i in range(half_height):
                print(row_odd)
                print(row_even)
                if i == half_height - 1:
                    print(row_odd)


print('Введите поочередно высоту и ширину: ')
height = int(input())
width = int(input())
chess_board = ChessBoard(height, width)
r_odd, r_even = chess_board.row_generation()
chess_board.print_board(r_odd, r_even)
