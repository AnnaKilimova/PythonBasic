# Task1
# Доопрацюйте класс Point так, щоб в атрибути x та y обʼєктів цього класу
# можна було записати тільки обʼєкти класу int або float

# Task2
# Доопрацюйте класс Line так, щоб в атрибути begin та end обʼєктів цього класу можна було записати
# тільки обʼєкти класу Point

# Task3
# Створіть класс Triangle (трикутник), який задається трьома точками (обʼєкти классу Point).
# Реалізуйте перевірку даних, аналогічно до класу Line. Визначет метод, що містить площу трикутника.
# Для обчислень можна використати формулу Герона (https://en.wikipedia.org/wiki/Heron%27s_formula)

class Point:
    x_coord = 0
    y_coord = 0

    """Task1_Begin"""

    def __init__(self, x, y):
        # check type (int, float)
        print('__Task1__Point__')
        point_class_intORfloat_properties_confirmation = (type(x) is int or type(x) is float) and (type(y) is int or type(y) is float)
        print(f'point_class_intORfloat_properties_confirmation for [{self}] object is {point_class_intORfloat_properties_confirmation}')
        if point_class_intORfloat_properties_confirmation:
            self.x_coord = x
            self.y_coord = y

    """Task1_End"""

    def __str__(self):
        return f'Point {self.x_coord} {self.y_coord}'

    def __getitem__(self, item):
        print(f'__getitem__ {item}')
        if item == 0:
            return self.x_coord
        elif item == 1:
            return self.y_coord
        else:
            raise TypeError

    def __setitem__(self, item, value):
        print(f'__setitem__ {item}, {value}')
        if item == 0:
            self.x_coord = value
        elif item == 1:
            self.y_coord = value
        else:
            raise TypeError

    def __eq__(self, other):
        # check type Point
        return self.x_coord == other.x_coord and self.y_coord == other.y_coord

    def __add__(self, other):
        # складываем 2 точки чтоб получить линию
        print(f'self = {self}')
        print(f'other = {other}')
        return Line(self, other)


class Line:
    begin_point = None
    end_point = None

    """Task2_Begin"""

    def __init__(self, begin, end):
        # check type Point
        print('\n__Task2__Line__')
        line_class_Point_properties_confirmation = isinstance(begin, Point) and isinstance(end, Point)
        print(f'line_class_Point_properties_confirmation = {line_class_Point_properties_confirmation}')
        if line_class_Point_properties_confirmation:
            self.begin_point = begin
            self.end_point = end

    """Task2_End"""

    def __str__(self):
        return f'Line from [{self.begin_point}] to [{self.end_point}]'

    def length(self):
        k1 = self.begin_point.x_coord - self.end_point.x_coord
        k2 = self.begin_point.y_coord - self.end_point.y_coord

        return (k1 ** 2 + k2 ** 2) ** 0.5

    def __len__(self):
        """ len(obj) """
        return 2

    def __contains__(self, item):
        """ a in b """
        print('__contains__', item)
        return self.begin_point == item or self.end_point == item


"""Task3_Begin"""


class Triangle:
    one_side = None
    two_side = None
    three_side = None

    def __init__(self, one, two, three):
        # check type Point
        print('\n__Task3__Triangle__')
        triangle_class_Point_properties_confirmation = isinstance(one, Point) and isinstance(two, Point) and isinstance(three, Point)
        print(f'triangle_class_Point_properties_confirmation = {triangle_class_Point_properties_confirmation}')
        if triangle_class_Point_properties_confirmation:
            self.one_side = one.x_coord + one.y_coord
            self.two_side = two.x_coord + two.y_coord
            self.three_side = three.x_coord + three.y_coord
            print(f'Point_one = {one} \nPoint_two = {two} \nPoint_three = {three}')

    def __str__(self):
        return f'One_side = {self.one_side},  Two_side = {self.two_side},  Three_side = {self.three_side}'

    def area(self):
        p_half = 0.5 * (self.one_side + self.two_side + self.three_side)
        triangle_area = (p_half * (p_half - self.one_side) * (p_half - self.two_side) * (p_half - self.three_side)) ** 0.5
        return f'Triangle_area = {triangle_area}'


"""Task3_End"""

p1 = Point(2, 2)
p2 = Point(5, 6)
p3 = Point(9, 2)

line = Line(p1, p2)
print(line)

triangle = Triangle(p1, p2, p3)
print(triangle)
print(triangle.area())
