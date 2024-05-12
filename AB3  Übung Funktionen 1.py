# Summenberechnung

def Variablenbestimmung():

    a = int(input("Bitte ganze positive Zahl eingeben"))
    while a<0:
        a = int(input("Bitte ganze positive Zahl eingeben"))

    s1 = 0
    s2 = 0
    return a, s1, s2


def Berechnung(a, s1, s2):
    for i in range(1, 11, 2):

        if a % i == 0:
            s1 += 1
        else:
            s2 += 1
    return s1, s2

def Ausgabe(s1, s2):
    print(s1, s2)


# Hauptprogramm

a, s1, s2 = Variablenbestimmung()
s1, s2 = Berechnung(a, s1, s2)
Ausgabe(s1, s2)

# Programm teilt eingegebene Zahl durch 1,3,5,7,9 wenn ohne rest Teilbar dann s1 += 1 wenn nicht dann s2 += 1