#Demonstrating dictionaries
fruit_prices = {
    "Apple" : 2.79, 
    "Bananas" : 3.45, 
    "Orange" : 1.50
}

state_capitals = {}

#Add items

state_capitals["MA"] = "Boston"
state_capitals["NY"] = "Albany"
state_capitals["CA"] = "Sacramento"
print(state_capitals)

#Get size
print(len(state_capitals))


#Overwrite
state_capitals["MA"] = "Amherst"
print(state_capitals)


print(state_capitals["MA"])

print()

# Dem Methods of dose dicts

states = list(state_capitals.keys())
print(states)


captials = list(state_capitals.values())
print(captials)


# Iterating over dat dictionary
for k, v in state_capitals.items():
    print("The captial of " + k + " is " +v)

# A common method for storing data
state_data = [
    {
    "Name" : "California",
    "Addr" : "CA",
    "Capital" : "Sacremento",
    "Population" : 39250000
    }, {
    "Name" : "Alabama",
    "Addr" : "AL",
    "Capital" : "Montgomery",
    "Population" : 6666666
        }
    ]

def my_function(my_dict):
    my_dict["f_name"] = "Isaac"
    my_dict["l_name"] = "Taylor"
    #return my_dict
    ##Works with or without return

initial = {"age" : 22}
result = my_function(initial)
print(initial)
