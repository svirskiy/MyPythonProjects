#На вход программе подается натуральное число
#Напишите программу, которая печатает звездный прямоугольник размерами n×19
#На вход программе подаётся натуральное число n∈[1;20] — высота звездного прямоугольника.

n = int(input())
for n1 in range(n):
    print(19 * "*")
