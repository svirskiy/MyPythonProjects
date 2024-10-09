#Даны названия трёх городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
#Формат входных данных
#На вход программе подаются названия трёх городов, каждое на отдельной строке

city1 = input()
city2 = input()
city3 = input()
if len(city1) <= len(city2) and len(city1) <= len(city3):
    shortest_city = city1
elif len(city2) <= len(city1) and len(city2) <= len(city3):
    shortest_city = city2
else:
    shortest_city = city3
if len(city1) >= len(city2) and len(city1) >= len(city3):
    longest_city = city1
elif len(city2) >= len(city1) and len(city2) >= len(city3):
    longest_city = city2
else:
    longest_city = city3
print(shortest_city)
print(longest_city)