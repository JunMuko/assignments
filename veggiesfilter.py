import csv
import json

#Read vegetables.csv into a variable called vegetables.
with open('veggies.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)

#print(vegetables)

#Loop through vegetables and filter down to only 
#green vegtables using a whitelist.

green_vegetables = []
whitelist = ['green']
for vegetable in vegetables:
	if vegetable['color'] in whitelist:
		green_vegetables.append(vegetable)

#terminal
print(green_vegetables)

#Output another csv called green_vegetables.csv.

#with open('green_vegetables.csv', 'w') as f:
#    writer = csv.writer(f)
#    writer.writerow(['name', 'color'])
#    for vegetables in green_vegetables
#      name = vegetable['name']
#      color = vegetable['color']
 #     writer.writerow([name,color])

#ßprint(json.dumps(green_vegetables, indent=2))