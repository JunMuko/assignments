# read superheroes.json
import json
import csv

with open('superheroes.json', 'r') as f:
    data = json.load(f)

# loop through each member 

members = data['members']
for member in members:
#   print(member)

# save data for each mameber into a csv file

  with open('member.csv', 'w') as f:
      writer = csv.writer(f)
      #header
      header = [
      'name', 
      'age', 
      'secretIdentity', 
      'powers', 
      'squadName', 
      'homeTown', 
      'formed', 
      'secretBase', 
      'active']
      writer.writerow(header)

#loop through member
members = data['members']
for member in members:
 
      row = [
      member["name"],
      member["age"],
      member["secretIdentity"],
      member["powers"],
      data['squadName'],
      data['homeTown'],
      data['formed'],
      data['secretBase'],
      data['active']]
      writer.writerow(row)

