from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map: square numbers
squares = list(map(lambda x: x**2, numbers))
print(squares)
#output: [1, 4, 9, 16, 25]

