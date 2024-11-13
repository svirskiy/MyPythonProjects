# Дано натуральное число. Напишите программу, которая вычисляет:
#
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.
# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести значения указанных величин в указанном порядке.

num = int(input())
sum_digits = 0
count_digits = 0
product_digits = 1
last_digit = num % 10
while num > 0:
    digit = num % 10
    sum_digits += digit
    count_digits += 1
    product_digits *= digit
    first_digit = num
    num //= 10
average_digits = sum_digits / count_digits
sum_first_last = first_digit + last_digit
print(sum_digits, count_digits, product_digits, average_digits, first_digit, sum_first_last, sep = "\n")