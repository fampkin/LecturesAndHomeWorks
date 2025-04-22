import numpy as np
from scipy import integrate
from scipy.optimize import root_scalar

def density(x, C):
    """Функция плотности распределения"""
    return C * (1 + 3*x**0.5 + 6*x**0.7 + 9*x**0.9)**1.5

def find_C():
    """Находит константу C из условия, что интеграл плотности равен 1"""
    def integral_eq(C):
        result, _ = integrate.quad(density, 4, 7, args=(C,))
        return result - 1
    
    # Ищем C методом бисекции
    C = root_scalar(integral_eq, bracket=[0.0001, 0.001], method='bisect').root
    return C

def expected_value(C):
    """Вычисляет математическое ожидание"""
    def integrand(x):
        return x * density(x, C)
    result, _ = integrate.quad(integrand, 4, 7)
    return result

def variance(C, mean):
    """Вычисляет дисперсию"""
    def integrand(x):
        return (x - mean)**2 * density(x, C)
    result, _ = integrate.quad(integrand, 4, 7)
    return result

def find_quantile(C, p):
    """Находит квантиль уровня p"""
    def cdf_minus_p(x):
        result, _ = integrate.quad(lambda t: density(t, C), 4, x)
        return result - p
    
    # Ищем квантиль методом бисекции
    quantile = root_scalar(cdf_minus_p, bracket=[4, 7], method='bisect').root
    return quantile

# Находим константу C
C = find_C()
print(f"1) Константа C = {C:.6f}")

# Вычисляем математическое ожидание
mean = expected_value(C)
print(f"2) Математическое ожидание E(X) = {mean:.4f}")

# Вычисляем стандартное отклонение
std = np.sqrt(variance(C, mean))
print(f"3) Стандартное отклонение σ_X = {std:.4f}")

# Находим квантиль уровня 0.8
quantile = find_quantile(C, 0.8)
print(f"4) Квантиль уровня 0.8 = {quantile:.4f}")

# Визуализация
import matplotlib.pyplot as plt

x = np.linspace(4, 7, 1000)
y = [density(xi, C) for xi in x]

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(x, y, 'b-', label='Плотность распределения')
plt.axvline(x=mean, color='r', linestyle='--', label=f'E(X) = {mean:.4f}')
plt.axvline(x=quantile, color='g', linestyle='--', label=f'Квантиль 0.8 = {quantile:.4f}')
plt.fill_between(x[x <= quantile], y[x <= quantile], alpha=0.3)
plt.grid(True)
plt.legend()
plt.title('Плотность распределения')
plt.xlabel('x')
plt.ylabel('f(x)')

# График функции распределения
plt.subplot(1, 2, 2)
cdf_values = []
for xi in x:
    result, _ = integrate.quad(lambda t: density(t, C), 4, xi)
    cdf_values.append(result)

plt.plot(x, cdf_values, 'b-', label='Функция распределения')
plt.axhline(y=0.8, color='g', linestyle='--', label='Уровень 0.8')
plt.axvline(x=quantile, color='g', linestyle='--')
plt.grid(True)
plt.legend()
plt.title('Функция распределения')
plt.xlabel('x')
plt.ylabel('F(x)')

plt.tight_layout()
plt.show()

# Проверка корректности результатов
print("\nПроверка:")
print(f"Интеграл плотности = {integrate.quad(density, 4, 7, args=(C,))[0]:.10f} ≈ 1")
print(f"F(квантиль) = {integrate.quad(lambda x: density(x, C), 4, quantile)[0]:.4f} ≈ 0.8") 