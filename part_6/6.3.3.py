#среднее арифметическое чисел
#среднее геометрическое чисел
#среднее гармоническое чисел
#среднее квадратичное чисел

import math
a = float(input())
b = float(input())
print((a + b) / 2)
print(math.sqrt(a * b))
print((2 * a * b) / (a + b))
print(math.sqrt((a**2 + b**2) / 2))