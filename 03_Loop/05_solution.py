# Find the First Non-Repeated Character
character = "awabbcddd"
non_reptation = ""

for char in character:
    if character.count(char)==1:
        non_reptation += char
        break
print("non reptation character is: ",non_reptation)