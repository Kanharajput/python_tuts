import random


class this:
    def __init__(self,inpwr):                                # instance variable
        self.inpwr=inpwr 
  


    def func(self,atk):
        self.atk=atk
        print("attck deacrease your health to ",(self.inpwr-self.atk))
        inpwr=self.inpwr-self.atk

        if inpwr <= 0:
            print("you lose the game :)")


        else:
            print("yeh bencho apni g... bacha ")

        return inpwr


pwr=100  
that = this(pwr)
while pwr>0:
    enemy_atk = random.randrange(0,100)
    print("Enemy atacks with power" ,enemy_atk)
    pwr = that.func(enemy_atk)
    # print(plyr1inpwr)
    if pwr <=0:
        print("you lose the game babe")
        break