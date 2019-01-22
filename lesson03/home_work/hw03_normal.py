# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
import math


def fibonacci(n, m):
	fib = []
	for i in range(n, m+1):
		nfib = round((((1 + math.sqrt(5)) / 2) ** i + ((1 - math.sqrt(5)) / 2) ** i) / math.sqrt(5))
		fib.append(nfib)
	return fib


print(fibonacci(5, 12))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(orig):
	n = 1
	while n < len(orig):
		for i in range(len(orig) - n):
			if orig[i] > orig[i + 1]:
				orig[i], orig[i + 1] = orig[i + 1], orig[i]
		n += 1
	return orig


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def custom_flt(func, iter):
	if func is None:
		return (item for item in iter if item)
	else:
		return (item for item in iter if func(item))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def paral(a, b, c, d):

	ab = math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
	cb = math.sqrt((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2)
	cd = math.sqrt((d[0] - c[0]) ** 2 + (d[1] - c[1]) ** 2)
	ad = math.sqrt((d[0] - a[0]) ** 2 + (d[1] - a[1]) ** 2)

	rm = ab == cd and cb == ad
	h2 = ((a[0] + c[0]) / 2, (a[1] + c[1]) / 2)
	h1 = ((b[0] + d[0]) / 2, (b[1] + d[1]) / 2)

	if rm and h1 == h2:
		return 'Параллерограмм'
	else:
		'Введенные точки параллеррограммом не вляются'
