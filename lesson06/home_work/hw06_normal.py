# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

import itertools


def intersection(lst1, lst2):
	return list(set(lst1) & set(lst2))


class School:
	def __init__(self, classes: list, teachers: list):
		self._classes = classes
		self._teachers = teachers

	def classes(self):
		return self._classes

	def class_list(self):
		return [cl.name for cl in self._classes]

	def teachers(self):
		return self._teachers

	def students_for_class(self, class_name):
		classes = filter(lambda x: x.name == class_name, self._classes)
		students = itertools.chain.from_iterable( [cl.students for cl in classes])
		return [st.name() for st in students]

	def teachers_for_class(self, class_name):
		cl = self._find_class_by_name(class_name)
		teachers = [t.name() for t in self._teachers if cl in t.classes()]
		return teachers

	def student_courses(self, student_name):
		student = self._find_student_by_name(student_name)
		student_classes = set([cl for cl in self._classes if student in cl.students])
		student_teachers = []
		for teacher in self._teachers:
			if intersection(student_classes, teacher.classes()):
				student_teachers.append(teacher)
		lessons_list = [ t.course() for t in student_teachers ]
		return lessons_list

	def student_parents(self, student_name):
		student = self._find_student_by_name(student_name)
		return student.parent_names()

	def _find_class_by_name(self, name):
		cl = [cl for cl in self._classes if cl.name == name]
		return cl[0]

	def _find_student_by_name(self, student_name):
		students = itertools.chain.from_iterable( [cl.students for cl in self._classes])
		student = list(filter(lambda x: x.name() == student_name, students))[0]
		return student


class SchoolClass:
	def __init__(self, name, *students):
		self.name = name
		self.students = students

	def __str__(self):
		return "%s" % self.name


class Person(object):
	def __init__(self, name):
		self._name = name

	def name(self):
		return self._name


class Teacher(Person):
	def __init__(self, name, course, classes):
		super(Teacher, self).__init__(name)
		self._course = course
		self._classes = classes

	def classes(self):
		return self._classes

	def course(self):
		return self._course


class Student(Person):
	def __init__(self, name, father, mother):
		super(Student, self).__init__(name)
		self._father = father
		self._mother = mother

	def parent_names(self):
		return [self._father.name(), self._mother.name()]

	def __str__(self):
		return "%s" % self.name


