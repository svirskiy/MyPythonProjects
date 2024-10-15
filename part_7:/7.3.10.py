# Напишите программу, которая считывает последовательность из
# 10
# 10 целых чисел и определяет, является ли каждое из них чётным или нет.
#


flag = True
for _ in range(10):
    num = int(input())
    if num % 2 != 0:
        flag = False
if flag:
    print("YES")
else:
    print("NO")