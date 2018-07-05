from elementary_tasks.do_continue import do_continue


class Envelope:
    def __init__(self, side_a, side_b, side_c, side_d):
        # От пользователя принимаются параметры конвертов,
        # вызывается функция определения вхождения конверта
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.side_d = side_d

        instance_id = id(Envelope)
        print(f'Instance id: {instance_id}\n')

    def envelope_entry(self):
        # Сравниваются стороны конвертов,
        # вызывается функция проверки результата
        if (self.side_a > self.side_c) and (self.side_b > self.side_d):
            print('The second envelope can be nested in the first.\n')
        elif (self.side_a < self.side_c) and (self.side_b < self.side_d):
            print('The first envelope can be nested in the second.\n')
        else:
            print('None of the envelopes can be nested in another.\n')


def main():
    is_continue = True
    while is_continue:
            print('Enter the sizes of two envelopes (a, b) and (c, d).')
            try:
                side_a = float(input('Side a:\n'))
                side_b = float(input('Side b:\n'))
                side_c = float(input('Side c:\n'))
                side_d = float(input('Side d:\n'))
                if side_a < 1 or side_b < 1 or side_c < 1 or side_d < 1:
                    raise ValueError
            except ValueError:
                print('Invalid value. Entries must contain numbers greater '
                      'than zero.\n')
                continue
            envelope = Envelope(side_a, side_b, side_c, side_d)
            envelope.envelope_entry()
            is_continue = do_continue()

    print('The program is completed.')


if __name__ == '__main__':
    main()
