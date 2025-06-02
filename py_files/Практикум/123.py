import itertools
import functools
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MplPolygon
from matplotlib.collections import PatchCollection

# --- Вспомогательная функция для сдвига полигона ---
def translate_polygon(polygon, dx=0, dy=0):
    return tuple((x + dx, y + dy) for x, y in polygon)

# --- Генератор прямоугольников ---
def gen_rectangle(width=1, height=1, spacing=0.1, y=0):
    for i in itertools.count():
        dx = i * (width + spacing)
        yield translate_polygon(((0, 0), (0, height), (width, height), (width, 0)), dx=dx, dy=y)

# --- Генератор треугольников (равносторонних, основание на оси x) ---
def gen_triangle(side=1, spacing=0.1, y=0):
    h = (3 ** 0.5) / 2 * side
    for i in itertools.count():
        dx = i * (side + spacing)
        yield translate_polygon(((0, 0), (side / 2, h), (side, 0)), dx=dx, dy=y)

# --- Генератор правильных шестиугольников ---
def gen_hexagon(side=1, spacing=0.1, y=0):
    from math import cos, sin, pi
    dx_step = 1.5 * side + spacing
    for i in itertools.count():
        dx = i * dx_step
        hexagon = tuple(
            (side * cos(pi / 3 * k), side * sin(pi / 3 * k))
            for k in range(6)
        )
        # Сдвигаем так, чтобы основание было на оси x
        min_x = min(x for x, y in hexagon)
        min_y = min(y for x, y in hexagon)
        hexagon = translate_polygon(hexagon, dx=-min_x, dy=-min_y)
        yield translate_polygon(hexagon, dx=dx, dy=y)

# --- Визуализация последовательности полигонов ---
def visualize_polygons(polygons, n=None):
    patches = []
    for i, poly in enumerate(polygons):
        if n is not None and i >= n:
            break
        patches.append(MplPolygon(poly, closed=True))
    fig, ax = plt.subplots()
    p = PatchCollection(patches, alpha=0.5, edgecolor='black', facecolor='white')
    ax.add_collection(p)
    # Автоматически подобрать границы
    all_points = [pt for poly in patches for pt in poly.get_xy()]
    if all_points:
        xs, ys = zip(*all_points)
        ax.set_xlim(min(xs) - 1, max(xs) + 1)
        ax.set_ylim(min(ys) - 1, max(ys) + 1)
    ax.set_aspect('equal')
    plt.show()

# --- Пример использования ---
if __name__ == "__main__":
    # 3 прямоугольника, 2 треугольника, 2 шестиугольника
    rects = itertools.islice(gen_rectangle(width=1, height=0.5, spacing=0.2, y=0), 3)
    tris = itertools.islice(gen_triangle(side=1, spacing=0.2, y=1), 2)
    hexs = itertools.islice(gen_hexagon(side=0.6, spacing=0.2, y=2), 2)
    # Объединяем в одну последовательность
    all_polys = itertools.chain(rects, tris, hexs)
    visualize_polygons(all_polys, n=7)
