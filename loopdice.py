import random

hoeveel = input("Hoeveel dobbelstenen wilt u rollen?")
repeat = "Y"

while repeat == "Y":

    print("Het resultaat:")
    print(random.randint(1,6))

    repeat =input("Do you wanna roll again Y/N?")
    if repeat == "Y": continue
    if repeat == "N": break
    else: print ("Deze functie werkt niet. Begin opnieuw.")
    
    
    