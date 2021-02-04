# we gonna sum anythink with th ehelp of eval function knows as a evaluate
ope =True
while ope:
     
    print("type quit to exit")
    preexpress=input("enter the dgits on which you wan to apply mathematical operationwant with signs" "\n" "like 454+/5454*23453-4565=  ")
    print(preexpress)
    if preexpress=="quit":
        break
    else:
        print(" this the solution of the expression you typed ")
        presolve=eval(preexpress)
        print(presolve)
        print("enter the expression " ,presolve ," + ")
        
        answer=input(" Do you want to change '-','*','/'")
        if answer=="yes":
            operat=input("enter the operator : ")
            if operat=="-":
                print("enter the value " ,presolve , operat)
                newexpress=input()
                newsolve=eval(newexpress)
                final=presolve - newsolve
                print(final)

            elif operat=="*":
                print("enter the value " ,presolve , operat)
                newexpress=input()
                newsolve=eval(newexpress)
                final=presolve * newsolve
                print(final)

            elif operat=="/":
                print("enter the value " ,presolve , operat)
                newexpress=input()
                newsolve=eval(newexpress)
                final=presolve / newsolve
                print(final)

        else:
            print("enter the value " ,presolve , "+")
            newexpress=input()
            newsolve=eval(newexpress)
            final=presolve + newsolve
            print(final)
            


