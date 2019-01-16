# reading a text file
with open('myfile.txt') as f:
    full_text = f.read()

print(full_text)

# writing a text file
with open('testwrite.txt', 'a') as f:
    f.write('hello')
    f.write('\n')