from functools import reduce

numbers = [1, 2, 3, 4, 5]

# filter: keep even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)
#output: [2, 4]