# Дано натуральное число
# 𝑛
# (
# 𝑛
# >
# 9
# )
# n(n>9). Напишите программу, которая определяет его вторую (с начала) цифру.
#
# Формат входных данных
# На вход программе подается одно натуральное число, состоящее как минимум из двух цифр.
#
# Формат выходных данных
# Программа должна вывести его вторую (с начала) цифру.

n = int(input())
while n >= 100:
    n //= 10
second_digit = n % 10
print(second_digit)