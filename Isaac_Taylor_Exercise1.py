

##########################################
# AREA OF A TRIANGLE
#
# Given the following variables:
#   triangle_base (number): Width of triangle base.
#   triangle_height (number): Height of triangle.
#
# Print the area of the triangle.

triangle_base = 3.3
triangle_height = 2.5

## YOUR CODE HERE ##
triangle_area = 0.5 * triangle_base * triangle_height

print("Triangle area")
print(triangle_area)

##########################################
# AREA OF A TRAPEZOID
#
# Given the following variables:
#   base_1 (number): Width of triangle base.
#   base_2 (number): Height of triangle.
#   height (number): Height of triangle.
#
# Print the area of the triangle.
# TIP: https://www.mathgoodies.com/lessons/vol1/area_trapezoid

trapezoid_base_1 = 1.1
trapezoid_base_2 = 1.3
trapezoid_height = 2.0

## YOUR CODE HERE ##
trapezoid_area = (trapezoid_base_1 + trapezoid_base_2 * trapezoid_height)/2

print("Trapezoid area")
print(trapezoid_area)
##########################################
# TIP CALCULATOR
#
# Given the following variables:
#   meal_cost (number): Cost of the meal
#   tip_percent (number): Number between 0 and 100 dentoring the percent to tip.
#
# Print the cost of the tip one line.
# Print the total cost of the meal including tip on the next line.

meal_cost = 22.0
tip_percent = 15

## YOUR CODE HERE ##

tip = meal_cost * 0.15
print("Tip")
print(tip)
total_meal_cost = tip + meal_cost
print("Ttoal")
print(total_meal_cost)
