###############################
# GRADE
#
# Given the score (0 to 100) received on a test, print the letter grade.
# You can just give the letter, no need for the +/-
#
# The score should be taken from user input.
#
# In case you have been at Hampshire long enough to forget how grades work,
# you can use the first table on this wikipedia page:
# https://en.wikipedia.org/wiki/Academic_grading_in_the_United_States

### YOUR CODE HERE ###
score = int(input("What was your score? "))
print()
if score <= -1:
    print("You've redefined the conept of failure")
if score <= 59 and score > -1:
    print("You FAILED! >:[")
elif score >=60 and score < 70:
    print("You get a D.")
elif score >=69 and score < 80:
    print("You get a c.")
elif score >=79 and score < 90:
    print("You get a D.")
elif score >=90 and score < 101:
    print("You get an A!")
elif score >= 101:
    print("You have transcended the very notion of a grade")

###############################
# AREA
#
# Take user input to determine the name of a shape (rectangle or triangle)
#
# Depending on the shape name, create as many variables as needed and set their
# values based on user input.
#
# Print the area of the shape.

### YOUR CODE HERE ###
##Tried using the lower command but couldn't figure it out
print()
shape_type = str(input("Is your shape a triangle, or a rectangle? "))
print()
if shape_type == "triangle":
    triangle_base = int(input("What is the base of your triangle? "))
    triangle_height = int(input("What is the height of your triangle? "))
    print()

    triangle_area = 0.5 * triangle_base * triangle_height
    print("The area of your triangle is ", triangle_area)

elif shape_type == "rectangle":
    rectangle_width = int(input("What is the width of your rectangle? "))
    rectangle_length = int(input("What is the length of your rectangle? "))
    print()
    
    rectangle_area = rectangle_width * rectangle_length
    print("The area of your rectangle is ", rectangle_area)
else:
    print("You must select either a triangle or a rectangle... bro.")
print()
print()
input("Press enter to exit")
