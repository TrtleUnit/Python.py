
#Rekenmachine
import math
Getal1 = float(input("Voer uw eerste getal in: "))
Bewerking = (input ("Welke bewerking wilt u uitvoeren"))
Getal2 = float(input("Voer uw tweede getal in: "))

if Bewerking == "+":
    print(Getal1 + Getal2)
    
elif Bewerking == "-":
    print(Getal1 - Getal2)
    
elif Bewerking == "x":
    print(Getal1 * Getal2)

elif Bewerking == ":":
    print(Getal1 / Getal2)

antwoord = Getal1 + Bewerking + Getal2
print (antwoord)
