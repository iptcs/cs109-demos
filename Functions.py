def sqr_number(x):
    sqr = x * x
    print(sqr)
    return sqr
z = int(input("Pick a number: "))
z_sqrd = sqr_number(z)

def my_max(a, b):
    if a > b:
        return a
    else:
        return b

print(my_max(5, 8))

def my_max_2():
    a = int(input("Enter number A: "))
    b = int(input("Enter number B: "))
    if a > b:
        return a
    else:
        return b
    
a = my_max_2()
print(a)

input("Press enter to exit")
