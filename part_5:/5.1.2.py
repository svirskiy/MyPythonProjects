first_cell_a = int(input())
first_cell_b = int(input())
second_cell_a = int(input())
second_cell_b = int(input())
if (first_cell_a + first_cell_b) % 2 == (second_cell_a + second_cell_b) % 2 and 1 <= first_cell_a <= 8 and 1 <= first_cell_b <= 8 and 1 <= second_cell_a <= 8 and 1 <= second_cell_b <= 8:
    print("YES")
else:
    print("NO")