#while loop
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 #output: 1 2 3

  #My example
j = 1
while j <= 10:
    print(j)
    if j == 7:
        break
    j += 1 #output: 1 2 3 4 5 6 7
#my example
k = 1
while k < 10:   
    print(k)
    k += 2  #output: 1 3 5 7 9

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i) #output: 1 2 4 5 6
#My example
m = 0
while m < 10:
    m += 1
    if m == 5:
        continue
    print(m) #output: 1 2 3 4 6 7 8 9 10


i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6") #output: 1 2 3 4 5 i is no longer less than 6

#My example
n = 1
while n <= 5:
    print(n)
    n += 1
else:
    print("n is no longer less than or equal to 5") #output: 1 2 3 4 5 n is no longer less than or equal to 5

