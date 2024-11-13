# Дано натуральное число
# 𝑛
# (
# 𝑛
# ≥
# 10
# )
# n(n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры и выводит текст в следующем формате:
#
# Максимальная цифра равна <максимальная цифра>
# Минимальная цифра равна <минимальная цифра>
# Формат входных данных
# На вход программе подаётся одно натуральное число
# 𝑛
# (
# 𝑛
# ≥
# 10
# )
# n(n≥10).
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.


num = int(input())
min_digit = 9
max_digit = 0
while num != 0:
    last_digit = num % 10
    if last_digit > max_digit:
        max_digit = last_digit
    if last_digit < min_digit:
        min_digit = last_digit
    num = num // 10
print("The maximum number is equal to", max_digit)
print("The minimum number is equal to", min_digit)