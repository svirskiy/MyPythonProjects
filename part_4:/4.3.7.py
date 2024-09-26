main_color1 = input()
main_color2 = input()
if main_color1 == "red":
    if main_color2 == "blue":
        print("purple")
    elif main_color2 == "yellow":
        print("orange")
    elif main_color2 == "red":
        print("red")
    else:
        print("error color")
elif main_color1 == "blue":
    if main_color2 == "red":
        print("purple")
    elif main_color2 == "yellow":
        print("green")
    elif main_color2 == "blue":
        print("blue")
    else:
        print("error color")
elif main_color1 == "yellow":
    if main_color2 == "red":
        print("orange")
    elif main_color2 == "blue":
        print("green")
    elif main_color2 == "yellow":
        print("yellow")
    else:
        print("error color")
else:
    print("error color")