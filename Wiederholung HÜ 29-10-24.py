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


# Hauptprogramm

#Summe()
#AusgabeZiffer()
#CountZero()
#CountA()
#Random7()


