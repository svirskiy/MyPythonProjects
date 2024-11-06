number = int(input())
last_digit = number % 10
is_same = True
while number > 0:
    current_digit = number % 10
    if current_digit != last_digit:
        is_same = False

    number //= 10
if is_same:
    print("YES")
else:
    print("NO")