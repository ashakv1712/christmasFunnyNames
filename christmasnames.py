print("Christmas is coming!!")
print("\nGenerate a random Christmas character name for yourself!\n")

import random

adjectives = open("adjectives.txt", "r")
adjective_list = []

while(adjectives.readline() != ""):
    split = adjectives.readline().split('\n')
    adjective_list.append(split[0])

characters = open("christmascharacters.txt", "r", encoding="utf-8")
christmas_characters = []

while(characters.readline() != ""):
    split = characters.readline().split("\n")
    christmas_characters.append(split[0])


adjectives.close()
characters.close()

print(f"Your christmas character name is '{random.choice(adjective_list)} {random.choice(christmas_characters)}'")


