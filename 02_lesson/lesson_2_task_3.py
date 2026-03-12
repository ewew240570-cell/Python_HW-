import math


def square(side):
    area = side * side
    if not isinstance(side, int):
        area = math.ceil(area)
    return area


print("Площадь квадрата со стороной 5:", square(5))
print("Площадь квадрата со стороной 4:", square(4))
print("Площадь квадрата со стороной 3.2:", square(3.2))
print("Площадь квадрата со стороной 2.3:", square(2.3))
