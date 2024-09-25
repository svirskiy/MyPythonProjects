side1, side2, side3 = int(input()), int(input()), int(input())
if side1 == side2 == side3:
    print("Equilateral")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles")
else:
    print("Versatile")