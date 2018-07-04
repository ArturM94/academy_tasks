class WordNumber:
    def __init__(self, digit_number):
        self.digit_number = digit_number
        self.ZERO = 'ноль'
        self.ONES = {
            0: '',
            1: 'один',
            2: 'два',
            3: 'три',
            4: 'четыре',
            5: 'пять',
            6: 'шесть',
            7: 'семь',
            8: 'восемь',
            9: 'девять'
            }
        self.TEENS = {
            0: '',
            10: 'десять',
            11: 'одинадцать',
            12: 'двенадцать',
            13: 'тринадцать',
            14: 'четырнадцать',
            15: 'пятнадцать',
            16: 'шестнадцать',
            17: 'семнадцать',
            18: 'восемнадцать',
            19: 'девятнадцать',
            }
        self.TENS = {
            0: '',
            1: 'десять',
            2: 'двадцать',
            3: 'тридцать',
            4: 'сорок',
            5: 'пятьдесят',
            6: 'шестьдесят',
            7: 'семьдесят',
            8: 'восемьдесят',
            9: 'девяносто',
            }
        self.HUNDREDS = {
            0: '',
            1: 'сто',
            2: 'двести',
            3: 'триста',
            4: 'четыреста',
            5: 'пятьсот',
            6: 'шестьсот',
            7: 'семьсот',
            8: 'восемьсот',
            9: 'девятьсот',
            }
        self.THOUSANDS = {
            0: '',
            1: 'одна тысяча',
            2: 'две тысячи',
            3: 'три тысячи',
            4: 'четыре тысяч',
            5: 'пять тысяч',
            6: 'шесть тысяч',
            7: 'семь тысяч',
            8: 'восемь тысяч',
            9: 'девять тысяч',
            }

    def number_to_word(self):
        # Конвертирует целое число в прописной вариант
        #
        # Вводимое число преобразуется в список, по длине списка
        # определяется количество разрядов в числе, исходя из длины
        # программа попадает в нужный блок оператора ветвления.
        # В теле ветвления определяется ключ. Ключом является само значение
        # в списке с соответсвующим индексом. С помощью полученного ключа
        # из соответсвующего словаря извлекается прописной вариант числа.
        list_number = list(self.n)
        length = len(list_number)
        # Для числа 0
        if length == 1 and int(list_number[0]) == 0:
            return self.ZERO
        # Для чисел 1 - 9
        elif length == 1:
            key = int(list_number[0])
            word = self.ONES[key]
            return word
        # Для чисел 10 - 19
        elif length == 2 and int(list_number[0]) == 1:
            key_teens = int(list_number[0] + list_number[1])
            word = self.TEENS[key_teens]
            return word
        # Для чисел 20 - 99
        elif length == 2 and int(list_number[0]) > 1:
            key_tens = int(list_number[0])
            key_ones = int(list_number[1])
            word_tens = self.TENS[key_tens]
            word_ones = self.ONES[key_ones]
            word = list()
            word.append(word_tens)
            word.append(word_ones)
            word = ' '.join(word)
            return word
        # Для чисел 101 - 109
        elif length == 3 and int(list_number[1]) == 0:
            key_hundreds = int(list_number[0])
            key_ones = int(list_number[2])
            word_hundreds = self.HUNDREDS[key_hundreds]
            word_ones = self.ONES[key_ones]
            word = list()
            word.append(word_hundreds)
            word.append(word_ones)
            word = ' '.join(word)
            return word
        # Для чисел х10 - х19
        elif length == 3 and int(list_number[1]) == 1:
            key_hundreds = int(list_number[0])
            key_teens = int(list_number[1] + list_number[2])
            word_hundreds = self.HUNDREDS[key_hundreds]
            word_teens = self.TEENS[key_teens]
            word = list()
            word.append(word_hundreds)
            word.append(word_teens)
            word = ' '.join(word)
            return word
        # Для чисел х20 - х99,
        elif length == 3 and int(list_number[1]) > 1:
            key_hundreds = int(list_number[0])
            key_tens = int(list_number[1])
            key_ones = int(list_number[2])
            word_hundreds = self.HUNDREDS[key_hundreds]
            word_tens = self.TENS[key_tens]
            word_ones = self.ONES[key_ones]
            word = list()
            word.append(word_hundreds)
            word.append(word_tens)
            word.append(word_ones)
            word = ' '.join(word)
            return word
        else:
            raise ValueError
        # TODO: Для чисел 1,000 - 999,999
        # elif length == 4:
        #     key_thousands = int(list_number[0])
        #     key_hundreds = int(list_number[1])
        #     key_tens = int(list_number[2])
        #     key_ones = int(list_number[3])
        #     word_thousands = self.THOUSANDS[key_thousands]
        #     word_hundreds = self.HUNDREDS[key_hundreds]
        #     word_tens = self.TENS[key_tens]
        #     word_ones = self.ONES[key_ones]
        #     word = list()
        #     word.append(word_thousands)
        #     word.append(word_hundreds)
        #     word.append(word_tens)
        #     word.append(word_ones)
        #     word = ' '.join(word)
        #     return word


def main():
    while True:
        try:
            digit_number = input('Enter the number:\n')
            if not digit_number:
                print('NUMBER TO WORD\n'
                      '1. Number must be positive.\n'
                      '2. Number must be from 0 to 999.\n')
                continue
            word_number = WordNumber(digit_number)
            word = word_number.number_to_word()
            print(word)
        except ValueError:
            print('Entry must contain only positive number from 0 to 999.\n')


if __name__ == '__main__':
    main()
