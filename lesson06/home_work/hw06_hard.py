# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers.csv.txt").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of.csv.txt"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла


class Worker:

	def __init__(self, s):
		name, surname, salary, position, norm = s.split()
		self.fullname = name + ' ' + surname
		self.salary = float(salary)
		self.position = position
		self.norm = float(norm)

	def calc_salary(self):
		hours = work_hours.get(self.fullname, None)
		if hours is None:
			return None
		if hours >= self.norm:
			real_salary = self.salary * (1 + 2 * (hours / self.norm - 1))
		else:
			real_salary = self.salary * (hours / self.norm)
		return round(real_salary, 2)


with open('data/workers.txt', 'r', encoding='utf-8') as f:
	s_list = f.readlines()

with open('data/hours_of.txt', 'r', encoding='utf-8') as f:
	h_list = f.readlines()


def parse(x):
	name, surname, hours = x.split()
	return name + ' ' + surname, float(hours)


workers = list(map(Worker, s_list[1:]))
work_hours = {key: value for key, value in map(parse, h_list[1:])}

real_salaries = {worker.fullname: worker.calc_salary() for worker in workers}

print(real_salaries)


import pandas


class PandaSalary:
	def __init__(self, base1_path, base2_path):
		with open(base1_path, 'r', encoding='utf-8') as b1:
			l1 = b1.readlines()
			self.file1 = self.__file_to_csv(l1)
		with open(base2_path, 'r', encoding='utf-8') as b2:
			l2 = b2.readlines()
			self.file2 = l2

	def __file_to_csv(self, file):
		new_lst = []
		for i in file:
			new_lst.append(' '.join(i.split()))
		return new_lst

p = PandaSalary('data/workers.txt', 'data/hours_of.txt')
print(p.file1)



