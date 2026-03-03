import re

pattern = r"ab{2,3}"

text = "abb"
print(bool(re.fullmatch(pattern, text)))