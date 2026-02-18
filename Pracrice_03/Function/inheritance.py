#Inheritance

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


#example
class Student(Person):
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Student("Mike", "Olsen")
x.printname()



class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()


#example
class Buildings:
  def __init__(self, city, year):
    self.city = city
    self.year = year

  def myfunc(self):
    print("This building is in " + self.city)

class School(Buildings):
  def __init__(self, city, year):
    Buildings.__init__(self, city, year)

school = School("Almaty", 2000)
school.myfunc()





class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()


#example
class Buildings:
  def __init__(self, city, year):
    self.city = city
    self.year = year

  def myfunc(self):
    print("This building is in " + self.city)

class School(Buildings):
  def __init__(self, city, year):
    super().__init__(city, year)

school = School("Almaty", 2000)
school.myfunc()


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


class School(Buildings):
  def __init__(self, city, year, closeyear):
    super().__init__(city, year)
    self.closeyear = closeyear

  def myfunc(self):
    print("This building is in " , self.city , " It was opened in " , self.year , " and it closed in " , self.closeyear)





#My Full Example
class Buildings:
  def __init__(self, city, year):
    self.city = city
    self.year = year

  def myfunc(self):
    print("This building is in " + self.city)

class School(Buildings):
  def __init__(self, city, year, closeyear):
    super().__init__(city, year)
    self.closeyear = closeyear

  def myfunc(self):
    print("This building is in " , self.city , " It was opened in" , self.year , "and it closed in" , self.closeyear)


school = School("Almaty", 2000, 2020)
school.myfunc()

