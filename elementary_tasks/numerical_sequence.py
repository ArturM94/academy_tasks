from elementary_tasks.do_continue import do_continue


class SequenceOfNaturalNumbers:
    def __init__(self, limit_number, sequence=None):
        """Initialisation method

        :param limit_number: -- Entered natural number
        """
        self.limit_number = limit_number
        self.sequence = sequence

    def __str__(self):
        """str method

        Redefines str() function for sequence output

        :return: sequence -- Sequence separated by commas
        """
        self.sequence = [str(_) for _ in self.sequence]
        return ', '.join(self.sequence)

    def sequence_generation(self):
        """Sequence generator

        Generates sequence list of natural numbers
        which square less than limit_number

        :return: sequence -- Sequence of natural numbers
        """
        self.sequence = []
        natural_number = 1  # First natural number

        while natural_number ** 2 < self.limit_number:
            self.sequence.append(natural_number)
            natural_number += 1

        return self.sequence


def main():
    is_continue = True

    while is_continue:
        try:
            limit_number = int(input('Enter limit number for sequence:\n'))
        except ValueError:
            print('Invalid value. Entry must contain only integer number.\n')
            continue
        sequence_instance = SequenceOfNaturalNumbers(limit_number)
        sequence_instance.sequence = sequence_instance.sequence_generation()
        print(sequence_instance)
        answer = str(input('Do you want to continue? [y / yes]\n'))
        is_continue = do_continue(answer)


if __name__ == '__main__':
    main()
