import re

pattern = r"a.*b"

text = "aXYZ123b"
print(bool(re.fullmatch(pattern, text)))