from elementary_tasks.do_continue import do_continue


class SequenceOfNaturalNumbers:
    def __init__(self, limit_number):
        """Initialisation method

        :param limit_number: -- Entered natural number
        """
        self.limit_number = limit_number

    def sequence_generation(self):
        """Sequence generator

        Generates sequence list of natural numbers
        which square less than limit_number

        :return: sequence -- Sequence of natural numbers
        """
        sequence = []
        natural_number = 1  # First natural number

        while natural_number ** 2 < self.limit_number:
            sequence.append(natural_number)
            natural_number += 1

        return sequence


def output_generation(sequence):
    """Output generator

    Generates single-line output sequence separated by a comma

    :param sequence: -- Sequence of natural numbers
    :return: sequence -- Same sequence with a commas
    """
    sequence = [str(_) for _ in sequence]
    sequence = ', '.join(sequence)
    return sequence


def main():
    is_continue = True

    while is_continue:
        try:
            limit_number = int(input('Enter limit number for sequence:\n'))
        except ValueError:
            print('Invalid value. Entry must contain only integer number.\n')
            continue
        sequence = SequenceOfNaturalNumbers(limit_number)
        sequence = sequence.sequence_generation()
        print(output_generation(sequence))
        answer = str(input('Do you want to continue? [y / yes]\n'))
        is_continue = do_continue(answer)


if __name__ == '__main__':
    main()
