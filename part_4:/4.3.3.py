first_number = int(input())
second_number = int(input())
third_number = int(input())
if third_number > first_number > second_number or second_number > first_number > third_number:
    print(first_number)
elif first_number > second_number > third_number or third_number > second_number > first_number:
    print(second_number)
elif second_number > third_number > first_number or first_number > third_number > second_number:
    print(third_number)