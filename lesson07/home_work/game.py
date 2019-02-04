import random
import copy


class Ticker:

	def __init__(self):
		self.__card_lst = random.sample(range(1, 91), 15)
		self.ticker = self.ticker_generator(self.__card_lst)

	@staticmethod
	def ticker_generator(lst):

		first_line = []
		second_line = []
		third_line = []
		num_lst = copy.deepcopy(lst)
		for i in range(0, 5):
			num = str(num_lst.pop(num_lst.index(random.choice(num_lst))))
			first_line.append(num if len(num) == 2 else '*'+num)
		for i in range(0, 5):
			num = str (num_lst.pop(num_lst.index (random.choice (num_lst))))
			second_line.append(num if len(num) == 2 else '*'+num)
		for i in range(0, 5):
			num = str (num_lst.pop(num_lst.index (random.choice (num_lst))))
			third_line.append(num if len(num) == 2 else '*'+num)

		ticker = '{}\n{}\n{}\n{}\n{}'.format(
			'{}'.format('-'*26),
			'{0[0]:>2} {0[1]:<10} {0[2]:<5} {0[3]} {0[4]}'.format(first_line),
			'{0[0]:>4} {0[1]:<6} {0[2]:<4} {0[3]:<4} {0[4]} '.format(second_line),
			'{0[0]} {0[1]:<5} {0[2]:<5} {0[3]:<5} {0[4]} '.format(third_line),
			'{}'.format('-'*26)
		)

		return ticker

	def replacer(self, num):
		if int(num) in self.__card_lst:
			print('Цифра {} находится в билете!\nВычеркиваем!')
			self.__card_lst.pop(self.__card_lst.index(int(num)))
			if len(str(num)) == 1:
				self.ticker = self.ticker.replace('*{}'.format(num), '--')
			else:
				self.ticker = self.ticker.replace(str(num), '--')

			print('Ваша карточка {}'.format(self.ticker))
			return True
		else:
			return False

	def comp_replacer(self, num):
		if int(num) in self.__card_lst:
			print('Цифра {} находится в билете!\nВычеркиваем!')
			self.__card_lst.pop(self.__card_lst.index(int(num)))
			if len(str(num)) == 1:
				self.ticker = self.ticker.replace('*{}'.format(num), '--')
			else:
				self.ticker = self.ticker.replace(str(num), '--')

	def len_lst(self):
		return len(self.__card_lst)

	def card(self):
		return self.__card_lst


class Generator:

	def __init__(self, count=90):
		self.list = self.list_gen(count)

	@staticmethod
	def list_gen(count):
		try:
			int(count)
		except ValueError:
			return 'Переданно не число!!!'
		else:
			return [x for x in range(1, count+1)]

	def choice(self):
		res = self.list.pop(self.list.index(random.choice(self.list)))
		print('Выбранно число {}\nОсталось вариантов {}'.format(res, len(self.list)))
		return res


name = input('Введите пожалуйста свое Имя ')
print("Добро пожаловать {}".format(name))

player_ticker = Ticker()
compukter = Ticker()
g = Generator()
answers = ['да', "+", "yes", 'true', 'yup', 'ага']

res = True
while True:
	print('Ваша карточка\n\n{}'.format(player_ticker.ticker))
	print('Карточка Компуктера\n\n{}'.format(compukter.ticker))

	c = g.choice()
	choise = input('Хотите зачеркнуть?')
	if choise in answers:
		res = player_ticker.replacer(c)
		print(res)
		if res == False:
			print('Сорян {} Вы проиграли :( :( :( :('.format(name))
			break
	elif c in player_ticker.card():
		print('Упс, невнимательны, число {} было в вашей карте\n Вы проиграли)))'.format(c))
		break
	compukter.comp_replacer(c)
	print(compukter.len_lst())
	if compukter.len_lst() == 0:
		print('Сорян, победил компуктер')
		break
	if player_ticker.len_lst() == 0:
		print('Вы выиграли о/')
		break
