
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
import itertools
from math import cos, sin, pi







def tr_translate(polygon, dx=0, dy=0):
    """
    Параллельный перенос полигона.
    
    Args:
        polygon: список точек полигона [(x1,y1), (x2,y2), ...]
        dx: смещение по x
        dy: смещение по y
    """
    return [(x + dx, y + dy) for x, y in polygon]

def tr_rotate(polygon, angle_degrees=0, center_x=0, center_y=0):
    """
    Поворот полигона вокруг заданной точки.
    
    Args:
        polygon: список точек полигона
        angle_degrees: угол поворота в градусах
        center_x, center_y: центр поворота
    """
    angle = angle_degrees * pi / 180  # перевод в радианы
    cos_a = cos(angle)
    sin_a = sin(angle)
    
    result = []
    for x, y in polygon:
        # Сдвиг к началу координат
        x_shifted = x - center_x
        y_shifted = y - center_y
        
        # Поворот
        x_rotated = x_shifted * cos_a - y_shifted * sin_a
        y_rotated = x_shifted * sin_a + y_shifted * cos_a
        
        # Сдвиг обратно
        result.append((x_rotated + center_x, y_rotated + center_y))
    
    return result

def tr_symmetry(polygon, axis='x'):
    """
    Симметричное отражение полигона.
    
    Args:
        polygon: список точек полигона
        axis: ось симметрии ('x', 'y' или 'origin')
    """
    if axis == 'x':
        return [(x, -y) for x, y in polygon]
    elif axis == 'y':
        return [(-x, y) for x, y in polygon]
    elif axis == 'origin':
        return [(-x, -y) for x, y in polygon]
    else:
        raise ValueError("axis должен быть 'x', 'y' или 'origin'")

def tr_homothety(polygon, k=1, center_x=0, center_y=0):
    """
    Гомотетия полигона (масштабирование относительно точки).
    
    Args:
        polygon: список точек полигона
        k: коэффициент гомотетии (k > 0)
        center_x, center_y: центр гомотетии
    """
    if k <= 0:
        raise ValueError("Коэффициент гомотетии должен быть положительным")
        
    result = []
    for x, y in polygon:
        # Вычисляем вектор от центра до точки
        dx = x - center_x
        dy = y - center_y
        
        # Умножаем вектор на коэффициент и добавляем к центру
        new_x = center_x + k * dx
        new_y = center_y + k * dy
        
        result.append((new_x, new_y))
    
    return result

# Визуализация результата
# if __name__ == "__main__":
    # Создаем и визуализируем ленту прямоугольников
    

    # hexagons_list = list(itertools.islice(hexagons, 5))  # Сохраняем список из 5 шестиугольников
    # # visualize_polygons(hexagons_list)    # Показываем 5 шестиугольников
    
    # # Показываем комбинацию из 7 фигур
    # visualize_polygons(itertools.chain(
    #     itertools.islice(rectangles, 5),
    #     itertools.islice(triangles, 5),
    #     itertools.islice(hexagons, 5)
    # ))
    
    # # Трансформации только для шестиугольников:
    
    # # 1. Параллельный перенос
    # translated = map(lambda p: tr_translate(p, dx=2, dy=1), hexagons_list)
    # visualize_polygons(translated)
    
    # # 2. Поворот на 45 градусов вокруг начала координат
    # rotated = map(lambda p: tr_rotate(p, angle_degrees=45), hexagons_list)
    # visualize_polygons(rotated)
    
    # # 3. Симметрия относительно оси X
    # symmetric = map(lambda p: tr_symmetry(p, axis='x'), hexagons_list)
    # visualize_polygons(symmetric)
    
    # # 4. Гомотетия с коэффициентом 2 относительно начала координат
    # scaled = map(lambda p: tr_homothety(p, k=2, center_x=0, center_y=0), hexagons_list)
    # visualize_polygons(scaled)
    
    # # Можно также попробовать гомотетию с другими параметрами:
    # # Например, с центром в точке (2,2) и коэффициентом 1.5
    # scaled2 = map(lambda p: tr_homothety(p, k=1.5, center_x=2, center_y=2), hexagons_list)
    # visualize_polygons(scaled2)