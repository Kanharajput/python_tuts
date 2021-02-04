# DEFINATIOM OF THE FUNCTIONS
global order # main think it take my 2 hours in an error nameerror
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    return a/b
 

def operation():    
    if order=="add":
        value=add(number1,number2) 
        print("here is the sum " , value)

    elif order=="sub":
        value=subtract(number1,number2) 
        print("here is the subtract " , value)

    elif order=="mul":
        value=multiply(number1,number2) 
        print("here is the multiply " , value)

    elif order=="div":
        value=division(number1,number2) 
        print("here is the dividion " , value)

    
    else:
        print("not defined maths ke akka ", order ,"rules konsa hai")
        



print("welcome to kanha's calculator")
print("what you want add,subtract,multiply,division:")
print("enter in form of add,sub,mul,div")                # TAKING CHOICES AND VAKUES



#if order=="add" or "subtract" or "multiply":
    #print("kya ker raha hai")                     #print not working here

kanha=True
while kanha:
    print("type quit to exit")
    order=str(input("please type your marji:  "))
    if order=="quit":
        kanha=False
    
    else:
        number1=int(input("enter the first number:  "))
        number2=int(input("enter the second number:  "))
        operation()

    


'''    
else:
    print("first number should be larger")          #print not working here
    number1=int(input("enter the first number , first no. should be larger"))
    number2=int(input("enter the second number"))
'''

