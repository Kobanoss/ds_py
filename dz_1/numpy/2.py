"""
Вычислите массив a_centered, отняв от значений массива “а” средние значения соответствующих признаков,
    содержащиеся в массиве mean_a.
Вычисление должно производиться в одно действие.
Получившийся массив должен иметь размер 5x2.
"""
import numpy as np

# Вывод с предыдущего номера
a = np.array([[1, 2, 3, 3, 1], [6, 8, 11, 10, 7]])
mean_a = list(map(float, (a.mean(1))))
print(f'Input array: \n{a}')
print(f'Arithmetical mean: {mean_a}\n')
# Вывод с предыдущего номера

a_centered = np.array([[round(i - mean_a[j], 2) for i in a[j] ]for j in range(len(mean_a))]) # Само вычисление

print(f'Centered array in numpy form: \n{a_centered}\n')
print(f'Centered array in normal form: \n{[list(map(float,a_centered[i])) for i in range(len(a_centered))]}\n')