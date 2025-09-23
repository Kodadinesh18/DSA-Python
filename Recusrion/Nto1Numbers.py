#printing values n to 1 eg:10,9,8,7,6,5,4,3,2,1
#it can also be done by 
#1.head recusrion 
#tail recursion/ backtracking

#head recursion:

def printNumbers(n,i):
    if n<i:
        return
    print(n)
    printNumbers(n-1,i)

printNumbers(10,1)


#tail recursion/back-tracking:

def printNumbers2(n,i):
    if (i>n):
        return
    printNumbers2(n,i+1)
    print(i)

printNumbers2(10,1)
