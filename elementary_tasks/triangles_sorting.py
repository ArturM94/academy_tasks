from math import sqrt

from elementary_tasks.do_continue import do_continue


class Triangle:
    def __init__(self, name, side_a, side_b, side_c):
        """Initialisation method

        :param name: -- Name of triangle
        :param side_a: -- Side a of triangle
        :param side_b: -- Side b of triangle
        :param side_c: -- Side c of triangle
        """
        self.name = name
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area_calculation(self):
        """Calculating the area of triangle

        Method returns the area by Heron's formula

        :return: triangle_area
        """
        sp = (self.side_a + self.side_b + self.side_c) / 2.0  # semi perimeter
        area = round(sqrt(sp * (sp - self.side_a) * (sp - self.side_b) *
                          (sp - self.side_c)), 2)
        triangle_area = {self.name: area}
        return triangle_area


def validation(triangle):
    """Validation of input data

    :param triangle:
    :return: valid data of False
    """
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


def sorting(triangles_dict):
    """Sorts the dictionary

    Sorts by value in order of decreasing area

    :param triangles_dict: -- Collection of triangles
    :return: triangles_dict -- Sorted triangles
    """
    triangles_dict = sorted(triangles_dict.items(), key=lambda item: item[1],
                            reverse=True)
    triangles_dict = dict(triangles_dict)
    return triangles_dict


def print_out_data(sorted_dict):
    """Prints data in console

    :param sorted_dict: -- Sorted triangles
    :return: -- Strings with triangle and its area
    """
    # Выводит данные в консоль
    print('============= Triangles list: ===============')
    for i, key in enumerate(sorted_dict, 1):
        print(f'{i}. [Triangle {key}]: {sorted_dict[key]} cm²')


def main():
    triangles_dict = dict()
    is_continue = True

    while is_continue:
        triangle = input('Enter triangle data:\n')
        # The instruction for using the program is called
        # if 'triangle' have no parameters
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
        answer = str(input('Do you want to continue? [y / yes]\n'))
        is_continue = do_continue(answer)

    sorted_dict = sorting(triangles_dict)
    print_out_data(sorted_dict)


if __name__ == '__main__':
    main()
