"""
    author: wangyuxiang
    date: 2020-3-4

    如何使用特殊方法
"""
from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # 也可以重写__str__方法
    def __repr__(self):
        return 'Vector(%r %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        # return bool(self.x or self.y) -> 更高效
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(2, 4)
v2 = Vector(2, 1)
v3 = Vector(3, 4)
v4 = Vector(0, 0)
print(v1 + v2)
print(abs(v3))
print(v3 * 3)
print(bool(v4))
