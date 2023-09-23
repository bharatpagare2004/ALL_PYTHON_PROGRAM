# this program for simple menu driven.
a =int(input("enter the value of a : "))
b = int(input("enter the value of b: "))
def sum():
    c = a+b
    print("the addition is : ",c)
def sub():
    c1 = a-b
    print("the sub is :",c1)
    
bharat = 1
while bharat ==1:
    print("@@@@@@@ this is menu driven program @@@@@@@")
    print("1 . perform addition of two number.")
    print("2. perform substraction of two number.")
    print("this is end of program")
    ch = int(input("enter the choice:"))
    if ch ==1:
     sum()
    elif ch ==2:
     sub()
    elif ch ==3:
       print("wrong choice")
    else:
       break