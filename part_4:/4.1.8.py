age = int(input())
if age <= 13:
    print("Childhood")
else:
    if age <= 24:
        print("Youth")
    else:
        if age <= 59:
            print("Adulthood")
        else:
            print("Oldness")

