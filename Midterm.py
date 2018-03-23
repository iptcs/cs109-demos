##stats = [20, 4, 0, 6, 20, 4, 0, 6]
p_hp = 20
p_power = 4
p_defense = 0
p_mana = 6
e_hp = 20
e_power = 4
e_defense =0
e_mana = 6

def p_attack(e_hp, p_power, e_defense):
    p_power -= e_defense
    e_hp -= p_power
    return e_hp

def p_guard(p_defense):
    p_defense += 3
    return p_defense

def e_attack(p_hp, e_power, p_defense):
    e_power -= p_defense
    p_hp -= e_power
    return p_hp

def e_guard(e_defense):
    e_defense += 3
    return e_defense

##def p_turn(stats):
##    print("It's your turn, your options are...")
##    print("Attack")
##    print("Guard")
##    print("Spells")
##    print("Do nothing")
##    action = input("/nWhat will you do?").lower
##    if action == "attack":
##        e_hp = p_attack(p_power, e_hp, e_guard)
##    elif action == "guard":
##        p_defense = p_guard(p_defense)

while e_hp >= 0 and p_hp >= 0:
    #Player turn
    print("It's your turn")
    print("Player Health: ", p_hp)
    print("Player Mana: ", p_mana)
    print("Enemy HP: ", e_hp)
    print("Enemy Mana: ", e_mana)
    print("You may:")
    print("Attack")
    print("Guard")
    print("Spells")
    print("Do nothing")
    p_action = str(input("\nWhat will you do? ").lower)
    if "attack" in p_action:
        e_hp = p_attack(p_power, e_hp, e_guard)
    elif "guard" in p_action:
        p_defense = p_guard(p_defense)
    else:
        print("You do nothig...")
    print("It's your opponent's turn")
    print("Player Health: ", p_hp)
    print("Player Mana: ", p_mana)
    print("Enemy HP: ", e_hp)
    print("Enemy Mana: ", e_mana)
    e_defense = 0
    #Enemy turn
    import random
    e_action = random.randrange(1, 4)
    if e_action == 1:
        p_hp = e_attack(p_hp, e_power, p_defense)
        print("The enemy attacks you")
    elif e_action == 2:
        e_defense = e_guard(e_defense)
        print("The enemy guards against your attack")
    p_defense = 0
