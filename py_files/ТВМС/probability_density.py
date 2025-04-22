import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Создаем данные
x = np.linspace(-4, 4, 1000)
pdf = norm.pdf(x)  # Плотность вероятности
cdf = norm.cdf(x)  # Функция распределения

# Создаем график
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# График плотности вероятности
ax1.plot(x, pdf, 'b-', label='Плотность вероятности')
ax1.fill_between(x[(x >= -1) & (x <= 1)], 
                pdf[(x >= -1) & (x <= 1)], 
                alpha=0.3, 
                color='red',
                label='P(-1 ≤ X ≤ 1)')
ax1.grid(True)
ax1.set_title('Плотность вероятности (PDF)')
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)')
ax1.legend()

# Добавляем пояснения
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
textstr = '\n'.join([
    'Свойства плотности вероятности:',
    '• Всегда неотрицательна: f(x) ≥ 0',
    '• Интеграл по всей области равен 1',
    '• Вероятность попадания в интервал -',
    '  это площадь под кривой',
    '• Размерность: 1/единица измерения X'
])
ax1.text(1.5, 0.3, textstr, bbox=props, fontsize=10)

# График функции распределения
ax2.plot(x, cdf, 'g-', label='Функция распределения')
ax2.grid(True)
ax2.set_title('Функция распределения (CDF)')
ax2.set_xlabel('x')
ax2.set_ylabel('F(x)')
ax2.legend()

# Вычисляем вероятность попадания в интервал [-1, 1]
prob = norm.cdf(1) - norm.cdf(-1)

plt.tight_layout()
plt.show()

print(f"Вероятность попадания в интервал [-1, 1]: {prob:.4f}")
print("Это соответствует площади закрашенной области под кривой плотности") 