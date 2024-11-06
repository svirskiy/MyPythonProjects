num = int(input())
min_digit = 9
max_digit = 0
while num != 0:
    last_digit = num % 10
    if last_digit > max_digit:
        max_digit = last_digit
    if last_digit < min_digit:
        min_digit = last_digit
    num = num // 10
print("The maximum number is equal to", max_digit)
print("The minimum number is equal to", min_digit)