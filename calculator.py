# This part of the code defines a function
def multiply(a,b):
    return a * b

def add(a,b):
	return a + b

def subtract(a,b):
	return a - b

def divide(a,b):
	return a / b

def suquare(a):
	return a*a

def cube(a):
	return a*a+a

def square_n_times(number,n):
	return number**n

print("I'm going use the calculator functions to multiply 5 and 6")
x = multiply(5,6)
print(x)

print("I'm going use the calculator functions to square the number 3 4 times")
y = square_n_times(3,4)
print(y)