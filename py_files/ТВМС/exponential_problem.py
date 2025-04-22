import numpy as np
from scipy.stats import expon

# Параметры
lambda_param = 4/3
size = 1000000  # Размер выборки для симуляции

# Генерируем случайные числа из показательного распределения
X = np.random.exponential(scale=1/lambda_param, size=size)

# Проверяем дисперсию 10 - 4X
var_transformed = np.var(10 - 4*X)
print(f"Проверка дисперсии 10 - 4X: {var_transformed:.4f} ≈ 9")

# Вычисляем E[(X-9)(10-X)]
expectation = np.mean((X-9)*(10-X))
print(f"E[(X-9)(10-X)] ≈ {expectation:.4f} ≈ -78")

# Теоретические значения
E_X = 1/lambda_param
E_X2 = 2/(lambda_param**2)
theoretical = -E_X2 + 19*E_X - 90
print(f"\nТеоретическое значение: {theoretical:.4f}")

# Проверка свойств показательного распределения
print(f"\nПроверка свойств:")
print(f"E[X] (теор.): {E_X:.4f}, (эмпир.): {np.mean(X):.4f}")
print(f"Var[X] (теор.): {1/lambda_param**2:.4f}, (эмпир.): {np.var(X):.4f}") 