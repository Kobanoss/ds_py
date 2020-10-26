"""
Найдите скалярное произведение столбцов массива a_centered.
В результате должна получиться величина a_centered_sp.
Затем поделите a_centered_sp на N-1, где N - число наблюдений.
"""
import numpy as np

# Вывод с предыдущего номера
a = np.array([[1, 2, 3, 3, 1], [6, 8, 11, 10, 7]])
mean_a = list(map(float, (a.mean(1))))
a_centered = np.array([[round(i - mean_a[j], 2) for i in a[j] ]for j in range(len(mean_a))])

print(f'Input array: \n{a}')
print(f'Arithmetical mean: {mean_a}\n')
print(f'Centered array in normal form: \n{[list(map(float,a_centered[i])) for i in range(len(a_centered))]}\n')
# Вывод с предыдущего номера


a_centered_sp = np.dot(a_centered[0], a_centered[1])
print(f'Scalar: {a_centered_sp}')

print(f'Scalar divide number of all obs(N): {a_centered_sp/(len(a_centered) * len(a_centered[0]))}')
