#math
import math

degree = 15
radian = degree * math.pi / 180

print(degree)
print(round(radian, 6))


height = 5
base1 = 5
base2 = 6

area = 0.5 * height * (base1 + base2)

print(area)   



import math

n = 4
side = 25

area = (n * side ** 2) / (4 * math.tan(math.pi / n))

print(int(area))


base = 5
height = 6

area = base * height

print(float(area))
