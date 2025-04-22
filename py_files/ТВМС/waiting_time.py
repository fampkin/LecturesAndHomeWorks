import numpy as np
from scipy.stats import uniform
import matplotlib.pyplot as plt

def calculate_waiting_time(n, T=1):
    # Генерируем времена прихода
    time1 = uniform.rvs(loc=0, scale=T, size=n)
    time2 = uniform.rvs(loc=0, scale=T, size=n)
    
    # Вычисляем время ожидания (минимум из прямого и обратного времени)
    direct_wait = np.abs(time2 - time1)
    reverse_wait = T - direct_wait
    waiting_times = np.minimum(direct_wait, reverse_wait)
    return waiting_times

# Параметры моделирования
T = 1
sample_sizes = np.logspace(2, 5, 50, dtype=int)  # от 100 до 100000
means = []

# Теоретическое среднее время ожидания
theoretical_mean = T/6  # E(τ) = T/6

# Вычисляем средние значения для разных размеров выборки
for size in sample_sizes:
    waiting_times = calculate_waiting_time(size, T)
    means.append(np.mean(waiting_times))

# Создаем графики
plt.figure(figsize=(15, 5))

# График сходимости среднего
plt.subplot(1, 2, 1)
plt.semilogx(sample_sizes, means, 'b-', label='Эмпирическое среднее')
plt.axhline(y=theoretical_mean, color='r', linestyle='--', 
            label=f'Теоретическое среднее = {theoretical_mean:.4f}')
plt.grid(True)
plt.xlabel('Число экспериментов')
plt.ylabel('Среднее время ожидания')
plt.title('Сходимость среднего времени ожидания')
plt.legend()

# Гистограмма распределения времени ожидания
plt.subplot(1, 2, 2)
waiting_times = calculate_waiting_time(100000, T)
plt.hist(waiting_times, bins=50, density=True, alpha=0.7, 
         label='Эмпирическое распределение')

# Теоретическая плотность
x = np.linspace(0, T/2, 1000)
pdf = 4*(1-2*x/T)/T  # Теоретическая плотность
plt.plot(x, pdf, 'r-', label='Теоретическая плотность')
plt.xlabel('Время ожидания')
plt.ylabel('Плотность')
plt.title('Распределение времени ожидания')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Функция распределения
def cdf(x, T=1):
    if x < 0:
        return 0
    elif x > T/2:
        return 1
    else:
        return 4*x/T - 4*x**2/T**2

print(f"\nТеоретические значения для T={T}:")
print(f"E(τ) = {theoretical_mean:.4f}")
print(f"\nЭмпирические значения (100000 точек):")
print(f"E(τ) ≈ {np.mean(waiting_times):.4f}")

# Проверка функции распределения для нескольких значений
test_points = [0, T/4, T/2]
print("\nЗначения функции распределения:")
for x in test_points:
    print(f"F({x:.2f}) = {cdf(x):.4f}") 