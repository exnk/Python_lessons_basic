# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()


def task1(lst):
	for elm in lst:
		print('{}.{:>20}'.format(lst.index(elm)+1, elm))


L = []
while True:
	fruit = input('Введине название фрукта или для выхода нажмите Enter\n')
	print(fruit)
	if fruit == "":
		break
	else:
		L.append(fruit)
print(len(L))
try:
	assert len(L) > 0
except ValueError:
	print('Вы не ввели ни одного элемента')
else:
	task1(L)


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
list1 = input('Введите значения первого списка через пробел')
list1 = list1.split(' ')

list2 = input('Введите значения второго списка через пробел')
list2 = list2.split(' ')

res = set(list1).difference(set(list2))
print(res)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.


def task3(lst):
	res_lst = []
	for elm in lst:
		if elm % 2 == 0:
			res_lst.append(elm/4)
		else:
			res_lst.append(elm*2)
	return res_lst


lst = input('Введите значения списка через пробел')
try:
	lst = map(int, lst.split(' '))
except ValueError:
	print("Не все значения списка являются числами!")
else:
	print(task3(lst))
