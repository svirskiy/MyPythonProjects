start, speed, days = int(input()), int(input()), int(input())
for i in range(days):
    print(i + 1, start)
    start = start * (1 + speed/100)