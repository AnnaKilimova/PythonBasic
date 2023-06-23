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
        if (type(x) is int or type(x) is float) and (type(y) is int or type(y) is float):
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


class Line:
    begin_point = None
    end_point = None

    """Task2_Begin"""

    def __init__(self, begin, end):
        # check type Point
        if isinstance(begin, Point) and isinstance(end, Point):
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
        type_one = type(one) is int or type(one) is float
        type_two = type(two) is int or type(two) is float
        type_three = type(three) is int or type(three) is float
        if type_one and type_two and type_three:
            self.one_side = one
            self.two_side = two
            self.three_side = three

    def area(self):
        p_half = 0.5 * (self.one_side + self.two_side + self.three_side)
        return (p_half * (p_half - self.one_side) * (p_half - self.two_side) * (p_half - self.three_side)) ** 0.5


"""Task3_End"""

p1 = Point(2, 2)
p2 = Point(5, 6)
p3 = Point(9, 2)

line1 = Line(p1, p2)
line2 = Line(p2, p3)
line3 = Line(p3, p1)

triangle = Triangle(line1.length(), line2.length(), line3.length())

print(triangle.area())
