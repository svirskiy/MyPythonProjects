number = int(input())
last_digit = number % 10
is_ordered = True
number //= 10
while number > 0:
    current_digit = number % 10
    if current_digit < last_digit:
        is_ordered = False

    last_digit = current_digit
    number //= 10
if is_ordered:
    print("YES")
else:
    print("NO")
