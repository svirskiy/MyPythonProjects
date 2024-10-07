#На вход программе подаётся натуральное число n. Напишите программу, которая для каждого из чисел от

n = int(input())
for i in range(n + 1):
    print("The square of the number", i, "equal",  i**2)