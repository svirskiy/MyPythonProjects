import math
n = int(input())
sum_series = 0
for i in range(1, n + 1):
    sum_series += 1 / i
print(sum_series - math.log(n))