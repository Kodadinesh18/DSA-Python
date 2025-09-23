#we want to print numbers between 1 to n 
#there are two methods to implement this:

#head recusrion:
#i=starting index,n=until which number
def printNumbers(i,n):
    if i>n:
        return
    print(i)
    printNumbers(i+1,n)

printNumbers(1,10)

#tail or back tracking recusion
def printNumbers2(n):
    if n==0:
        return 
    printNumbers2(n-1)
    print(n)

printNumbers2(5)

