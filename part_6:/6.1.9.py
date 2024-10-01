number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
minimum_number = min(number_1, number_2, number_3)
maximum_number = max(number_1, number_2, number_3)
middle_number = number_1 + number_2 + number_3 - maximum_number - minimum_number
print(maximum_number)
print(middle_number)
print(minimum_number)