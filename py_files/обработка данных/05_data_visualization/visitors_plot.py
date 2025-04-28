import numpy as np
import matplotlib.pyplot as plt

# Загрузка данных
visitors = np.load('visitors.npy')
days = np.arange(1, 101)  # Создаем массив дней от 1 до 100

# Создаем фигуру с двумя подграфиками
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Первый график (линейный масштаб)
ax1.plot(days, visitors, 'b-')
ax1.axhline(y=100, color='r', linestyle='-')
ax1.set_xlabel('Количество дней с момента акции')
ax1.set_ylabel('Число посетителей')
ax1.set_title('$y(x)=\lambda e^{-\lambda x}$')

# Второй график (логарифмический масштаб)
ax2.plot(days, visitors, 'b-')
ax2.axhline(y=100, color='r', linestyle='-')
ax2.set_xlabel('Количество дней с момента акции')
ax2.set_ylabel('Число посетителей')
ax2.set_yscale('log')
ax2.set_title('$y(x)=\lambda e^{-\lambda x}$')

# Общий заголовок
plt.suptitle('Изменение количества пользователей в линейном и логарифмическом масштабе')

# Добавляем подписи к горизонтальным линиям
ax1.text(1, 100, '$y(x)=100$', color='r', va='bottom')
ax2.text(1, 100, '$y(x)=100$', color='r', va='bottom')

# Настраиваем отступы
plt.tight_layout()

# Сохраняем график
plt.savefig('visitors_plot.png')
plt.show() 