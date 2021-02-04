class A:
    def __init__(self):
        print("this is init of A")

    def feature1(self):
        print("this is feature 1-A")


class B:
    def __init__(self):
        super().__init__()            # calling the init of A class
        print("this is init of B")
    def feature1(self):
        print("this is feature 1-B")

class C(A,B):                   # constructor call from left to right
    def __init__(self):
        super().__init__()
        super().feature1()       # calling from super
        print("init of C")
        
        

# b = B()                # this is constructor
c = C()
c.feature1()

'''
contructor follow the method resolution order in which it call firswtly the function from left to right
'''


"""
if there is no consturctor in a subcalss then object will go for parent class init
"""