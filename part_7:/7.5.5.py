n = int(input())
while n >= 100:
    n //= 10
second_digit = n % 10
print(second_digit)