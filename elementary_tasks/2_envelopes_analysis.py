from elementary_tasks.do_continue import do_continue


class Envelope:
    def __init__(self, a, b, c, d):
        # От пользователя принимаются параметры конвертов,
        # вызывается функция определения вхождения конверта
        self.side_a = a
        self.side_b = b
        self.side_c = c
        self.side_d = d

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
                a = float(input('Side a:\n'))
                b = float(input('Side b:\n'))
                c = float(input('Side c:\n'))
                d = float(input('Side d:\n'))
                if a < 0 or b < 0 or c < 0 or d < 0:
                    raise ValueError
            except ValueError:
                print('Invalid value. Entries must contain numbers greater '
                      'than zero.\n')
                continue
            envelope = Envelope(a, b, c, d)
            envelope.envelope_entry()
            is_continue = do_continue()

    print('The program is completed.')


if __name__ == '__main__':
    main()
