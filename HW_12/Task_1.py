# Task1
# Реалізуйте перевірку даних на те що вершини є Point за допомогою property

class Point:
    x_coord = 0
    y_coord = 0

    def __init__(self, x, y):
        # check type (int, float)
        point_class_intORfloat_properties_confirmation = ((type(x) in (int, float)) and (type(y) in (int, float)))
        if point_class_intORfloat_properties_confirmation:
            self.x_coord = x
            self.y_coord = y

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
        print(f'self = {self}')
        print(f'other = {other}')
        return Line(self, other)


class Line:
    begin_point = None
    end_point = None

    def __init__(self, begin, end):
        # check type Point
        print('\n__Task2__Line__')
        line_class_Point_properties_confirmation = isinstance(begin, Point) and isinstance(end, Point)
        print(f'line_class_Point_properties_confirmation = {line_class_Point_properties_confirmation}')
        if line_class_Point_properties_confirmation:
            self.begin_point = begin
            self.end_point = end

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


class Triangle:
    one_side = None
    side_list = []

    @property
    def side_length(self):
        return self.one_side

    @side_length.setter
    def side_length(self, value):
        triangle_class_Point_properties_confirmation = isinstance(value, Point)
        if triangle_class_Point_properties_confirmation:
            self.one_side = value.x_coord + value.y_coord
            self.side_list.append(self.one_side)

    def __str__(self):
        return f'side_list = {self.side_list}'

    def area(self):
        p_half = 0.5 * (self.side_list[0] + self.side_list[1] + self.side_list[2])
        triangle_area = (p_half * (p_half - self.side_list[0]) * (p_half - self.side_list[1]) * (
                    p_half - self.side_list[2])) ** 0.5
        return f'Triangle_area = {triangle_area}'


p1 = Point(2, 2)
p2 = Point(5, 6)
p3 = Point(9, 2)

triangle = Triangle()

triangle.side_length = p1
triangle.side_length = p2
triangle.side_length = p3

print(triangle)
print(triangle.area())
