# load libraries
import json

# read superhero.json

with open('superheroes.json', 'r') as f:
    superheroes = json.load(f)

data = []

#  get the members
members = superheroes['members']

#print(members)

# loop through each members
for member in members:
    # for each member, get a list of the powers
    powers = member['powers']
    # loop through the powers and print each one
    for power in powers:
    	data.append(power)

#make the list unique. unique value can be done by "set"
unique_powers = list(set(data))
print(unique_powers)