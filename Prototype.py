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

defend_options = ["block", "take_damage"]
attack_options = ["hit", "walk"]
weighted_attack_options = random.choices(attack_options, weights=(3, 6))


class Entity:
    
    def __init__(self, name, hp, row, col, symbol, defense, hit_chance_self):
        self.name = name
        self.hp = hp
        self.row = row
        self.col = col
        self.symbol = symbol
        self.defense = defense
        self.hit_chance_self = hit_chance_self

    def DealDamage(self, defender, damage):
        print("damage is in fact being done")
        defender.TakeDamage(damage)
        pass

    def TakeDamage(self, damage):
        self.hp -= damage
        print(f"{self.name} has taken {damage} Damage!")
        pass

bot = Entity(name="Bot", hp=100, row=1, col=1, symbol=2, defense=5, hit_chance_self=7)
enemy = Entity(name="Enemy", hp=50, row=3, col=4, symbol=3, defense=8, hit_chance_self=10)

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
                        print(str(row_index) + " | " + str(col_index))
                        TestField[row_index][col_index] == bot.symbol
                        TestField[target_row][target_col] = enemy.symbol

                        fightAction(bot, enemy)

                        break

                    return target_row, target_col, row_index, col_index, Direction


def fightAction(bot, enemy):
    print(f"{bot.name} is fighting {enemy.name}")

    bot_choice = weighted_attack_options
    enemy_choice = weighted_attack_options

    
    if bot_choice == "hit":

        weighted_defend_options = random.choices(defend_options, weights=(enemy.defense, enemy.hit_chance_self))
        
        if weighted_defend_options == "block":
            print(f"Enemy has {enemy.hp}! Attack was blocked!")
            time.sleep(1)

        if weighted_defend_options == "take_damage":
            bot.DealDamage(enemy, 5)
            print(f"Enemy has {enemy.hp} HP left.")
            

    for row in TestField:
        print(row)
    time.sleep(2)  
    


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

                    if TestField[target_row][target_col] == bot.symbol:
                        
                        TestField[row_index][col_index] = enemy.symbol
                        TestField[target_row][target_col] == bot.symbol

                        break

                    return target_row, target_col, row_index, col_index, Direction


def EnemyMoveAction(current_row, current_col, desired_row, desired_col, Direction):
    
    TestField[current_row][current_col] = 0
    TestField[desired_row][desired_col] = enemy.symbol
    print(f"\nEnemy Moved {Direction}")
    print("---------------------------------------------")
    

while True: 
    time.sleep(2.5)
    target_row, target_col, current_row, current_col, Direction = checkSpotAvailability()
    target_row_enemy, target_col_enemy, current_row_enemy, current_col_enemy, Direction_enemy = EnemyCheckSpotAvailability()
    
    MoveAction(current_row, current_col, target_row, target_col, Direction)
    EnemyMoveAction(current_row_enemy, current_col_enemy, target_row_enemy, target_col_enemy, Direction_enemy)
    
    for row in TestField:
        print(row)