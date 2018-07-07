class NaturalNumbers:
    def __init__(self):
        self.n = int(input())
        self.i = 1
        self.sequence = []

    def sequence_generation(self):
        # Генерирует список последовательности натуральных чисел,
        # квадрат которых меньше заданного n
        while self.i ** 2 < self.n:
            self.sequence.append(self.i)
            self.i += 1

        return self.sequence

    # Поскольку метод output_generation не использует экземпляр,
    # то ему не нужно принимать аргумент self. Следовательно,
    # метод нужно объявить статическим, либо вывести за пределы класса
    @staticmethod
    def output_generation(sequence):
        # Простая функция
        # Однострочный вывод последовательности через запятую

        # Вариант 1
        # for _ in sequence:
        #     if _ == sequence[-1]:
        #         print(_)
        #     else:
        #         print(_, end=', ')

        # Вариант 2
        sequence = [str(_) for _ in sequence]
        sequence = ', '.join(sequence)

        return sequence


def main():
    natural_numbers = NaturalNumbers()
    sequence = natural_numbers.sequence_generation()
    print(natural_numbers.output_generation(sequence))


if __name__ == '__main__':
    main()
