#what is arm strong number??
#sum of indivdual digits ** total_digitscount
#should be equal to the number then it is called as arm strong number

#for eg: 153 number:153 digits:3 so 1**3 + 5**3 + 3**3= 153 so it is a arm strong number

#code for arm strong number:

number=153
n=number
total=0
digits=len(str(n))

while(n>0):
    last_digit=n%10
    total+=last_digit**digits
    n=n//10

print(total)//153

