### Creating lists

# Hard code dat shit
three_elf_rings = ["Galadriel", "Gandalf the Grey", "Elrond"]
print(three_elf_rings)

# Appendin' this mutha fucka
rule_of_two =[]
rule_of_two.append("Bane")
print(rule_of_two)
rule_of_two.append("Zannah")
print(rule_of_two)

# Splitin' it up
kings_in_the_north = "Ned Stark - Robb Stark" .split(" - ")
print(kings_in_the_north)

# Range it up, boi
numbers = list(range(20, 40, 60))
print(numbers)

# Slickity Slicey
list_A = ["A", "B", "C", 1, 5, 10]
sub_list_A  = list_A[1:5]
print(sub_list_A)

# C-c-c-concatenate!
lords = three_elf_rings + rule_of_two + kings_in_the_north + ["16"]
print(lords)

# Every day I'm sortin'
lords.sort()
print(lords)
number_list = [4, 8, 12, 16, 20]
number_list.sort()
print(number_list)


stuff_thangs = [3, 1.5, 0, "Stuff", "THAAANGS"]
stuff_thangs.sort()
print(stuff_thangs)
