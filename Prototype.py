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
attack_options = ["hit", "run"]
weighted_attack_options = random.choices(attack_options, weights=(10, 0))


class Entity:
    
    def __init__(self, name, hp, row, col, symbol, defense, hit_chance_self):
        self.name = name
        self.hp = hp
        self.row = row
        self.col = col
        self.symbol = symbol
        self.defense = defense
        self.hit_chance_self = hit_chance_self

    def move(self, d_row, d_col):
        self.row += d_row
        self.col += d_col

    def TakeDamage(self, damage):
        self.hp -= damage
        print(str(self.hp) + self.name)


class MLBot:
    
    def __init__(self, model):
        self.model = model

    def decide(self, state):
        return self.model.predict(state)
        

class EnemyBrain:

    def decide(self, self_entity, target):

        dr = target.row - self_entity.row
        dc = target.col - self_entity.col

        step_row = 0
        step_col = 0

        # If vertical distance is bigger, move vertically
        if abs(dr) > abs(dc):
            step_row = 1 if dr > 0 else -1

        # Otherwise move horizontally
        elif dc != 0:
            step_col = 1 if dc > 0 else -1

        # If perfectly aligned vertically, still allow horizontal fallback only if needed
        elif dr == 0 and dc != 0:
            step_col = 1 if dc > 0 else -1

        return step_row, step_col

bot = Entity(name="Bot", hp=100, row=1, col=1, symbol=2, defense=5, hit_chance_self=7)
enemy = Entity(name="Enemy", hp=50, row=4, col=4, symbol=3, defense=0, hit_chance_self=10)

enemy_brain = EnemyBrain()

def DealDamage(attacker, defender, damage):
    defender.TakeDamage(damage)



TestField[bot.row][bot.col] = bot.symbol
TestField[enemy.row][enemy.col] = enemy.symbol


def MovementSelection():
    return random.choice(list(direction_deltas.keys()))


def checkSpotAvailability():
    while True:
        #time.sleep(1)
        Direction = MovementSelection()
        delta_row, delta_col = direction_deltas[Direction]



        """
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

                        botfightAction(bot, enemy)

                        break

                    return target_row, target_col, row_index, col_index, Direction
"""

def MoveAction(current_row, current_col, desired_row, desired_col, Direction):
    
    TestField[current_row][current_col] = 0
    TestField[desired_row][desired_col] = bot.symbol
    print(f"\nBot Moved {Direction}")
    print("---------------------------------------------")
    

def EnemyMoveAction(current_row, current_col, desired_row, desired_col, Direction):
    
    TestField[current_row][current_col] = 0
    TestField[desired_row][desired_col] = enemy.symbol
    print(f"\nEnemy Moved {Direction}")
    print("---------------------------------------------")


def fightAction(Entity1, Entity2):
    
    attack_pick = weighted_attack_options
    print(attack_pick)

    if attack_pick[0] == "hit":
        DealDamage(Entity1, Entity2, 10)
        pass


def EnemyMovement():
    step_row, step_col = enemy_brain.decide(enemy, bot)
        
    new_row = enemy.row + step_row
    new_col = enemy.col + step_col

    old_row = enemy.row
    old_col = enemy.col


    # Read the tile to ensure we can move into position
    tile = TestField[new_row][new_col]


    if tile == 1:
        # tile is blocked
        pass
    elif tile == bot.symbol:
        print(fightAction(enemy, bot))
        
        
    elif tile == 0:
        # allowed to move
        TestField[old_row][old_col] = 0
        TestField[new_row][new_col] = enemy.symbol

        # updates enemy position
        enemy.row = new_row
        enemy.col = new_col
            
    elif tile == 4:
        print("test item picked up")
        TestField[old_row][old_col] = 0
        TestField[new_row][new_col] = enemy.symbol

        # updates enemy position
        enemy.row = new_row
        enemy.col = new_col
        
    for row in TestField:
        print(row)


def AgentMovement():
    pass

while True:
    time.sleep(2.5)
    EnemyMovement()