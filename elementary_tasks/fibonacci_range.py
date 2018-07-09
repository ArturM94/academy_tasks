from elementary_tasks.do_continue import do_continue


class FibonacciRange:
    def __init__(self, s, f):
        self.start = s
        self.finish = f

    @staticmethod
    def fibonacci(n):
        """Counts the Fibonacci number for n

        :param n:
        :return: a
        """
        a = 0
        b = 1
        for _ in range(n):
            a, b = b, a + b
        return a

    def fibonacci_generation(self):
        """Generates Fibonacci numbers in the specified range

        :return: fibonacci_list
        """
        fibonacci_list = []
        for n in range(self.start, self.finish + 1):
            fibonacci_number = self.fibonacci(n)
            fibonacci_list.append(fibonacci_number)
        return fibonacci_list


def main():
    is_continue = True
    while is_continue:
        try:
            start = int(input('Enter the start number of range:\n'))
            finish = int(input('Enter the finish number of range:\n'))
            if start > finish:
                raise ValueError
        except ValueError:
            print('Incorrect value. The finish number must be greater than '
                  'the start number.\n')
            continue
        fr = FibonacciRange(start, finish)
        fibonacci_range = fr.fibonacci_generation()
        fibonacci_range = [str(_) for _ in fibonacci_range]
        fibonacci_range = ', '.join(fibonacci_range)
        print(fibonacci_range)
        answer = str(input('Do you want to continue? [y / yes]\n'))
        is_continue = do_continue(answer)


if __name__ == '__main__':
    main()
