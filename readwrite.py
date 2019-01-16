#reading the text

with open('myfile.txt') as f:
    full_text = f.read()

print(full_text)

#writing the text
with open('testwrite.txt', 'w') as f:
    f.write('hello')
    f.write('\n')