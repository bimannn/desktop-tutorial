import re

#Return a list containing every occurrence of "ai":

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
#Output: 
#['ai', 'ai']


#example
import re
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)
#Output: 
#[]
