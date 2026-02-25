import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
# Output: 30


#example
import json
x =  '{ "name":"Alice", "age":25, "city":"Los Angeles"}'
y = json.loads(x)   
print(y["name"])
# Output: Alice