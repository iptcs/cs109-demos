###############################
# Print Range
#
# Giving the following variables:
#   start (number): The lower bound of the range.
#   end (number): The upper bound of the range.
#   stride (number): The amount to increment when counting.
#
#
# Print all numbers between `start` and `end` at
# intervals of `stride`
#
# Example:
#   if start = 0, end = 5, stride = 1, then print
#   0
#   1
#   2
#   3
#   4
#   5
#
# Example:
#   if start = 2, end = 3.2, stride = 0.5, then print
#   2
#   2.5
#   3.0

start = 2
end = 3.2
stride = 0.5

### Your code here ###
start = 0
end = 25
stride = 5

while start < end:
    print(start)
    start += stride
print(end)


###############################
# Wheel of Fortune
#
# WARNING: This exersise is significantly harder than what
# we have done up until this point. You should attempt it,
# but if you cannot complete it that is fine.
#
# Giving the following variables:
#   word (string): The secret word to guess
#
# Write a program that shows a string of underscores ("_") of
# the same length as `word`. We will refer to this sting as the
# board. Using a loop, take a single character input from the
# user. If the input character exists in the secret word,
# replace the underscores on the board in the same positions
# as character in the secret word with the character.
#
# Once all characters in the secret word have been input,
# the board should be equal to the secret word.
#
# Basically we are trying to recreate a simple version of
# the "Wheel of Fortune" or "hangman".
# https://www.coolmath-games.com/0-hangman
#
# EXAMPLE: Using the word "lollipop" the output should look
# something like this:
# 
# ________ | Enter a letter: l
# l_ll____ | Enter a letter: p
# l_ll_p_p | Enter a letter: i
# l_llip_p | Enter a letter: o
# lollipop Correct!

word = "lollipop"

### Your code here ###
