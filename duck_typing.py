class water:
    def walking(self):
        print("duck is walking and swiming")
        
    
class land:
    def walking(self):
        print("duck is walking")



class legs:
    def duck(self,place):
        place.walking()



place = land()
obj_legs = legs()
obj_legs.duck(place)