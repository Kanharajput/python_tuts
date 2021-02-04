class A:
    def feature1(self):
        return "this is feature 1"

class B(A):
    def feature2(self):
        return "this is feature 2"

class C(B):
    def feature3(self):
        return "this is feature 3"


# multilevel one function one by one get all the functions    
obj1 = C()
print(obj1.feature1())
print(obj1.feature2())
print(obj1.feature3())
