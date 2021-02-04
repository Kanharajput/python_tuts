class work:
    def __init__(self,a,b):
        self.a  = a
        self.b = b

    def __add__(self,other):
        a = self.a + other.a
        b = self.b + other.b
        obj3 = work(a,b)
        return obj3

obj1 = work(50,20)
obj2 = work(110,50)
obj3 = obj1 + obj2
print(obj3.a)