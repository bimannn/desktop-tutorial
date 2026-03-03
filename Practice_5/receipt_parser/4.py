import re

text = "Hello World TEST"

result = re.findall(r"\b[A-Z][a-z]+\b", text)
print(result)