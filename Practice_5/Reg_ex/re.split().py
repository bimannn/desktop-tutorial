import re

#Split the string at every white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
#Output:
#['The', 'rain', 'in', 'Spain']



#example
import re
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
#Output:
#['The', 'rain in Spain']
