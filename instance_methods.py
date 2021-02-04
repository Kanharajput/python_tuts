#### instance methods
#### method == functon
class test:
    def __init__(self,value1,value2):    
        self.val1 = value1
        self.val2 = value2
 
                                             
    def avr(self):                                  
        return(self.val1+self.val2/2)


    def get_value1(self):                # accessor method  or getter
        return self.val1


    def set_value2(self,it):               # mutator method
        self.val2 = it
        return(self.val2)



obj = test(78,89)
print(obj.avr())
print(obj.get_value1())               
print(obj.set_value2(10))

