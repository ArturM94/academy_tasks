import sys


class Envelopes:
    def __init__(self):
        print('Введите поочередно размеры двух конвертов (a, b) и (c, d):')
        # От пользователя принимаются параметры конвертов,
        # вызывается функция определения вхождения конверта
        self.a = float(input())
        self.b = float(input())
        self.c = float(input())
        self.d = float(input())
        self.envelope_entry(self.a, self.b, self.c, self.d)

    def envelope_entry(self, a, b, c, d):
        # Сравниваются стороны конвертов,
        # вызывается функция проверки результата
        entry_result = (a < d) and (c < b)
        self.check_result(entry_result)

    def check_result(self, entry_result):
        # Если второй конверт входит в первый, выводится утвердительный
        # ответ, иначе выводится отрицательный, после чего вызывается
        # функция на запрос продолжения выполнения программы
        if entry_result is True:
            print('Второй конверт можно вложить в первый.')
            self.do_continue()
        else:
            print('Второй конверт нельзя вложить в первый.')
            self.do_continue()

    def do_continue(self):
        # Если пользователь ответил утвердительно, вызывается инициализатор,
        # иначе программа завершается с выводом соответвующего уведомления
        print('Хотите продолжить? [y / yes]')
        answer = str(input())
        if (answer.lower() == 'y') or (answer.lower() == 'yes'):
            self.__init__()
        else:
            print('Работа с программой завершена.')
            sys.exit()


def main():
    # Точка входа вызывает класс Envelopes
    return Envelopes()


if __name__ == '__main__':
    main()
