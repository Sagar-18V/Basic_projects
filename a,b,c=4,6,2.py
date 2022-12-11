# Python program to demonstrate nested ternary operator
#a, b =  20,10

#print ("Both a and b are equal" if a == b else "a is greater than b"
#		if a > b else "b is greater than a")

# Python Program to perform addition
# of two complex numbers using binary
# + operator overloading.

class complex:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	# adding two objects
	def __add__(self, other):
		return self.a + other.a, self.b + other.b

Ob1 = complex(1, 2)
Ob2 = complex(2, 3)
Ob3 = Ob1 + Ob2
print(Ob3)
