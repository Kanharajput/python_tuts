class  A():
    def feature1(self):
        return "feature 1 is inherit by both the classes"

    
class B(A):
    def feature2(self):
        return "this is only inherit by own class , B calss featue"


class C(A):
    def feature3(self):
        return "this is only inherit by own class , C calss featue"


# every sub classs inherit the behavior of paent class 
obj1 = B()           # object of b class
print("features by B class")
print(obj1.feature1())
print(obj1.feature2())
obj12 = C()
print("feature by c class")
print(obj12.feature1())
print(obj12.feature3())
