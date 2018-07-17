from elementary_tasks.do_continue import do_continue


class Envelope:
    def __init__(self, first_side, second_side):
        """Initialisation method

        :param first_side: -- First side envelope
        :param second_side: -- Second side envelope
        """
        self.first_side = first_side
        self.second_side = second_side


def envelope_entry(envelope1, envelope2):
    """Compares envelopes

    Compares sides of two envelopes in pairs

    :param envelope1: -- First envelope
    :param envelope2: -- Second envelope
    :return: -- String result of comparision
    """
    if (envelope1.first_side > envelope2.first_side) and \
            (envelope1.second_side > envelope2.second_side):
        return 'The second envelope can be nested in the first.\n'
    elif (envelope1.first_side < envelope2.first_side) and \
            (envelope1.second_side < envelope2.second_side):
        return 'The first envelope can be nested in the second.\n'
    else:
        return 'None of the envelopes can be nested in another.\n'


def main():
    is_continue = True
    while is_continue:
            print('Enter the sizes of two envelopes (a, b) and (c, d).')
            try:
                side_a = float(input('Side a:\n'))
                side_b = float(input('Side b:\n'))
                side_c = float(input('Side c:\n'))
                side_d = float(input('Side d:\n'))
                # Additional validation
                if side_a < 1 or side_b < 1 or side_c < 1 or side_d < 1:
                    raise ValueError
            except ValueError:
                print('Invalid value. Entries must contain numbers greater '
                      'than zero.\n')
                continue
            envelope1 = Envelope(side_a, side_b)
            envelope2 = Envelope(side_c, side_d)
            entry_result = envelope_entry(envelope1, envelope2)
            print(entry_result)
            answer = str(input('Do you want to continue? [y / yes]\n'))
            is_continue = do_continue(answer)

    print('The program is completed.')


if __name__ == '__main__':
    main()
