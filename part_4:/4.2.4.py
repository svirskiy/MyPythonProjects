pretty_number = int(input())
if (pretty_number % 7 == 0 or pretty_number % 17 == 0) and 1000 <= pretty_number <= 9999:
    print("YES")
else:
    print("NO")