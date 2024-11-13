# Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
#
# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести «YES» если число состоит из одинаковых цифр и «NO» в противном случае.


number = int(input())
last_digit = number % 10
is_same = True
while number > 0:
    current_digit = number % 10
    if current_digit != last_digit:
        is_same = False

    number //= 10
if is_same:
    print("YES")
else:
    print("NO")