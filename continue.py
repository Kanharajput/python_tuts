import random


value1=130
value2=10
value3=20
while value1>0:
    minus=random.randrange(value2,value3)
    value1=value1-minus
    print("you damaged the player by " , minus)
    print("power bachi huyi", value1)

    if value1<=1:
        value1=0


    if(value1<=10):
        continue   # it will change the flow of contol, read to top most of the loop 
        print("you lose the game ")
        print("better luck next time")
        


    if value1>=11 and value1<=30:
        print("you need to go to hospital")
    
    
    else:
        print("hurry up! your power is decreasing")

