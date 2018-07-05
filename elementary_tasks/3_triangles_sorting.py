from math import sqrt
from collections import Counter


class Triangle:
    def __init__(self, name, side_a, side_b, side_c):
        self.name = name
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

        instance_id = id(Triangle)
        print(f'Instance id: {instance_id}\n')

    def area_calculation(self):
        # Расчет площади треугольника
        # Возвращает площадь по формуле Герона
        sp = (self.side_a + self.side_b + self.side_c) / 2.0  # semi perimeter
        area = round(sqrt(sp * (sp - self.side_a) * (sp - self.side_b) *
                          (sp - self.side_c)), 2)
        triangle_area = {self.name: area}
        return triangle_area

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
        triangles_dict = Counter(triangles_dict).most_common()
        triangles_dict = dict(triangles_dict)
        return triangles_dict

    @staticmethod
    def print_out_data(sorted_dict):
        # Выводит данные в консоль
        print('============= Triangles list: ===============')
        for i, key in enumerate(sorted_dict, 1):
            print(f'{i}. [Triangle {key}]: {sorted_dict[key]} cm')


def validation(triangle):
    # Проверка на валидность вводимых данных
    triangle = list(triangle.split(', '))
    name = triangle[0].lower()
    side_a = float(triangle[1])
    side_b = float(triangle[2])
    side_c = float(triangle[3])
    if side_a < (side_b + side_c) and side_b < (side_a + side_c) and \
            side_c < (side_a + side_b):
        return name, side_a, side_b, side_c
    else:
        return False


def main():
    triangles_dict = dict()
    while True:
        triangle = input('Enter triangle data:\n')
        # Если параметры отсутвуют,
        # вызывается инструкция по использованию
        if not triangle:
            print('1. Enter triangle data in format: <name>, '
                  '<side length>, <side length>, <side length>.\n'
                  '2. Data must satisfy next conditions:\n'
                  'a < b + c\n'
                  'b < a + c\n'
                  'c < a + b\n')
            continue

        try:
            name, side_a, side_b, side_c = validation(triangle)
        except (ValueError, IndexError, TypeError):
            print('Invalid data. Entry must contain 4 values. <side length> '
                  'must contain only numbers.\n')
            continue

        triangle = Triangle(name, side_a, side_b, side_c)
        triangle_area = triangle.area_calculation()
        triangles_dict.update(triangle_area)
        is_continue = triangle.do_continue()

        if is_continue:
            continue
        else:
            sorted_dict = triangle.sorting(triangles_dict)
            triangle.print_out_data(sorted_dict)
            break


if __name__ == '__main__':
    main()
