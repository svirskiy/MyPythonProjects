x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 - x2 == y1 - y2) or (x1 - x2 == y2 - y1):
    print("YES")
else:
    print("NO")