import re

pattern = r"ab*"

text = "abbb"
print(bool(re.fullmatch(pattern, text)))