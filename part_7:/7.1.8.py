m, p, n = int(input()), int(input()), int(input())
for i in range(n):
    print(i + 1, m)
    m = m * (1 + p/100)