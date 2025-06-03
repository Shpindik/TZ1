# geometry-lib

Простая библиотека для вычисления площади фигур:
- Круг
- Треугольник (+ определение прямоугольного)
- Возможность расширения
- Фабрика `compute_area()` для работы с фигурами без знания типа

🛠 Установка и запуск
1. Перейди в корень проекта:
```
cd TZ1
```
2. Установи библиотеку локально:
```
pip install -e .
```

✅ Проверка
В Python:
```
from geometry.circle import Circle
from geometry.triangle import Triangle
from geometry.factory import compute_area

print(Circle(3).area())
print(Triangle(3, 4, 5).is_right())
print(compute_area({'type': 'triangle', 'a': 3, 'b': 4, 'c': 5}))
```