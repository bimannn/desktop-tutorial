import json

print(json.dumps({"name": "John", "age": 30})) # Output: {"name": "John", "age": 30}
print(json.dumps(["apple", "bananas"])) # Output: ["apple", "bananas"]
print(json.dumps(("apple", "bananas"))) # Output: ["apple", "bananas"]
print(json.dumps("hello"))   # Output: "hello"
print(json.dumps(42))    # Output: 42
print(json.dumps(31.76))   # Output: 31.76
print(json.dumps(True))   # Output: true
print(json.dumps(False))    # Output: false
print(json.dumps(None))   # Output: null


import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))
# Output:
# {
#     "name" = "John".
#     "age" = 30.
#     "married" = true.
#     "divorced" = false.
#     "children" = [
#         "Ann",
#         "Billy"
#     ].
#     "pets" = null.
#     "cars" = [
#         {
#             "model" = "BMW 230".
#             "mpg" = 27.5
#         },
#         {
#             "model" = "Ford Edge".
#             "mpg" = 24.1
#         }
#     ]
# }


#example
import json
x = {  
    "name": "Alice",
    "age": 25,
    "married": False,
    "divorced": True,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
        {"model": "Audi A4", "mpg": 27.5},
        {"model": "Mercedes C-Class", "mpg": 24.1}
    ]
    }
