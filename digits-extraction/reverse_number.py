#reversing a number:

number=1234
n=number
reversed=0

while(n>0):
    last_digit=n%10
    reversed=(reversed*10)+last_digit
    n=n//10

print(f"Reversed number is: {reversed}")
#Reversed number is: 4321

#checking wheather it is palindrome or not?

if(reversed==number):
    print("it is a palindrome number")
else:
    print("it is not a palindrome number")