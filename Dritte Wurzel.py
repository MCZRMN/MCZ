z = int(input("Z EINGEBEN"))

xalt = 10000000
for i in range(300):

    xneu = (2*xalt + z/xalt**2) / 3
    xalt = xneu
print(xneu)