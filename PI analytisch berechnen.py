import random



trycount_str = input("Number of attempts")
trycount = int(trycount_str)

hit = 0
nothit = 0

for i in range(trycount):
    x = random.random()
    y = random.random()
    if (x**2 + y**2)**0.5 <= 1:
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