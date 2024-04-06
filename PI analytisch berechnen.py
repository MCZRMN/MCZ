import random
import math
import matplotlib.pyplot as plt



trycount_str = input("Number of attempts")
trycount = int(trycount_str)

hitx    = []
nothitx = []

hity    = []
nothity = []


hit = 0
nothit = 0

for i in range(trycount):
    x=random.uniform(0.0, 1.0)
    y=random.uniform(0.0, 1.0)

    if (x * x + y * y) <= 1:
        hit += 1
        hitx.append(x)
        hity.append(y)
    else:
        nothit += 1
        nothitx.append(x)
        nothity.append(y)

pi = 4*((hit)/(trycount))

Error = pi - math.pi

print("")
print("")
print("trycount   =",trycount)
print("hit        =",hit)
print("nothit     =",nothit)
print("Pi         =",pi)
print("Error      =",Error)
print("deviation  =",Error/math.pi*100,"%")

#graphic

plt.plot(nothitx,nothity,y,color='none',linestyle='dashed',linewidth = 2, marker= 'o', markersize=3,markerfacecolor='red' , markeredgecolor ='red')
plt.plot(hitx,hity,color='none',linestyle='dashed',linewidth = 2, marker= 'o', markersize=3,markerfacecolor='green' , markeredgecolor ='green')

plt.grid()
plt.show()

