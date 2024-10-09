#Напишите программу, которая принимает на вход действительное число и вычисляет по нему значение:

import math
x = float(input())
print(math.floor(x) + math.ceil(x))