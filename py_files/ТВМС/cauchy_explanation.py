import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import cauchy, norm

# Создаем данные
x = np.linspace(-5, 5, 1000)
cauchy_pdf = cauchy.pdf(x)
normal_pdf = norm.pdf(x)

# Создаем график
plt.figure(figsize=(12, 6))

# График плотностей
plt.plot(x, cauchy_pdf, 'r-', label='Распределение Коши', linewidth=2)
plt.plot(x, normal_pdf, 'b--', label='Нормальное распределение', linewidth=2)

plt.title('Сравнение распределения Коши и нормального распределения')
plt.xlabel('x')
plt.ylabel('Плотность вероятности')
plt.grid(True)
plt.legend()

# Добавляем текст с основными свойствами
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
textstr = '\n'.join([
    'Свойства распределения Коши:',
    '• Симметрично относительно x=0',
    '• Не имеет математического ожидания',
    '• Не имеет дисперсии',
    '• Имеет "тяжелые хвосты"'
])
plt.text(2, 0.3, textstr, bbox=props, fontsize=10)

plt.show()

# Демонстрация "тяжелых хвостов"
print("Вероятности для |X| > 3:")
print(f"Распределение Коши: {2 * (1 - cauchy.cdf(3)):.4f}")
print(f"Нормальное распределение: {2 * (1 - norm.cdf(3)):.4f}") 