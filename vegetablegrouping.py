#Read vegtables.csv into a variable called vegtables.
import csv
import json
from pprint import pprint

with open('veggies.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)

#print(vegetables)

#Group vegtables by color as a variable vegtables_by_color.
vegtables_by_color = {}
for vegetable in vegetables:
	color = vegetable['color']
	if color in vegtables_by_color:
		vegtables_by_color[color].append(vegetable)
	else:
		vegtables_by_color[color] = [vegetable]

#print vegetables by color to the temrinal.
pprint(vegtables_by_color)

#output vegtables_by_color into a json called vegtables_by_color.json.
with open('vegtables_by_color.json', 'w') as f:
    json.dump(vegtables_by_color, f, indent =2)