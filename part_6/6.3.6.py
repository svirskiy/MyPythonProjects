a = float(input())
b = float(input())
c = float(input())
import math
sqrt_part = b**2 - 4*a*c
if sqrt_part > 0:
    sqrt_part = math.sqrt(sqrt_part)
    x1 = (-b - sqrt_part) / (2*a)
    x2 = (-b + sqrt_part) / (2*a)
    print(min(x1, x2))
    print(max(x1, x2))
elif sqrt_part == 0:
    x = -b / (2*a)
    print(x)
else:
    print("No roots")