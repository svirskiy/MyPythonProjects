# На вход программе подается последовательность целых чисел от
# 1
# 1 до
# 5
# 5, характеризующее оценку ученика, каждое число на отдельной строке. Концом последовательности является любое неположительное число либо число, большее
# 5
# 5. Напишите программу, которая выводит количество пятерок.

rate = int(input())
sum = 0
while 0 < rate < 6:
    if rate == 5:
        sum += 1
    rate = int(input())
print(sum)