from math import sqrt
from collections import OrderedDict


class Triangles:
    def __init__(self):
        # Ввод данных
        self.triangle = input('Input triangles data in format: <name>, '
                              '<side length>, <side length>, <side length>.\n'
                              'Data must satisfy next conditions:\n'
                              'a < b + c\n'
                              'b < a + c\n'
                              'c < a + b\n')
        self.validation()

    def validation(self):
        # Проверка на валидность вводимых данных

        # Разбиение треугольника на список
        triangle = list(self.triangle.split(', '))
        # Распределение списка в переменные
        name = triangle[0].lower()
        a = float(triangle[1])
        b = float(triangle[2])
        c = float(triangle[3])
        if a < (b + c) and b < (a + c) and c < (a + b):
            self.area_calculation(name, a, b, c)
        else:
            print('Invalid data. The non-existent triangle. Try again.')
            self.__init__()

    def area_calculation(self, name, a, b, c):
        # Расчет площади треугольника
        sp = (a+b+c) / 2.0  # semi perimeter
        area = round(sqrt(sp * (sp-a) * (sp-b) * (sp-c)), 2)
        triangle = {name: str(area)}
        self.recording_data(triangle)

    def recording_data(self, triangle):
        # Запись треугольников в словарь
        triangles_dict = {}
        triangles_dict.update(triangle)
        print(triangles_dict)
        self.do_continue(triangles_dict)
        # TODO: Реализовать рабочий метод дозаписи данных в словарь

    def do_continue(self, triangles_dict):
        # Если пользователь ответил утвердительно, вызывается инициализатор,
        # иначе программа завершается с выводом соответвующего уведомления
        print('Add another triangle? [y / yes]')
        answer = str(input())
        if (answer.lower() == 'y') or (answer.lower() == 'yes'):
            self.__init__()
        else:
            # TODO: Не забыть вызвать метод сортировки вместо вывода данных
            # self.sorting(triangles_dict)
            self.print_out_data(triangles_dict)

    # def sorting(self, triangles_dict):
    #     # TODO: Реализовать метод сортировки словаря по значению
    #     # sorted(triangles_dict.items(), key=lambda x: x[1], reverse=True)
    #     OrderedDict(sorted(triangles_dict.items(), key=lambda t: t[1]))
    #     print(triangles_dict)
    #     self.print_out_data(triangles_dict)

    def print_out_data(self, triangles_dict):
        print('============= Triangles list: ===============')
        for i, key in enumerate(triangles_dict, 1):
            print(f'{i}. [Triangle {key}]: {triangles_dict[key]} cm')


def main():
    # Точка входа вызывает класс Envelopes
    Triangles()


if __name__ == '__main__':
    main()

