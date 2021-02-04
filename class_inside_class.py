class student:
    def __init__(self,name,roll_number):
        self.name = name
        self.roll_number = roll_number
        self.s3 = self.info_student("Barda")     # declare object inside the class

    class info_student:
        def __init__(self,vill_name):
            self.vill_name = vill_name

        def village_name1(self):
            return self.vill_name

        def village_name(self):
            return "barda"

    def show(self):
        print(self.name,self.roll_number)

s1 = student("kanha",90)
s1.show()                       # if we use double se print it will show none
s2 = student.info_student("barda")                # declare object outside the class
print("village name" , s2.village_name())
s4 = s1.s3
print("village name from inside object",s4.village_name1())