#Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит информацию о ней в следующем формате:
#Футбольная команда <название футбольной команды> имеет длину <длина названия футбольной команды> символов

team = input()
long = len(team)
print("Football team", team, "has long", long, "symbols")