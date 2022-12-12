import random

repeat = "Y"


while repeat == "Y":
    
    hoeveel = int( input("Hoeveel dobbelstenen wilt u rollen?"))
    for x in range(hoeveel):
        print("Uw resultaat:")
        print(random.randint(1,6))

    repeat =input("Wilt u nog een keer rollen Y/N?")
    if repeat == "Y": continue
    if repeat == "N": break
    else: print ("Deze functie werkt niet. Begin opnieuw.")
    
    