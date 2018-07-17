from math import sqrt

from elementary_tasks.do_continue import do_continue


class Triangle:
    def __init__(self, name, side_a, side_b, side_c, semi_perimeter=None,
                 area=None):
        """Initialisation method

        :param name: -- Name of triangle
        :param side_a: -- Side a of triangle
        :param side_b: -- Side b of triangle
        :param side_c: -- Side c of triangle
        :param semi_perimeter: -- Semi perimeter of triangle
        :param area: -- Area of triangle
        """
        self.name = name
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.sp = semi_perimeter
        self.area = area

    def __str__(self):
        """str method

        Redefines str() function for triangles output

        :return: -- String in specified format
        """
        return f'[Triangle {self.name}]: {self.area} cm²'

    def area_calculation(self):
        """Calculating the area of triangle

        Method returns the area by Heron's formula

        :return: area -- Area of triangle
        """
        self.sp = (self.side_a + self.side_b + self.side_c) / 2.0
        self.area = round(sqrt(self.sp * (self.sp - self.side_a) *
                               (self.sp - self.side_b) *
                               (self.sp - self.side_c)), 2)
        return self.area


class ValidationError(ValueError):
    """Exception for nonexistent triangle"""
    pass


def validation(triangle_data):
    """Validation of input data

    :param triangle_data: --- String data of triangle
    :return: -- Valid Triangle object or ValidationError
    """
    triangle_data = list(triangle_data.split(', '))
    name = triangle_data[0].lower()
    side_a = float(triangle_data[1])
    side_b = float(triangle_data[2])
    side_c = float(triangle_data[3])

    if side_a < (side_b + side_c) and side_b < (side_a + side_c) and \
            side_c < (side_a + side_b):
        return Triangle(name, side_a, side_b, side_c)
    else:
        raise ValidationError


def sorting(triangles_list):
    """Sorts the dictionary

    Sorts by value in order of decreasing area

    :param triangles_list: -- Collection of triangles
    :return: triangles_dict -- Sorted triangles
    """
    sorted_list = sorted(triangles_list, key=lambda x: x.area, reverse=True)
    return sorted_list


def main():
    triangles_list = []
    is_continue = True

    while is_continue:
        triangle_data = input('Enter triangle data:\n')
        # The instruction for using the program for empty input
        if not triangle_data:
            print('1. Enter triangle data in format: <name>, '
                  '<side length>, <side length>, <side length>.\n'
                  '2. Data must satisfy next conditions:\n'
                  'a < b + c\n'
                  'b < a + c\n'
                  'c < a + b\n')
            continue

        try:
            # Create triangle object
            triangle = validation(triangle_data)
        except ValidationError:
            print('Nonexistent triangle. Sides must satisfy triangle '
                  'inequality.\n')
            continue
        except IndexError:
            print('Invalid range. Entry must contain 4 values.\n')
            continue
        except ValueError:
            print('Invalid data. <side length> must contain only numbers.\n')
            continue

        triangle.area = triangle.area_calculation()
        triangles_list.append(triangle)
        answer = str(input('Do you want to continue? [y / yes]\n'))
        is_continue = do_continue(answer)

    sorted_list = sorting(triangles_list)
    print('============= Triangles list: ===============')
    for i, triangle in enumerate(sorted_list, 1):
        print(i, end='. ')
        print(triangle)


if __name__ == '__main__':
    main()
