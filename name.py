#reading the text

with open('name.txt') as f:
    my_name = f.read()

print(my_name)

#writing the text
with open('hello.txt', 'w') as f:
    f.write('Hello, my name is ' + my_name + '.')
    f.write('\n')