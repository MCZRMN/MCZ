#Aufgabe 2(2)

x = int(input("Zahl eingeben"))
v = x
while v != 0:
    if x%v == 0:
        print(v)
    v -= 1