# Дано натуральное число. Напишите программу, которая выводит его цифры в столбик в обратном порядке.
#
# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести цифры введенного числа в столбик в обратном порядке.


num = int(input())
while num != 0:
    last_digit = num % 10
    print(last_digit)
    num = num // 10