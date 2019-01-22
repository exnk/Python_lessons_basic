# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

from fractions import Fraction


def fract(string):
	"""Расчитывает только для 2ух дробей((("""
	string = str(string).split(' ')
	num1 = Fraction(*list(map(int, string[0].split('/'))))
	num2 = Fraction(*list(map(int, string[-1].split('/'))))
	if string[1] is '+':
		res = num1 + num2
	elif string[1] is '*':
		res = num1 * num2
	elif string[1] is '/':
		res = num1 / num2
	elif string[1] is '-':
		res = num1 - num2
	else:
		return 'В выражении отсутствует знак операции'
	print(res)
	if res > 1:
		res = str(res).split('/')
		main = int(res[0]) // int(res[1])
		sub = int(res[0]) % int(res[1])
		return '{} {}/{}'.format(main, sub, res[1])
	else:
		return res


print(fract('5/6 + 4/6'))


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers.txt").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of.txt"

with open('data/workers.txt', encoding='utf-8') as w:  # with для того чтоб файл после отработки закрывался автоматом
	with open('data/hours_of.txt', encoding='utf-8') as h:
		w_lines = [' '.join(line.split()) for line in w]
		h_lines = [' '.join(line.split()) for line in h]
		del h_lines[0]
		del w_lines[0]
		workers = dict()
		for elm in h_lines:  # создаем массив сотрудников
			e = elm.split(' ')
			worker = ' '.join([e[0], e[1]])
			for w in w_lines:
				if worker in w:
					w2 = w.split(' ')
					workers.update({worker: {'worked': int(e[-1]), 'price': int(w2[2]),
											'rate': int(w2[-1]), 'salary': None}})

		for worker in workers.keys():  # просчитываем зарплату
			if workers[worker]['worked'] > workers[worker]['rate']:
				conversion = workers[worker]['worked'] - workers[worker]['rate']
				h_salary = workers[worker]['price'] / workers[worker]['rate'] * 2
				workers[worker]['salary'] = round(h_salary*conversion + workers[worker]['price'], 2)
			else:
				conversion = workers[worker]['rate'] - workers[worker]['worked']
				h_salary = workers[worker]['price'] / workers[worker]['rate']
				workers[worker]['salary'] = round(workers[worker]['price'] - h_salary*conversion, 2)


for worker in workers.keys():
	print('Зарплата сотрудника {} составляет {}'.format(worker, workers[worker]['salary']), end='\n')


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

def fruit_sort(file_path):
	charset = list(map(chr, range(ord('А'), ord('Я')+1)))
	char_dict = dict.fromkeys(charset, [])
	with open(file_path, encoding='utf-8') as f:
		fruits = list(filter(None, [x.strip() for x in f if x]))
		for fruit in fruits:
			st = fruit[0].upper()
			dlist = char_dict[st]
			char_dict[st] = dlist + [fruit]

	for key in char_dict.keys():
		if len(char_dict[key]) == 0:
			pass
		else:
			with open('data/fruits/fruit_by_{}.txt'.format(key), 'w', encoding='utf-8') as f:
				f.write('\n'.join(char_dict[key]))

a = fruit_sort('data/fruits.txt')

