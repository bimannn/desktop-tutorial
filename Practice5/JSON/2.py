import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
# Output: {"name": "John", "age": 30, "city": "New York"}

#example
import json 
x = {
  "name": "Alice",
  "age": 25,
  "city": "Los Angeles"
}
y = json.dumps(x)
print(y)
# Output: {"name": "Alice", "age": 25, "city": "Los Angeles"}   
