
__author__ = 'Ваши Ф.И.О.'

import math
# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True

# Вопрос: Чему была равна переменная a,
# если точно известно, что её значение не изменялось?

# Подсказка: это значение точно есть ;)

# значение бсконечности при любых математических операциях = бесконечности,
# Ответ: infinity

a = math.inf
print(a == a**2)
print(a == a*2)
print(a > 999999)
