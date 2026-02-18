def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

#examples
from math import sqrt
def Pifagor_find(a, b):
   return sqrt(a**2 + b**2)
print(Pifagor_find(3, 4))

#Argumnents
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#example
def my_function(name):
  print(name + " Mamyrkhan")

my_function("Biman")
my_function("Dariya")

#key arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

#example
def my_function(friend, age):
  print("My friend name is " + friend)
  print("He is " + age + " years old")

my_function(friend= "Aman", age= "18")


#Example 3:Returning values

def calculate_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

nums = [1, 2, 3, 4]
print(calculate_sum(nums))
