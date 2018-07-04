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


def validation(a, b, c):
    # Проверка на валидность вводимых данных
    if a < (b + c) and b < (a + c) and c < (a + b):
        return True
    else:
        return False


def split(triangle):
    # Разделяет входящую строку на составляющие
    # треугольника: имя и стороны
    triangle = list(triangle.split(', '))
    name = triangle[0].lower()
    side_a = float(triangle[1])
    side_b = float(triangle[2])
    side_c = float(triangle[3])
    return name, side_a, side_b, side_c


def main():
    triangles_dict = dict()
    while True:
        try:
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

            name, side_a, side_b, side_c = split(triangle)
            is_valid = validation(side_a, side_b, side_c)

            if is_valid:
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
            else:
                print('Invalid data. The non-existent triangle.\n')
                continue
        except (ValueError, IndexError):
            print('Invalid data. Entry must contain 4 values. <side length> '
                  'must contain only numbers.\n')
            continue


if __name__ == '__main__':
    main()
