import random
import time

"""
Simulated Map
    1 = Wall, 
    2 = player, 
    3 = enemy, 
    4 = item
"""
TestField = [
    [1, 1, 1, 1, 1, 1],
    [1, 2, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 3, 1],
    [1, 0, 4, 0, 0, 1],
    [1, 1, 1, 1, 1, 1]
]

iteration = 0
player = 2

for tile in TestField:
    print(tile)

for row_index, row in enumerate(TestField):
    for col_index, tile in enumerate(row):
        if tile == 2:
            print("Player at: ", row_index, col_index)

            target_row = row_index
            target_col = col_index + 1
            TestField[row_index][col_index] = 0

            time.sleep(1)
            if TestField[target_row][target_col] == 1:
                print("Move Gets Blocked and Redrects.")
                TestField[row_index][col_index] = 2
                break

            if TestField[target_row][target_col] == 3:
                print("You Cannot here, Enemy is here")
                TestField[row_index][col_index] = 2
                break

            if TestField[target_row][target_col] == 4:
                print("item has been picked up")
                TestField[target_row][target_col] = 2
                break

            TestField[target_row][target_col] = 2
            print("Player at: ", target_row, target_col)
            break
            

for tile in TestField:
    print(tile)