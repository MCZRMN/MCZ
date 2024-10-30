# S.1 A1
import random

def Summe():
    Zahl = int(input("Zahl eingeben"))
    temp = 0
    for i in range(Zahl+1):
        temp += i
    print(temp)
    return

def AusgabeZiffer():
    Zahl1 = input("Zahl eingeben")
    temp = 0
    for i in Zahl1:
        temp +=1
        print("Ziffer",temp,":      ",i)

    return



def CountZero():
    Zahl2 = input("Zahl eingeben")
    temp = 0
    for i in Zahl2:
        if i == "0":
            temp+=1
    print(temp)


def CountA():
    String = input("Zahl eingeben")
    temp = 0
    for i in String:
        if i == "a":
            temp+=1
    print(temp)


def Random7():
    temp = 0

    for i in range(100):
        Zahl3 = random.randint(0,100)
        if Zahl3%7 == 0:
            temp+= 1

    print(temp)


def StringtoASCIICode():
    String = input("String eingeben")
    Liste = []
    for i in String:
        Liste +=[ord(i)]
    print(Liste)


def RandomStats():
    Liste = []
    Anzahl = int(input("Anzahl der generierten Zahlen eingeben"))
# Liste erstellen
    for i in range(Anzahl):
        n = random.randint(0,100)
        Liste += [n]

# Durchscnitt berechnen
    temp = 0
    for j in Liste:
        temp += j

    temp = temp/Anzahl

# Max ausrechenen
    Max = 0
    for k in Liste:
        if k > Max:
            Max = k


# Min ausrechenen
    Min = 100
    for l in Liste:
        if l < Min:
            Min = l




    print("Entstandende Liste:",Liste)
    print("Durchschnittlischer Zahlenwert:",temp)
    print("Min:",Min)
    print("Max:",Max)


def Whatsapp():
    n = input("Gewollter String")
    for i in range(101):
        print(i,". ",n)




# Hauptprogramm

#Summe()
#AusgabeZiffer()
#CountZero()
#CountA()
#Random7()
#StringtoASCIICode()
#RandomStats()
Whatsapp()


