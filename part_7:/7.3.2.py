# На вход программе подается натуральное число
# 𝑛
# n, а затем
# 𝑛
# n целых чисел, каждое на отдельной строке. Напишите программу, которая подсчитывает сумму введенных чисел (не включая само число
# 𝑛
# n).

n = int(input())
total = 0
for i in range(n):
    num = int(input())
    total += num
print(total)