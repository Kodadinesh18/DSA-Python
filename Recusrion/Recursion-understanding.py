'''
recursion is nothing but calling a function itself within the same function
if we didnt mention base case-it will go to infinite function 
need to mention a base case for every recursive function 

syntax:

def function_name(parameter1,parameter2...):
    if(base-condition:)
        return

        //task or job to be performed
        calling the function again-func(parameters)

'''

#two methods- head recursion,tail recursion /back-tracking

#head recursion:
def printName(name,n):
    if n==0:
        return
    print(name)
    printName(name,n-1)

printName("dinesh",5)
#here we are doing or job first and then we are calling the function!


#tail method or back tracking:
def printName2(name,n):
    if n==0:
        return
    printName2(name,n-1)
    print(name)

printName2("deepak",6)
#here we are calling the function first and then our task


