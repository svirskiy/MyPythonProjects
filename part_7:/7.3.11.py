# Напишите программу, которая считывает натуральное число
# 𝑛
# n и выводит первые
# 𝑛
# n чисел последовательности Фибоначчи.

n = int(input())
first_num, second_num = 1, 1
if n >= 1:
    print(first_num, end=" ")
if n >= 2:
    print(second_num, end=" ")
for i in range(3, n + 1):
    next_num = first_num + second_num
    print(next_num, end=" ")
    first_num, second_num = second_num, next_num