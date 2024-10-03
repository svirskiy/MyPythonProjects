#Напишите программу, которая принимает на вход действительное число и вычисляет по нему значение:

x = float(input())
import math
print(math.floor(x) + math.ceil(x))