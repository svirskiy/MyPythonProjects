# Дано натуральное число
# 𝑛
# n. Напишите программу, которая печатает численный треугольник в соответствии с примером:
#
# 1
# 22
# 333
# 4444
# 55555

n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        print(i, end='')
    print()