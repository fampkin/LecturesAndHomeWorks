import numpy as np
from scipy.stats import cauchy
import matplotlib.pyplot as plt

# Параметры распределения Коши
loc = 1  # параметр сдвига (a)
scale = 2  # параметр масштаба (γ)

# Теоретическая вероятность
theoretical_prob = 0.5 - np.arctan(7)/np.pi
print(f"Теоретическая вероятность P(1/X > 3) = P(X < 1/3) = {theoretical_prob:.9f}")

# Демонстрация статистической устойчивости
sample_sizes = [1000, 10000, 100000, 1000000]
results = []

for size in sample_sizes:
    # Генерируем выборку
    sample = cauchy.rvs(loc=loc, scale=scale, size=size)
    # Вычисляем долю значений, где 1/X > 3 (т.е. X < 1/3)
    prob = np.mean(sample < 1/3)
    results.append(prob)
    print(f"Размер выборки {size}: P(1/X > 3) ≈ {prob:.9f}")

# Визуализация статистической устойчивости
plt.figure(figsize=(10, 6))
plt.semilogx(sample_sizes, results, 'bo-', label='Эмпирическая вероятность')
plt.axhline(y=theoretical_prob, color='r', linestyle='--', 
            label=f'Теоретическая вероятность = {theoretical_prob:.9f}')
plt.grid(True)
plt.xlabel('Размер выборки')
plt.ylabel('P(1/X > 3)')
plt.title('Статистическая устойчивость вероятности P(1/X > 3)')
plt.legend()
plt.show()

# Визуализация плотности распределения
x = np.linspace(-2, 4, 1000)
pdf = cauchy.pdf(x, loc=loc, scale=scale)

plt.figure(figsize=(10, 6))
plt.plot(x, pdf, 'b-', label='Плотность распределения')
plt.fill_between(x[x < 1/3], pdf[x < 1/3], color='red', alpha=0.3, 
                 label='P(X < 1/3)')
plt.axvline(x=1/3, color='k', linestyle='--', label='x = 1/3')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Плотность распределения Коши Ca(1, 2)')
plt.legend()
plt.show() 