import random
import math
import matplotlib.pyplot as plt



print("")
print("")
print("Pi is calculated using random numbers")
trycount_str = input("Number of attempts [the more the more precise]:")
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


    if (x * x + y * y) <= 1.0:
        hit += 1
        hitx.append(x)
        hity.append(y)

    else:
        nothit += 1
        nothitx.append(x)
        nothity.append(y)

pi = 4*((hit)/(trycount))

Error = pi - math.pi
deviation = format(Error/math.pi*100,".2f")


print("")
print("")
print("trycount   =",trycount)
print("hit        =",hit)
print("nothit     =",nothit)
print("Pi         =",pi)
print("Error      =",Error)
print("deviation  =",deviation, "%")




#graphic:

graphic = input("Would you like a visualization? Could cause Error if [trycount] is too high: ")

if graphic != "yes":
    print("season closed")


else:
    plt.plot(nothitx,nothity,color='none',linestyle='dashed',linewidth = 2, marker= 'o', markersize=3,markerfacecolor='red' , markeredgecolor ='red')
    plt.plot(hitx,hity,color='none',linestyle='dashed',linewidth = 2, marker= 'o', markersize=3,markerfacecolor='green' , markeredgecolor ='green')

    plt.grid()
    plt.show()

