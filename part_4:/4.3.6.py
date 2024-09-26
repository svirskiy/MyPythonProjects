first_number = int(input())
second_number = int(input())
string = input()
if string == "*":
    print(first_number * second_number)
elif string == "/" and second_number != 0:
    print(first_number / second_number)
elif string == "+":
    print(first_number + second_number)
elif string == "-":
    print(first_number - second_number)
elif string == "/" and second_number == 0:
    print("You can't divide by zero!")
else:
    print("Invalid operation")