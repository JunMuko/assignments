# read superheroes.json
import json
import csv

with open('superheroes.json', 'r') as f:
    superheroes = json.load(f)

# save data for each mameber into a csv file

with open('member.csv', 'w') as f:
    writer = csv.writer(f)

#write header
    header = ['name', 'age', 'secretIdentity', 'powers', 'squadName', 'homeTown', 'formed', 'secretBase', 'active']
    writer.writerow(header)

# loop through each member 
    members = superheroes['members']
    for member in members:
#   print(member)

 #define variables
        name = member["name"]
        age = member["age"]
        secretIdentity = member["secretIdentity"]
        power = member["powers"]
        squadName = superheroes['squadName']
        homeTown = superheroes['homeTown']
        formed = superheroes['formed']
        secretBase = superheroes['secretBase']
        active = superheroes['active']
#write to csv
        row = [name, age, secretIdentity, power, squadName, homeTown, formed, secretBase, active]
        writer.writerow(row)

