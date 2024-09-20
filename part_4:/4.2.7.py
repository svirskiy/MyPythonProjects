column1 = int(input())
line1 = int(input())
column2 = int(input())
line2 = int(input())
if column2 == column1 and line2 != line1 or column2 != column1 and line2 == line1:
    print("YES")
else:
    print("NO")