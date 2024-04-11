# Aufgabe 3 Schleifen Primzahl

x = int(input("Natürliche Zahl eingeben"))
print(x)

v1 = x-1
rest = x % v1

while rest != 0:
    rest = x % v1
    v1 -= 1



if v1 == 0:
    print("Primzahl")

elif v1 != 1:
    print("Keine Primzahl")