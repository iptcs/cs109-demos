#Troll Battle
# This is a simple turn based battle which currently uses random enemy actions

# Default stats for both characters
player_stats = {
    "Name" : "La Hero",
    "Health" : 20,
    "Power" : 4,
    "Defense" : False,
    "Mana" : 6
    }

enemy_stats = {
    "Name" : "The Troll",
    "Health" : 20,
    "Power" : 4,
    "Defense" : False,
    "Mana" : 6
    }

# Defines the attack function, used to reduce enemmy health without spending mana
def attack(target_health, target_defense, user_power):
    if target_defense == False:
        target_health -= user_power
        return target_health
    else:
        return target_health

# Sets Defense stat to True, allowing it to deflect an incoming attack
def guard(user_defense):
    user_defense = True
    return user_defense

# Rage boosts the attack power of a character when called; it recieves a dictionary of stats, modifies it, then returns it
def rage(user_stats):
    if user_stats["Mana"] >= 2:
        user_stats["Power"] += 1
        user_stats["Mana"] -= 2
        print("\nRage empowers ", user_stats["Name"])
        return user_stats
    print("\n", "The power of rage will not come to ", user_stats["Name"],)
    return user_stats

# Curse decreases the enemies attack power; it works very similarly to Rage, but the Mana reduction had to be added later, since only one set of stats can be returned. Will try to address this in update
def curse(user_stats, target_stats):
    if user_stats["Mana"] >= 2:
        target_stats["Power"] -= 1
        print("\n", user_stats["Name"], " casts a profane curse upon ", target_stats["Name"])
        return target_stats
    print("\n", user_stats["Name"], " attempts to call on the forces of darkness, but they do not answer")
    return target_stats

# Soul Mutilation is an unblockable attack which does a lot of damage, but it's high cost means it can only be used once per game
def soul_mutilation(user_stats, target_stats):
    if user_stats["Mana"] >= 4:
        target_stats["Health"] -= 8
        print("\n", user_stats["Name"], " uses a forbidden spell to rend the very soul of ", target_stats["Name"])
        return target_stats
    print("\n", user_stats["Name"], " tries to cast a forbidden spell, but lacks the power")
    return target_stats

# This function is the main game loop; it recieves and modifies the stats from the beginning
def turn_cycle(player_stats, enemy_stats):
    possible_actions = ["1", "2", "3", "4", "5"] # This is a list of all valid actions, which the Troll selects randomly from
    print("The Hero's Health is currently ", player_stats["Health"], " and they have ", player_stats["Mana"], " Mana") #Status report
    print("The Troll's Health is currently ", enemy_stats["Health"], " and it has ", enemy_stats["Mana"], " Mana")
    print("""\nThe Hero's options...
          Attack - enter 1
          Guard - enter 2
          Enter Rage (2 Mana) - enter 3
          Cast Curse (2 Mana) - enter 4
          Cast Soul Mutilation - enter 5
          Do nothing - enter anything else""")
    p_action = (str(input("\nWhat will The Hero do? "))) # The player inputs a number here to make their move. The game currently has 5 total moves, 3 of which cost a limited resource called Mana
    import random
    e_action = random.choice(possible_actions) # The action of the troll is picked randomly from the aforementioned list
    if p_action == "3":
        rage(player_stats)
    if e_action == "3":
        rage(enemy_stats)
    if p_action == "4":
        curse(player_stats, enemy_stats)
        player_stats["Mana"] -= 2
    if e_action == "4":
        curse(enemy_stats, player_stats)
        enemy_stats["Mana"] -= 2
    if p_action == "5":
        soul_mutilation(player_stats, enemy_stats)
        player_stats["Mana"] -= 4
    if e_action == "5":
        soul_mutilation(enemy_stats, player_stats)
        enemy_stats["Mana"] -= 4
    if p_action == "2": # The choices are ordered like this to ensure that an Attack action cannot be resolved before a Guard action. elif and else were not used because Troll and Hero actions needed to be dispersed among one and other
        player_stats["Defense"] = guard(player_stats["Defense"])
        print("\nThe Hero raises thei guard")
    if e_action == "2":
        enemy_stats["Defense"] = guard(enemy_stats["Defense"])
        print("\nThe Troll raises its guard")
    if p_action == "1":
        enemy_stats["Health"] = attack(enemy_stats["Health"], enemy_stats["Defense"], player_stats["Power"])
        if enemy_stats["Defense"] == False:
            print("\nThe Hero attacks the Troll, reducing it's health to " + str(enemy_stats["Health"]))
        else:
            print("\nThe Hero strikes at the Troll, but their attack is deflected")
    if e_action == "1":
        player_stats["Health"] = attack(player_stats["Health"], player_stats["Defense"], enemy_stats["Power"])
        if player_stats["Defense"] == False:
            print("\nThe Troll attacks The Hero, reducing their health to " + str(player_stats["Health"]))
        else:
            print("\nThe Troll strike at The Hero, but they deflect it's attack")
    if p_action not in possible_actions:
        print("\nThe Hero does nothing")
    player_stats["Defense"] = False
    enemy_stats["Defense"] = False


print("A wild troll appears...\n") # Game intro
while player_stats["Health"] >= 1 and enemy_stats["Health"] >= 1:   # Starts and maintains the loop until someone dies
    turn_cycle(player_stats, enemy_stats)
if player_stats["Health"] <= 0:
    print("\nThe Troll has killed The Hero")    # Victory screen
else:
    print("\nThe Hero has slain the foul Troll") # Game Over
