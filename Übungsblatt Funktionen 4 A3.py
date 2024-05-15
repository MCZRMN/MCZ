
def Spiegeln(pZahl):
     Ergebnis = 0
     Rest = pZahl
     Zahl = pZahl
     while Rest > 0:
         Rest = Zahl // 10
         Ziffer = Zahl % 10
         Ergebnis = 10 * Ergebnis + Ziffer
         Zahl = Rest
     return Ergebnis



pZahl = int(input("B Eingeben"))
Ergebnis = Spiegeln(pZahl)
print(Ergebnis)