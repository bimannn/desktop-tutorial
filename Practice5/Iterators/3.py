class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
# Output: 1
# Output: 2
# Output: 3
# Output: 4


#example
class Mystr:
  def __iter__(self):
    self.a = 0
    return self
  def __next__(self):
    x = self.a
    self.a += 1
    return x
mystr = Mystr()
myiter = iter(mystr)
print(next(myiter))
print(next(myiter))
print(next(myiter))
# Output: 0
# Output: 1
# Output: 2

