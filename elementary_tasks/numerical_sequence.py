from elementary_tasks.do_continue import do_continue


class SequenceOfNaturalNumbers:
    def __init__(self, limit_number):
        """Initialisation method

        :param limit_number: -- Limit for squaring of natural number
        """
        self.limit_number = limit_number

    @property
    def sequence(self):
        """Sequence

        Calls method of sequence generation

        :return: -- Sequence of natural number
        """
        return self.sequence_generation()

    def __str__(self):
        """str method

        Redefines str() function for sequence output

        :return: -- Sequence separated by commas
        """
        return ', '.join([str(_) for _ in self.sequence])

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


def main():
    is_continue = True

    while is_continue:
        try:
            limit_number = int(input('Enter limit number for sequence:\n'))
            if limit_number < 2:
                raise ValueError
        except ValueError:
            print('Invalid value. Entry must contain only positive integer '
                  'number grater than 1.\n')
            continue
        sequence_instance = SequenceOfNaturalNumbers(limit_number)
        print(sequence_instance)
        answer = str(input('Do you want to continue? [y / yes]\n'))
        is_continue = do_continue(answer)


if __name__ == '__main__':
    main()
