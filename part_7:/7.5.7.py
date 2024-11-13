# Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.
#
# Формат входных данных
# На вход программе подаётся одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести «YES», если последовательность его цифр при просмотре справа налево является упорядоченной по неубыванию, или «NO» в противном случае.
#
# number = int(input())
# last_digit = number % 10


is_ordered = True
number //= 10
while number > 0:
    current_digit = number % 10
    if current_digit < last_digit:
        is_ordered = False
        break
    last_digit = current_digit
    number //= 10
if is_ordered:
    print("YES")
else:
    print("NO")
