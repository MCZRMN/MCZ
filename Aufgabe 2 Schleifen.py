#Aufgabe 2 Schleifen
x = int(input('Gib eine ganze positive Zahl ein.'))
while x > 0 :
 print(x, x**2, x**.5)
 x -= 1


# Zahle,Zahl zum Quatrat, Wurzel
x = int(input('Gib eine ganze positive Zahl ein.'))
for i in range(x):
    print(x, x**2, x**.5)
    x -= 1