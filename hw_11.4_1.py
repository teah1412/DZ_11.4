# Write a Python program that finds out who ate the ice cream. Your country will be grateful!

# Hint: There are Python functions that help you find a string within a string.

import json

# 1. Dictionary of DNA traits
hair = {
    "black": "CCAGCAATCGC",
    "brown": "GCCAGTGCCG",
    "blonde": "TTAGCTATCGC"
    }

face = {
    "square": "GCCACGG",
    "round": "ACCACAA",
    "oval": "AGGCCTCA"
    }

eyes = {
    "blue": "TTGTGGTGGC",
    "green": "GGGAGGTGGC",
    "brown": "AAGTAGTGAC"
    }

gender = {
    "female": "TGAAGGACCTTC",
    "male": "TGCAGGAACTTC"
    }

race = {
    "white": "AAAACCTCA",
    "black": "CGACTACAG",
    "asian": "CGCGGGCCG"
    }

# 2. Dictionary of suspects with a list of their traits taken from the dictionary

suspects = {
    "Eva": ["female", "white", "blonde", "blue", "oval"],
    "Larisa": ["female", "white", "brown", "brown", "oval"],
    "Matej": ["male", "white", "black", "blue", "oval"],
    "Miha": ["male", "white", "brown", "green", "square"]
    }


# 3. We have all dictionaries and our suspects. Next, import the suspect's DNA:

with open("dna.txt", "r") as suspect_file:
    dna = suspect_file.read()

# And make the suspect blank value:

person = []

# 5. now we have to make a program that looks for traits in the suspect's DNA

for i in gender:
    if gender[i] in dna:
        print(i)
        person.append(i)

for i in race:
    if race[i] in dna:
        print(i)
        person.append(i)

for i in hair:
    if hair[i] in dna:
        print(i)
        person.append(i)

for i in eyes:
    if eyes[i] in dna:
        print(i)
        person.append(i)

for i in face:
    if face[i] in dna:
        print(i)
        person.append(i)

# 6. This will give us the suspect's description. Now to compare who matches:

for p in people:
    if suspects[s] == person:
        print("The person we're looking for is {0}".format(s.upper()))
        break
