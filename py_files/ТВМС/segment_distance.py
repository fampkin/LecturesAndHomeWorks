import numpy as np
from scipy.stats import uniform
import matplotlib.pyplot as plt

def calculate_distances(n, T=1):
    # Генерируем точки на отрезке [0,T]
    points1 = uniform.rvs(loc=0, scale=T, size=n)
    points2 = uniform.rvs(loc=0, scale=T, size=n)
    
    # Вычисляем расстояния
    distances = np.abs(points2 - points1)
    return distances

def theoretical_moments(T=1, k=1):
    # Вычисляет теоретические моменты k-го порядка
    return 2 * T**k / ((k+1)*(k+2))

# Параметры моделирования
T = 1
sample_sizes = np.logspace(2, 5, 50, dtype=int)  # от 100 до 100000
means = []
variances = []
moments3 = []
moments4 = []

# Теоретические значения
theoretical_mean = T/3
theoretical_var = T**2/18
theoretical_moment3 = theoretical_moments(T, 3)
theoretical_moment4 = theoretical_moments(T, 4)

# Вычисляем статистики для разных размеров выборки
for size in sample_sizes:
    distances = calculate_distances(size, T)
    means.append(np.mean(distances))
    variances.append(np.var(distances))
    moments3.append(np.mean(distances**3))
    moments4.append(np.mean(distances**4))

# График зависимости среднего от числа экспериментов
plt.figure(figsize=(15, 10))

# График среднего
plt.subplot(2, 2, 1)
plt.semilogx(sample_sizes, means, 'b-', label='Эмпирическое среднее')
plt.axhline(y=theoretical_mean, color='r', linestyle='--', 
            label=f'Теоретическое среднее = {theoretical_mean:.4f}')
plt.grid(True)
plt.xlabel('Число экспериментов')
plt.ylabel('Среднее расстояние')
plt.title('Среднее значение')
plt.legend()

# График дисперсии
plt.subplot(2, 2, 2)
plt.semilogx(sample_sizes, variances, 'g-', label='Эмпирическая дисперсия')
plt.axhline(y=theoretical_var, color='r', linestyle='--',
            label=f'Теоретическая дисперсия = {theoretical_var:.4f}')
plt.grid(True)
plt.xlabel('Число экспериментов')
plt.ylabel('Дисперсия')
plt.title('Дисперсия')
plt.legend()

# Гистограмма распределения расстояний
plt.subplot(2, 2, 3)
distances = calculate_distances(100000, T)
plt.hist(distances, bins=50, density=True, alpha=0.7, label='Эмпирическое распределение')

# Теоретическая плотность
x = np.linspace(0, T, 1000)
pdf = 2*(T-x)/T**2  # Теоретическая плотность
plt.plot(x, pdf, 'r-', label='Теоретическая плотность')
plt.xlabel('Расстояние')
plt.ylabel('Плотность')
plt.title('Распределение расстояний')
plt.legend()
plt.grid(True)

# График функции распределения
plt.subplot(2, 2, 4)
x = np.linspace(-0.2*T, 1.2*T, 1000)
cdf = np.where(x < 0, 0, 
               np.where(x > T, 1, 
                       (2*T-x)*x/T**2))
plt.plot(x, cdf, 'r-', label='Теоретическая F(x)')
plt.plot(np.sort(distances), np.linspace(0, 1, len(distances)), 
         'b-', alpha=0.5, label='Эмпирическая F(x)')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.title('Функция распределения')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

print(f"Теоретические значения для T={T}:")
print(f"E(γ) = {theoretical_mean:.4f}")
print(f"Var(γ) = {theoretical_var:.4f}")
print(f"ν₃(γ) = {theoretical_moment3:.4f}")
print(f"ν₄(γ) = {theoretical_moment4:.4f}")

print("\nЭмпирические значения (100000 точек):")
print(f"E(γ) ≈ {np.mean(distances):.4f}")
print(f"Var(γ) ≈ {np.var(distances):.4f}")
print(f"ν₃(γ) ≈ {np.mean(distances**3):.4f}")
print(f"ν₄(γ) ≈ {np.mean(distances**4):.4f}") 