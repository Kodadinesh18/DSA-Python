#finding factors: the numbers which are divisble within 1 to the number to the number

#brute force method:
result=[]
def factors(number):
    for i in range(1,number+1):
        if (number%i)==0:
            result.append(i)
    return result

print(factors(20))#[1, 2, 4, 5, 10, 20]

#better solution:
#we dont need to traverse fully. we can get factors by iterating over half the number

n=120
result2=[]
#we need to traverse only till 60

def factors2(number2):
    for i in range(1,number2//2):
        if number2%i==0:
            result2.append(i)
    result2.append(number2)
    return result2

print(factors2(120))
#[1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 120]


#3.optimal solution:
from math import sqrt

result3 = []
number3 = 36

for i in range(1, int(sqrt(number3)) + 1):
    if number3 % i == 0:
        result3.append(i)
        if number3 // i != i:  # avoid duplicate for perfect squares
            result3.append(number3 // i)

result3.sort()
print(result3)





