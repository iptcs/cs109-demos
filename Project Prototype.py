#Ascension
#Train your magic to defeat the four celestial princes

#Each prince is based on a different planet in the solar system
##Each prince is a function that runs a random challenge
##Each challenge is essentially a riddle based on the prince's planet
##The riddles test the player's knowlegde of the solar system

#Each Prince takses something away from the player when the player defeats them,
#meaning the game gets harder whenever you defeat a prince
#Ideas
##Jupiter adds a false choice to all the other prince's challenges
##Saturn resurrects a random fallen prince, other than himself
##Mars forces you to complete an extra challenge to finish off the others
##Venus forces you to fight the others in a random order

#Faling a challenge causes you to lose a life
##When you run out of lives, you restart the game

#Players select one of three gifts at the start of the game
#Ideas
##The Aegis protects you from one attack
##The Eye eliminates one false option from riddles
##The Curse eliminates one prince from the game

#Make a list containing aspects of the player, such as their remaining lives
#and gifts

#Make a list of remaining princes
#Make a function for each prince that poses a challenge, then removes them from
#the 'princes remaining' list and adds them to the 'fallen princes' list

#Each prince must account for gifts, princes defeated
#If
#While
#Functions
#For



def Egg_Riddle:
    print("I am a box without hinges, key or lid, yet golden treasure inside is hid")
    correct_answers = ["EGGS", "AN EGG", "EGG", "YOU'RE AN EGG"]
    while player_answer not in correct_answers:
        player_answer = input("What am I? ").upper
        if player_answer not in correct_answers:
            print("Wrong")
            return('wrong')
        else:
            print("You've chosen wisely")
            enemies_defeated.append("Cagliostro")
            return('correct')
    



enemies_defeated = []
victory_condition = ["X", "Y", "z"]

while enemies_defeated != victory_condition:
    run game loop

import random

Functions

Lists of Riddles

Lists of Correct Answers (names should correspond in some way with riddle names)

Create variables:
    level = 1
    brennan_active = False
    mack_active = False

Print explanation of game and prompt user to start the game (blank input function)

i.e., input("Press enter to start!")

While True:
    if level == 1:
        do this
        level += 1
    elif level == 2:
        do this
        level += 1
    break


LIST_NAME[(import.randrange(len(LIST_NAME))]
    
    
