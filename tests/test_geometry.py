import math
import pytest

from geometry.circle import Circle
from geometry.triangle import Triangle
from geometry.factory import compute_area
from geometry.exceptions import InvalidTriangleError


def test_circle_area():
    c = Circle(2)
    assert math.isclose(c.area(), math.pi * 4)


def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert math.isclose(t.area(), 6.0)


def test_triangle_right():
    t = Triangle(3, 4, 5)
    assert t.is_right()


def test_triangle_not_right():
    t = Triangle(5, 5, 6)
    assert not t.is_right()


def test_invalid_triangle():
    with pytest.raises(InvalidTriangleError):
        Triangle(1, 2, 10)


def test_compute_area_with_instance():
    assert math.isclose(compute_area(Circle(1)), math.pi)
    assert math.isclose(compute_area(Triangle(3, 4, 5)), 6.0)


def test_compute_area_with_dict():
    assert math.isclose(compute_area({'type': 'circle', 'radius': 1}), math.pi)
    assert math.isclose(
        compute_area(
            {'type': 'triangle', 'a': 3, 'b': 4, 'c': 5}
        ), 6.0
    )
