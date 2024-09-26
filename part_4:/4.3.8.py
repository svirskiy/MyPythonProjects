pocket = int(input())
if (1 <= pocket <= 10 and pocket % 2 == 0) or (19 <= pocket <= 28 and pocket % 2 == 0) or (11 <= pocket <= 18 and pocket % 2 == 1) or (29 <= pocket <= 36 and pocket % 2 == 1):
    print("black")
elif (1 <= pocket <= 10 and pocket % 2 == 1) or (19 <= pocket <= 28 and pocket % 2 == 1) or (11 <= pocket <= 18 and pocket % 2 == 0) or (29 <= pocket <= 36 and pocket % 2 == 0):
    print("red")
elif pocket == 0:
    print("green")
else:
    print("wrong input")