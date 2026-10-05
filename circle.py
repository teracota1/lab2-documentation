import math


def area(r):
    """
    Возвращает площадь круга.
    Параметры:
        r(float): радиус круга
    Пример:
        area(1)=3.14 * 1 * 1=3.14

    """
    
    return math.pi * r * r


def perimeter(r):
    """
    Возвращает длину окружности.
    Параметры:
        r(float): радиус круга
    Пример:
        perimeter(1)=2 * 3.14 * 1=6.28

    """
    return 2 * math.pi * r

