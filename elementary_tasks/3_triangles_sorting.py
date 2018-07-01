from math import sqrt
from collections import Counter


class Triangles:
    def __init__(self):
        self.triangle = input('Input triangles data in format: <name>, '
                              '<side length>, <side length>, <side length>.\n'
                              'Data must satisfy next conditions:\n'
                              'a < b + c\n'
                              'b < a + c\n'
                              'c < a + b\n')

    def validation(self):
        # Проверка на валидность вводимых данных
        # Если данные валидны, возвращаются имя и стороны треугольника,
        # иначе вызывает init и метод валидации
        triangle = list(self.triangle.split(', '))
        name = triangle[0].lower()
        a = float(triangle[1])
        b = float(triangle[2])
        c = float(triangle[3])
        if a < (b + c) and b < (a + c) and c < (a + b):
            return name, a, b, c
        else:
            print('Invalid data. The non-existent triangle. Try again.')
            self.__init__()
            self.validation()

    @staticmethod
    def area_calculation(name, a, b, c):
        # Расчет площади треугольника
        # Возвращает площадь по формуле Герона
        sp = (a+b+c) / 2.0  # semi perimeter
        area = round(sqrt(sp * (sp-a) * (sp-b) * (sp-c)), 2)
        triangle = {name: area}
        return triangle

    @staticmethod
    def do_continue():
        # Если пользователь ответил утвердительно, возвращается True,
        # иначе возвращается False
        print('Add another triangle? [y / yes]')
        answer = str(input())
        if (answer.lower() == 'y') or (answer.lower() == 'yes'):
            return True
        else:
            return False

    @staticmethod
    def sorting(triangles_dict):
        # Сортирует словарь по значению в порядке убывания площади
        # Возвращает отсортированный словарь
        triangles_dict = Counter(triangles_dict)
        triangles_dict = triangles_dict.most_common()
        triangles_dict = dict(triangles_dict)
        return triangles_dict

    @staticmethod
    def print_out_data(sorted_dict):
        # Выводит данные в консоль
        print('============= Triangles list: ===============')
        for i, key in enumerate(sorted_dict, 1):
            print(f'{i}. [Triangle {key}]: {sorted_dict[key]} cm')


def main():
    triangles_dict = dict()
    triangles = Triangles()
    while True:
        name, a, b, c = triangles.validation()
        triangle = triangles.area_calculation(name, a, b, c)
        triangles_dict.update(triangle)
        go_on = triangles.do_continue()
        if go_on is True:
            triangles.__init__()
        elif go_on is False:
            sorted_dict = triangles.sorting(triangles_dict)
            triangles.print_out_data(sorted_dict)
            break


if __name__ == '__main__':
    main()

