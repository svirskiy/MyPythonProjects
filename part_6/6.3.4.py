#Напишите программу, вычисляющую значение тригонометрического выражения

x = float(input())
import math
r = math.radians(x)
print(math.sin(r) + math.cos(r) + math.tan(r)**2)