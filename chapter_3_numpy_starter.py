import numpy as np

a = np.array([0, 1, 2, 3])
b = np.array([4, 5, 6, 7])
c = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
d = np.zeros((2, 4))  # матрица 2 на 4 заполненная нулями
e = np.random.rand(2, 5)  # матрица 2 на 5 заполненная случайными числами от 0 до 1

print(a)
print(b)
print(c)
print(d)
print(e)

print("\nOPERATIONS:")
print(a * 10)
print(c * 2)
print(a * b)
print(a * b * 10)
print(a * c)

print("\n")
a = np.zeros((2, 4))
b = np.zeros((4, 3))
c = a.dot(b)
print(c.shape)

a = np.zeros((2, 4))
b = np.zeros((3, 4)).T
c = a.dot(b)
print(c.shape)

a = np.array([[1, 3], [2, 3]])
b = np.array([[4, 5], [9, 1]])
c = a.dot(b)  # [[31, 8], [35, 13]]
print(c)
