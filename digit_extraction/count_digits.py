#Extraction of digits follow these:
#method-1-counting of digits

number=1234

count=0
n=number #store them separately because we need to change them.
while(n>0):
    last_digit=n%10
    print(f"last Digit:{last_digit}")
    n=n//10
    count+=1

print(f"count of digits:{count}")

#method-2: using logn
import math

def count_digit(number):
    return int(math.log10(number)+1)

print(count_digit(number))


