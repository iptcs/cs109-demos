player_stats = {
    "Name" : "Hero",
    "Health" : 20,
    "Power" : 4,
    "Defense" : 0,
    "Mana" : 6
    }

enemy_stats = {
    "Name" : "Troll",
    "Health" : 20,
    "Power" : 4,
    "Defense" : 0,
    "Mana" : 6
    }

def attack(target_health, target_defense, user_power):
    user_power -= target_defense
    target_health -= user_power
    return target_health

def guard(user_defense):
    user_defense += 3
    return user_defense

def evaluate_action(player_stats, enemy_stats):
    potential_actions["attack", "guard", "do nothing"]
    sim_player = {}
    sim_player.update(player_stats)
    sim_enemy = {}
    sim_enemy.update(enemy_stats)
    turn_value = 0
    for action in potential actions:
        p_action = (str(input("\nWhat will you do? ").lower()))
        e_action = (str(input("\nWhat will the troll do? ").lower()))
        if "attack" in p_action:
            enemy_stats["Health"] = attack(enemy_stats["Health"],
                                           enemy_stats["Defense"],
                                           player_stats["Power"])
            print("\nYou attack the Troll, reducing it's health to " + str(enemy_stats["Health"]))
            input("")
        elif "guard" in p_action:
            player_stats["Defense"] = guard(player_stats["Defense"])
            print("\nYou raise your guard")
            input("")
        else:
            print("\nYou do nothing")
            input("")
        if "attack" in e_action:
            player_stats["Health"] = attack(player_stats["Health"],
                                           player_stats["Defense"],
                                           enemy_stats["Power"])
            print("\nThe Troll attacks you, reducing your health to " + str(player_stats["Health"]))
            input("")
        elif "guard" in e_action:
            enemy_stats["Defense"] = guard(enemy_stats["Defense"])
            print("\nThe Troll raises its guard")
            input("")
        else:
            print("\nThe Troll stares at you")
            input("")

def simulate_action(player_stats, enemy_stats, test_action):
    comparison = sim_target["Health"]
    sim_player = {}
    sim_player.update(player_stats)
    sim_enemy = {}
    sim_enemy.update(enemy_stats)
    if "attack" in test_action:
            sim_target["Health"] = attack(sim_target["Health"],
                                           sim_target["Defense"],
                                           sim_player["Power"])
    ## number representing health change
    ## list of of actions and their values

## Variation of turn cycle


def turn_cycle(player_stats, enemy_stats):
    print(player_stats)
    print(enemy_stats)
    print("""\nYour options...
          Attack
          Guard
          Spells
          Do nothing""")
    p_action = (str(input("\nWhat will you do? ").lower()))
    e_action = (str(input("\nWhat will the troll do? ").lower()))
    if "attack" in p_action:
        enemy_stats["Health"] = attack(enemy_stats["Health"],
                                       enemy_stats["Defense"],
                                       player_stats["Power"])
        print("\nYou attack the Troll, reducing it's health to " + str(enemy_stats["Health"]))
        input("")
    elif "guard" in p_action:
        player_stats["Defense"] = guard(player_stats["Defense"])
        print("\nYou raise your guard")
        input("")
    else:
        print("\nYou do nothing")
        input("")
    if "attack" in e_action:
        player_stats["Health"] = attack(player_stats["Health"],
                                       player_stats["Defense"],
                                       enemy_stats["Power"])
        print("\nThe Troll attacks you, reducing your health to " + str(player_stats["Health"]))
        input("")
    elif "guard" in e_action:
        enemy_stats["Defense"] = guard(enemy_stats["Defense"])
        print("\nThe Troll raises its guard")
        input("")
    else:
        print("\nThe Troll stares at you")
        input("")

print("A wild troll appears...\n")
while player_stats["Health"] >= 1 and enemy_stats["Health"] >= 1:
    turn_cycle(player_stats, enemy_stats)
if player_stats["Health"] <= 0:
    print("\nThe Troll has killed you")
else:
    print("\nYou have slain the foul Troll")
