number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
if number_1 < 0 and number_2 < 0 and number_3 < 0:
    print("0")
else:
    if number_1 >= 0 and number_2 >= 0 and number_3 >= 0:
        print(number_1 + number_2 + number_3)
    else:
        if number_1 >= 0 and number_2 >= 0 and number_3 < 0:
            print(number_1 + number_2)
        else:
            if number_1 >= 0 and number_3 >= 0 and number_2 <0:
                print(number_1 + number_3)
            else:
                if number_2 >= 0 and number_3 >= 0 and number_1 < 0:
                    print(number_2 + number_3)
                else:
                    if number_1 >= 0 and number_2 < 0 and number_3 < 0:
                        print(number_1)
                    else:
                        if number_2 >= 0 and number_1 < 0 and number_3 < 0:
                            print(number_2)
                        else:
                            if number_3 >= 0 and number_1 < 0 and number_2 < 0:
                                print(number_3)


