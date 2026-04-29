#for loops
total = 0

for i in range(1, 11):
    total += i   #add current value of i to total

print("Sum:", total) #
#output: Sum: 55


product = 1
for j in range(1, 6):
    product *= j  #multiply current value of j to product
print("Product:", product) 
#output: Product: 120

# Skip number 3 continuing the loop
for i in range(1, 6):
    if i == 3:
        continue   # skip this step
    print(i)
#output: 1 2 4 5

#break loop
for k in range(1, 6):
    if k == 4:
        break   # exit the loop
    print(k)
#output: 1 2 3


