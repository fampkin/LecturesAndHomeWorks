import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import cauchy

# Создаем фигуру
plt.figure(figsize=(12, 5))

# График исходного распределения Коши
x = np.linspace(-5, 5, 1000)
fx = cauchy.pdf(x)

plt.subplot(1, 2, 1)
plt.plot(x, fx, 'b-', label='f(x) = 1/(π(1+x²))')
plt.title('Плотность распределения X (Коши)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()

# График преобразованного распределения
# Y принимает значения от 0 до 1
y = np.linspace(0.001, 0.999, 1000)  # Избегаем точек 0 и 1 из-за особенностей
fy = 1 / (np.pi * np.sqrt(y * (1-y)))

plt.subplot(1, 2, 2)
plt.plot(y, fy, 'r-', label='f_Y(y)')
plt.title('Плотность распределения Y = X²/(1+X²)')
plt.xlabel('y')
plt.ylabel('f_Y(y)')
plt.grid(True)
plt.legend()
plt.ylim(0, 10)  # Ограничиваем ось Y для лучшей визуализации

plt.tight_layout()
plt.show()

print("Аналитическое решение:")
print("Плотность распределения Y имеет вид:")
print("f_Y(y) = 1/(π√(y(1-y))) для y ∈ (0,1)")
print("f_Y(y) = 0 для y ∉ [0,1]") 