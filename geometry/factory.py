from typing import Union
from .circle import Circle
from .triangle import Triangle
from .base import Figure


def compute_area(figure: Union[Figure, dict]) -> float:
    """
    Поддерживает:
    - Figure объект (Circle или Triangle)
    - dict: {'type': 'circle', 'radius': 3} или
    {'type': 'triangle', 'a': 3, 'b': 4, 'c': 5}
    """
    if isinstance(figure, Figure):
        return figure.area()

    if isinstance(figure, dict):
        figure_type = figure.get('type')
        if figure_type == 'circle':
            return Circle(figure['radius']).area()
        elif figure_type == 'triangle':
            return Triangle(figure['a'], figure['b'], figure['c']).area()

    raise ValueError('Неизвестный тип фигуры или формат данных')
