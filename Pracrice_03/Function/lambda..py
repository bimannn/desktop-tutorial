def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#example
def my_func(n):
  return lambda a : a / n * a

my_a = my_func(4)
print(my_a(8))
