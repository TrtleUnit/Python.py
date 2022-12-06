import random
min_val = 1
max_val = 6
roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
        print ("Rolling the dices...")
        print ("The value are...")
        print (random.randint(min, max))
        print (random.randint(max, min))
        
        roll_again = input("Rol het dobbelsteen nog een keer?")
   
