# На вход программе подается натуральное число
# 𝑛
# n. Напишите программу, которая вычисляет сумму всех его делителей.

total = 0
n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        total += i
print(total)