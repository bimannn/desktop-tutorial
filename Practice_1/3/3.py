x = {"name" : "John", "age" : 36}
print(x)


x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))


x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


#example number 1
person = {"first_name": "Alice", "last_name": "Smith", "age": 30}
print(person)

# Доступ к значениям
print(person["first_name"])
print(person["age"])

#example number 2
a = 10       # int
b = 3.14     # float
c = 2 + 3j   # complex

print(type(a))
print(type(b))
print(type(c))

#example number 3
num = 7
pi = 3.1415
comp = 1 + 2j
name = "Python"

print(type(num))   # <class 'int'>
print(type(pi))    # <class 'float'>
print(type(comp))  # <class 'complex'>
print(type(name))  # <class 'str'>


#string

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"



#example
word = "Programming"

print(word[0])   # первый символ → 'P'
print(word[3])   # четвертый символ → 'g'
print(word[-1])  # последний символ → 'g'

# Срезы
print(word[0:6])  # символы с 0 по 5 → 'Progra'
print(word[3:])   # с 3 до конца → 'gramming'
print(word[:6])   # с начала до 5 → 'Progra'
print(word[-6:-1])# с конца → 'ammin'

#2example
name = "python"

print(name.upper())   # 'PYTHON'
print(name.lower())   # 'python'
print(name.title())   # 'Python'

