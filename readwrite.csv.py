import csv

#write a csv file
#with open('testwrite.csv', 'w') as f:
#    writer = csv.writer(f)
#    writer.writerow(['col1', 'col2'])
#    writer.writerow(['val1', 'val2'])
#    writer.writerow(['val1', 'val2'])
#    writer.writerow(['val1', 'val2'])

 #read from a csv
# with open('testwrite.csv', 'r') as f:
#    reader = csv.DictReader(f)
#    rows = list(reader)

#  for row in rows*
#     print(row)


vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

#open csv
with open('veggies.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'color'])
 	#loop through veggies
    for vegetable in vegetables:
  	#write each vegitable to a csv
      name = vegetable['name']

      color = vegetable['color']
      row =[name, color]

      writer.writerow(row)
