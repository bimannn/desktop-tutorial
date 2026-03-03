text = "Hello world"

match = re.match(r"Hello", text)
print(match.group())  # Hello

#output:
#Hello

#example 
import re
txt = "The rain in Spain"
x = re.match("The", txt)
if x:
  print("Yes! We have a match!")
else:
    print("No match")

#output:
#Yes! We have a match!