def square_generator(n):
    for i in range(n + 1):
        yield i ** 2

squares = square_generator(5)
for value in squares:
    print(value)



def even_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

evens = even_generator(10)
for value in evens:
    print(value)




def divisible_by_3_and_4_generator(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
divisible_numbers = divisible_by_3_and_4_generator(50)
for value in divisible_numbers:
    print(value)

def squares(a,b):
    for i in range(a, b + 1):
        yield i ** 2

squares_in_range = squares(1, 5)
for value in squares_in_range:
    print(value)


def countdown(n):
    while n >= 0:
        yield n
        n -= 1

countdown_generator = countdown(5)
for value in countdown_generator:
    print(value)