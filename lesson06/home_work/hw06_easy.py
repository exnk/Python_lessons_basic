# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


class Triangle:

	def __init__(self, a: list, b: list, c: list):
		self.a = a
		self.b = b
		self.c = c
		self.AB = round(math.sqrt(int(math.fabs((pow((b[1] - a[1]),2)) + (pow((b[0] - a[0]), 2))))), 2)
		self.BC = round(math.sqrt(int(math.fabs((pow((c[1] - b[1]),2)) + (pow((c[0] - b[0]), 2))))), 2)
		self.CA = round(math.sqrt(int(math.fabs((pow((a[1] - c[1]),2)) + (pow((a[0] - c[0]), 2))))), 2)

	def square(self):

		return self.AB*self.BC*self.CA

	def perimeter(self):
		return self.AB + self.BC + self.CA

	def high(self):
		p = (self.AB + self.BC + self.CA)/2
		ha = 2*math.sqrt(p*(p-self.AB)*(p-self.BC)*(p-self.CA))/self.AB
		hb = 2*math.sqrt(p*(p-self.AB)*(p-self.BC)*(p-self.CA))/self.BC
		hc = 2*math.sqrt(p*(p-self.AB)*(p-self.BC)*(p-self.CA))/self.CA
		return ''.join(['Высота на сторону А:{}\n'.format(ha),
						'Высота на сторону B:{}\n'.format(hb),
						'Высота на сторону C:{}\n'.format(hc)])


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapeze:

	def __init__(self, a: list, b: list, c: list, d: list):
		self.__get_information(a, b, c, d)
		self.AB = round(math.sqrt(int(math.fabs((pow((b[1] - a[1]), 2)) + (pow((b[0] - a[0]), 2))))), 2)
		self.BC = round(math.sqrt(int(math.fabs((pow((c[1] - b[1]), 2)) + (pow((c[0] - b[0]), 2))))), 2)
		self.CD = round(math.sqrt(int(math.fabs((pow((d[1] - c[1]), 2)) + (pow((d[0] - c[0]), 2))))), 2)
		self.DA = round(math.sqrt(int(math.fabs((pow((a[1] - d[1]), 2)) + (pow((a[0] - d[0]), 2))))), 2)

	@staticmethod
	def __get_information(a, b, c, d):
		try:
			assert (a[1] == b[1]) and (c[1] == d[1])
		except AssertionError:
			print('Четырехугольник')
		else:
			print('Трапеция')

	def sides(self):
		return 'Сторона AB:{}\nСторона BC:{}\nСторона CD:{}\nСторона DA:{}\n'.format(self.AB, self.BC, self.CD, self.DA)

	def perimeter(self):
		return self.AB + self.BC + self.CD + self.DA

	def square(self):
		return ((self.AB+self.CD)/2) * \
			math.sqrt(pow(self.DA, 2) - pow((pow((self.CD-self.AB), 2) +
											pow(self.DA, 2) - pow(self.BC, 2))/2*(self.CD-self.AB), 2))
