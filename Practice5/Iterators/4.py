class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
# Output: 1
# Output: 2 till 20


#example
class Mystr:
  def __iter__(self):
    self.a = 0
    return self
  def __next__(self):
    if self.a < 3:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
mystr = Mystr()
myiter = iter(mystr)
for x in myiter:
  print(x)
# Output: 0
# Output: 1
# Output: 2
