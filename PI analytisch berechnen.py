import random
import math


trycount_str = input("Number of attempts")
trycount = int(trycount_str)

hit = 0
nothit = 0

for i in range(trycount):
    x = random.uniform(0.0, 1.0)
    y = random.uniform(0.0, 1.0)
    #print(f"{x}, {y}")
    # if (x**2 + y**2)**0.5 <= 1:
    if (x * x + y * y) <= 1:
        hit += 1
    else:
        nothit += 1

pi = 4*((hit)/(trycount))


print("")
print("")
print("trycount =",trycount)
print("hit      =",hit)
print("nothit   =",nothit)
print("Pi       =",pi)
print("Error    =",abs(pi - math.pi))