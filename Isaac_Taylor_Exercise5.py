##################################################
# AVERAGE NUMBERS, IGNORE STRINGS
#
# Assume we have a variable called stuff. In this variable,
# there is a list. The list contains numbers AND strings.
#
# Print the average of all of the numbers. Ignore the strings.
#

stuff = [2, "three", 4.5, -7, "dog", 3.14]
new_stuff = []

for x in stuff:
    if isinstance(x, int) or isinstance(x, float):
        new_stuff.append(x)
print(new_stuff)
total = 0
for number in new_stuff:
    total += number    

average = total / len(new_stuff)
print(average)
#Divide the sum by the count
