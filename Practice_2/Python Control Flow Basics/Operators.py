x = 5 
x |= 3 
print(x) # Output: 7


#My example
i = 30
i |= 5
print(i) # Output: 31


x = 5 
x >>= 3 #Right shift rule
print(x) # Output: 0

#My example
a = 30
a >>= 5 #Right shift rule
print(a) # Output: 0

x = 5 
x <<= 3 #Left shift rule
print(x) # Output: 40   

#My example
b = 15
b <<= 2 #Left shift rule
print(b) # Output: 60


x = 5 
x ^= 3 #XOR rule
print(x) # Output: 6

#My example
c = 10
c ^= 4 #XOR rule
print(c) # Output: 14

#AND; OR; NOT RULES
x = 5
print(x > 0 and x < 10) # Output: True

x = 5
print(x < 5 or x > 10) # Output: False

x = 5
print(not(x > 3 and x < 10)) #  Output: False

#My examples
y = 15
print(y > 10 and y < 20) # Output: True

z = 8
print(z < 5 or z > 10) # Output: False

w = 12
print(not(w > 15 or w < 5)) # Output: True

#Comparison Operators
a = 10
print(a == 10) # Output: True
print(a != 5)  # Output: True
print(a > 5)   # Output: True   
print(a < 15)  # Output: True
print(a >= 10) # Output: True
print(a <= 5)  # Output: False
#My examples
b = 20
print(b == 15) # Output: False
print(b != 20)  # Output: False
print(b > 25)   # Output: False
print(b < 30)  # Output: True
print(b >= 20) # Output: True
print(b <= 15)  # Output: False

#Membership Operators
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits) # Output: True

#Check if "pineapple" is NOT present in a list:
fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits) # Output: True

#+x  -x  ~x	Unary plus, unary minus, and bitwise NOT
x = 5
print(+x)  # Output: 5
print(-x)  # Output: -5
print(~x)  # Output: -6





