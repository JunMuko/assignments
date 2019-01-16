# read veggies.csv
import csv
import json

with open('veggies.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)

# convert to JSON
#print(vegetables)

#print rows
print(json.dumps(vegetables,indent=2))

# save Json as an vegetables.json
with open('cookedveggies.json', 'w') as f:
    json.dump(vegetables, f, indent=2)