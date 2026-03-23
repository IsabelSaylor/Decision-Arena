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
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 4, 0, 0, 1],
    [1, 1, 1, 1, 1, 1]
]

direction_deltas = {
    "Up": (-1, 0),
    "Down":(1, 0),
    "Left":(0, -1),
    "Right":(0, 1)
}


class Entity:
    
    def __init__(self, name, hp, row, col, symbol):
        self.name = name
        self.hp = hp
        self.row = row
        self.col = col
        self.symbol = symbol

bot = Entity(name="Bot", hp=100, row=1, col=1, symbol=2)
enemy = Entity(name="Enemy", hp=50, row=3, col=4, symbol=3)

TestField[bot.row][bot.col] = bot.symbol
TestField[enemy.row][enemy.col] = enemy.symbol

def MovementSelection():
    return random.choice(list(direction_deltas.keys()))


def checkSpotAvailability():
    while True:
        time.sleep(1)
        Direction = MovementSelection()
        delta_row, delta_col = direction_deltas[Direction]

        for row_index, row in enumerate(TestField):
            for col_index, tile in enumerate(row):
                if tile == bot.symbol:
                    target_row = row_index + delta_row
                    target_col = col_index + delta_col

                    if TestField[target_row][target_col] == 1:
                        print(f"Bot cannot move {Direction}! Retrying...")
                        break

                    if TestField[target_row][target_col] == enemy.symbol:
                        pass

                    return target_row, target_col, row_index, col_index, Direction


def MoveAction(current_row, current_col, desired_row, desired_col, Direction):
    
    TestField[current_row][current_col] = 0
    TestField[desired_row][desired_col] = bot.symbol
    print(f"\nBot Moved {Direction}")
    print("---------------------------------------------")
    

def EnemyCheckSpotAvailability():
    while True:
        time.sleep(1)
        Direction = MovementSelection()
        delta_row, delta_col = direction_deltas[Direction]

        for row_index, row in enumerate(TestField):
            for col_index, tile in enumerate(row):
                if tile == enemy.symbol:
                    target_row = row_index + delta_row
                    target_col = col_index + delta_col

                    if TestField[target_row][target_col] == 1:
                        print(f"Enemy cannot move {Direction}! Retrying...")
                        break
                    return target_row, target_col, row_index, col_index, Direction


def EnemyMoveAction(current_row, current_col, desired_row, desired_col, Direction):
    
    TestField[current_row][current_col] = 0
    TestField[desired_row][desired_col] = enemy.symbol
    print(f"\nEnemy Moved {Direction}")
    print("---------------------------------------------")
    

while True: 
    time.sleep(1)
    target_row, target_col, current_row, current_col, Direction = checkSpotAvailability()
    target_row_enemy, target_col_enemy, current_row_enemy, current_col_enemy, Direction_enemy = EnemyCheckSpotAvailability()

    EnemyMoveAction(current_row_enemy, current_col_enemy, target_row_enemy, target_col_enemy, Direction_enemy)
    MoveAction(current_row, current_col, target_row, target_col, Direction)
    for row in TestField:
        print(row)  