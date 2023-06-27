# class Frange:
#
#     def __init__(self, start=0.0, stop=0.0, step=3.0):
#         self.start = start
#         self.stop = stop
#         self.step = step
#
#     def __iter__(self):
#         self.value = self.start - self.step
#         return self
#
#     def __next__(self):
#         if self.value + self.step < self.stop:
#             self.value += self.step
#             return self.value
#         else:
#             raise StopIteration
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


class Triangle:

    def __init__(self, a, b, c):
        self.firstPoint1 = a
        self.firstPoint2 = b
        self.firstPoint3 = c

    def __iter__(self):
        return iter([self.firstPoint1, self.firstPoint2, self.firstPoint3])

p1 = Point(2, 2)
p2 = Point(5, 6)
p3 = Point(9, 2)

tr = Triangle(p1, p2, p3)

for point in tr:
    print(point)


# class Frange2D:
#
#     my_list = []
#
#     def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
#         self.rows = rows
#         self.fr = Frange(start, stop, step)
#         self.my_list = ['one', 'two', 'three', 'four']
#
#     def __iter__(self):
#         self.value = 0
#         return self
#
#     def __next__(self):
#         if self.value < self.rows:
#             self.value += 1
#             return iter(self.fr)
#         else:
#             raise StopIteration


# fr = Frange2D(my_listх, 3, 0.5, 4)
# for row in fr:
#     for x in row:
#         print(x, end='  ')
#     print()




