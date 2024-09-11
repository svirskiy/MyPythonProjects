num = int(input())
dig1 = num // 1000
dig2 = (num // 100) % 10
dig3 = (num // 10) % 10
dig4 = num % 10
sum1_4 = dig1 + dig4
dif2_3 = dig2 - dig3
if sum1_4 == dif2_3:
    print("YES")
else:
    print("NO")