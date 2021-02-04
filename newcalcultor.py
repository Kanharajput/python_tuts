print("welcome to kanha's calculator")
print("what you want add,subtract,multiply,division:")

# TAKING CHOICES AND VAKUES

order=int(input("please type your marji in 1=add,2=subtract,3=multiply,4=division"))

if order==add or subtract or multiply:
    number1=int(input("enter the first number"))
    number2=int(input("enter the second number"))

else:
    print("first number should be larger")
    number1=int(input("enter the first number"))
    number2=int(input("enter the second number"))

     
# CALLING OF THE FUNCTIONS

if order==1:
    value=jodna(number1,number2) 
    print("here is the sum " , value)

elif order=="subtract":
    value=subtract(number1,number2) 
    print("here is the subtract " , value)

elif order=="multiply":
    value=multiply(number1,number2) 
    print("here is the multiply " , value)

elif order=="division":
    value=division(number1,number2) 
    print("here is the dividion " , value)


# DEFINATIOM OF THE FUNCTIONS
def jodna(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    return a/b
 
