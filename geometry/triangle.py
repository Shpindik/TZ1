import math
from .base import Figure
from .exceptions import InvalidTriangleError


class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        if not self._is_valid_triangle(a, b, c):
            raise InvalidTriangleError('Невалидные стороны треугольника')
        self.a, self.b, self.c = a, b, c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def is_right(self) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(
            sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2,
            rel_tol=1e-9
        )

    @staticmethod
    def _is_valid_triangle(a: float, b: float, c: float) -> bool:
        return a + b > c and a + c > b and b + c > a and all(
            x > 0 for x in [a, b, c]
        )
