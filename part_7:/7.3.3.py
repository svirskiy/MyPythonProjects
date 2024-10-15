import math
n = int(input())
sum_series = 0
for i in range(1, n + 1):
    sum_series += 1 / i
log_n = math.log(n)
result = sum_series - log_n
print(result)