# #На вход программе подается последовательность целых чисел делящихся на
# 7
# 7, каждое число на отдельной строке. Концом последовательности является любое число, не делящееся на
# 7
# 7 (само это число в последовательность не входит, лишь символизируя её конец). Напишите программу, которая выводит члены данной последовательности.

num = int(input())
while num % 7 == 0:
    print(num)
    num = int(input())