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

def MovementSelection():
    choices = random.choice(['Left', 'Right', 'Up', 'Down'])
    return choices


def checkSpotAvailibility():
    while True:
        time.sleep(1)
        Direction = MovementSelection()
        if Direction == 'Right':
            for row_index, row in enumerate(TestField):
                for col_index, tile in enumerate(row):
                    if tile == 2:
                        print("Player at: ", row_index, col_index)

                        target_row = row_index
                        target_col = col_index + 1

                        if TestField[target_row][target_col] == 1:
                            print("Bot Cannot Move here! It Retries.")
                            continue
                            

                        print("Target at: ", target_row, target_col)
                        
                        return target_row, target_col, row_index, col_index, Direction
        
        if Direction == "Down":
            for row_index, row in enumerate(TestField):
                for col_index, tile in enumerate(row):
                    if tile == 2:
                        print("Player at: ", row_index, col_index)

                        target_row = row_index + 1
                        target_col = col_index

                        if TestField[target_row][target_col] == 1:
                            print("Bot Cannot Move here! It Retries.")
                            continue

                        print("Target at: ", target_row, target_col)

                        return target_row, target_col, row_index, col_index, Direction
                    

        if Direction == "Up":
            for row_index, row in enumerate(TestField):
                for col_index, tile in enumerate(row):
                    if tile == 2:
                        print("Player at: ", row_index, col_index)

                        target_row = row_index - 1
                        target_col = col_index 

                        if TestField[target_row][target_col] == 1:
                            print("Bot Cannot Move here! It Retries.")
                            continue
                            
                        print("Target at: ", target_row, target_col)

                        return target_row, target_col, row_index, col_index, Direction
        
        if Direction == "Left":
            for row_index, row in enumerate(TestField):
                for col_index, tile in enumerate(row):
                    if tile == 2:
                        print("Player at: ", row_index, col_index)

                        target_row = row_index
                        target_col = col_index - 1

                        if TestField[target_row][target_col] == 1:
                            print("Bot Cannot Move here! It Retries.")
                            continue

                        print("Target at: ", target_row, target_col)

                        return target_row, target_col, row_index, col_index, Direction
        

#X, Y, Desired_X, Desired_Y Positions, Last variable is the Direction in which the bot moves.
target_row_pos, target_col_pos, current_row_index, current_col_index, Direction = checkSpotAvailibility()

print(
      "---------------------------------------------\n"
      "TargetRowPos: " + str(target_row_pos) + "\n"
      "TargetColPos: " + str(target_col_pos) + "\n"
      "PreviousRowIndex: " + str(current_row_index) + "\n"
      "PreviousDirection: " + str(current_col_index) + "\n"
      "Direction: " + Direction
      )

def MoveAction(current_row, current_col, desired_row, desired_col, Direction):
        
        zewo = 0
        little_bot = 2

        if Direction == "Right":
            TestField[current_row][current_col] = zewo
            TestField[desired_row][desired_col] = little_bot
            print("---------------------------------------------")
            for tile in TestField:
                print(tile)

        if Direction == "Down":
            TestField[current_row][current_col] = zewo
            TestField[desired_row][desired_col] = little_bot
            print("---------------------------------------------")
            for tile in TestField:
                print(tile)

        if Direction == "Up":
            TestField[current_row][current_col] = zewo
            TestField[desired_row][desired_col] = little_bot
            print("---------------------------------------------")
            for tile in TestField:
                print(tile)

        if Direction == "left":
            TestField[current_row][current_col] = zewo
            TestField[desired_row][desired_col] = little_bot

MoveAction(current_row_index, current_col_index, target_row_pos, target_col_pos, Direction)

def EnemyMoveDirection():
    pass

"""
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
"""           
