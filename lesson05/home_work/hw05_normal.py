# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


import os


def change_dir(dir_name):

	pth = os.path.join(os.getcwd(), dir_name)
	try:
		os.chdir(pth)
		print('Успешно перешли в каталог {}'.format(os.getcwd()))
		return os.path.abspath(os.getcwd())
	except FileNotFoundError:
		print('Каталог задан не правильно или не существует')
		return None


def dir_lst(pth=None):
	"""
	:param pth: Путь к папке
	:return:
	"""
	if pth is None or pth == '':
		return os.listdir(os.getcwd())
	else:
		return os.listdir(pth)


def del_dir(directory):
	"""
	:param directory: Дирректория для удаления
	:return: Результат удаления
	"""
	try:
		os.rmdir(directory)
		assert directory not in os.listdir(os.getcwd())
		return 'Папка {} успешно удалена'.format(directory)
	except FileNotFoundError:
		return 'Путь не существует'
	except AssertionError:
		return 'Папка не удалена'


def make_dir(directory):
	"""
	:param directory: Директория которая будет создана
	:return: Итоге выполнения
	"""
	try:
		os.mkdir(directory)
		assert directory in os.listdir(os.getcwd())
		return 'Папка {} создалась успешно'.format(directory)
	except AssertionError:
		return 'Папка не создалась'


path = os.path.abspath(os.getcwd())
while True:
	action_dict = {'1': change_dir, '2': dir_lst, '3': make_dir, '4':del_dir}
	print("""1. Перейти в папку
			 2. Просмотреть содержимое текущей папки
			 3. Удалить папку
			 4. Создать папку
			 5. Выйти из программы""")
	choice = input('Введите цифру которую хотите использовать')
	if choice == '1':
		data = input('Введите данные для выполнения операции\n'
					'Подсказка по параметрам выбранной операции {}\n'.format (action_dict[choice].__doc__))
		action_dict[choice](data)
		path = os.path.abspath(os.getcwd())

	elif choice == '5':
		print('Пока Пока!')
		break

	else:
		data = input('Введите данные для выполнения операции\n'
					'Подсказка по параметрам выбранной операции {}\n'.format(action_dict[choice].__doc__))
		print(action_dict[choice](data))
