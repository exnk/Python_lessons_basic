# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
from shutil import copy


def make_dir():

	for n in range(1, 10):
		os.mkdir(''.join([os.curdir, 'exist']), n)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def get_folders():
	return os.getcwd()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy_file():
	print(''.join([os.curdir, 'exist']))
	print(os.curdir)
	return copy(__file__, ''.join([os.curdir, ''.join(['copy', os.path.basename(__file__)])]))


copy_file()
