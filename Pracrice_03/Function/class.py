class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

class Person:
  pass
p1 = Person()
p1.name = "John"
p1.age = 36
print(p1.name)  


class Pet:
  pass
my_pet = Pet()
my_pet.name = "Buddy"
my_pet.type = "Dog"
print(my_pet.name)  


#Python __init__() Method
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.myfunc()
print(p1)


#Examples
class Buildings:
  def __init__(self, city, year):
    self.city = city
    self.year = year
  def myfunc(self):
    print("This building is in " + self.city)  

school = Buildings("Almaty", 2000)
school.myfunc()



#Python self Parameter
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    def myfunc(self):
      print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


#Use the words myobject and abc instead of self:

class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet()


#Example
class Car:
  def __init__(maobj, brand, model):
    maobj.brand = brand
    maobj.model = model

    def car_info(abc):
        print("my car is " , abc.brand, "model is " , abc.model)

my_car = Car("Toyota", "Camry")
my_car.car_info()


#Call one method from another method using self:

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome()


#Example
class Friend:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "whasup, " + self.name
  
  def condition(self):
    mes = self.greet()
    print(mes + "! How are you doing?")

my_friend = Friend("Aman")
my_friend.condition()
  


