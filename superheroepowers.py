# load libraries
import json

# read superhero.json

with open('superheroes.json', 'r') as f:
    superheroes = json.load(f)

#print(superheroes)

allpowers = []

#  get the members
members = superheroes['members']

#print(members)

# loop through each members
for member in members:
    # for each member, get a list of the powers
    powers = member['powers']
    # loop through the powers and print each one
    for power in powers:
    	print(power)
    	#allpower.append(powers)

#make the list unique. unique value can be done by "set"
unique_powers = list(set(powers))
print(unique_powers)