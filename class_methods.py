class your_wise:
    kanha = 100
    rajput = 50
    @classmethod
    def get_class_var(cls):      # like objects it also have it' own space to change it 
        print("before changing :", cls.kanha)
        cls.kanha = 50 
        print("after changing" ,str(cls.kanha))       
        return ''
        
    def get_var(self):
        return self.kanha

    def set_class_var(self,value):           
        self.kanha = value
        return self.kanha
 
my_wise = your_wise()
print(your_wise.get_class_var())   
print(my_wise.get_var)
print(my_wise.set_class_var(50))
print(your_wise.get_class_var())