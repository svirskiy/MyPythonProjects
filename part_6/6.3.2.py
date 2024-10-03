#Напишите программу, определяющую площадь круга и длину окружности по заданному радиусу

R = float(input())
import math
print(math.pi * R**2)
print(2 * math.pi * R)