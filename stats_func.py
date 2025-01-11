"""Программа для расчета статистики"""

import numpy as np

# Создаем массив чисел

data=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

#Вычисляем среднее арифметическое значение
mean_value=np.mean(data)

#Находим медиану

median_value = np.median(data)

#Вычисляем стандартное отклонение
std_dev=np.std(data)

#Печатаем

print('Mean:', mean_value)
print('Median:', median_value)
print('Standart deviation:', std_dev)
