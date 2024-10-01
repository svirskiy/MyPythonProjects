number = int(input())
first_digit = number // 100
middle_digit = (number // 10) % 10
last_digit = number % 10
minimum_digit = min(first_digit, middle_digit, last_digit)
maximum_digit = max(first_digit, middle_digit, last_digit)
middle_digit = first_digit + middle_digit + last_digit - maximum_digit - minimum_digit
if maximum_digit - minimum_digit == middle_digit:
    print("The number is interesting")
else:
    print("The number is not interesting")