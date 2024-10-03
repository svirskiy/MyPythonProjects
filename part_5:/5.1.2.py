first_cell_a, first_cell_b, second_cell_a, second_cell_b = int(input()), int(input()), int(input()), int(input())
if 1 <= first_cell_a <= 8 and 1 <= first_cell_b <= 8 and 1 <= second_cell_a <= 8 and 1 <= second_cell_b <= 8:
    if (first_cell_a + first_cell_b) % 2 == (second_cell_a + second_cell_b) % 2:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
