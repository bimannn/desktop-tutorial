import re

text = "hello_world test_case Wrong_Test"

result = re.findall(r"\b[a-z]+_[a-z]+\b", text)
print(result)