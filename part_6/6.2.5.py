#Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет, можно ли из длин этих строк построить арифметическую прогрессию.
#Формат входных данных - На вход программе подаются три строки, каждая на отдельной строке.

str1 = input()
str2 = input()
str3 = input()
len1 = len(str1)
len2 = len(str2)
len3 = len(str3)
if (len1 + len3) == 2 * len2:
    print("YES")
elif (len1 + len2) == 2 * len3:
    print("YES")
elif (len2 + len3) == 2 * len1:
    print("YES")
else:
    print("NO")
