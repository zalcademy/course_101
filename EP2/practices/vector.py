import math


class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, o):
        return Vector(o.x + self.x, o.y + self.y)

    def __str__(self):
        return "{} X {}".format(self.x, self.y)

    def __len__(self):
        return int(math.sqrt(self.x ** 2 + self.y ** 2))

v1 = Vector(5, 2)
v2 = Vector(2, 8)
v3 = v1 + v2
print(v3)
print(len(v3))
