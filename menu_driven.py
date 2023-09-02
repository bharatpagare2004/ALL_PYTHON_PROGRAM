# This program for arithmatic operation .
# this is menu driven program.
print("@_THIS IS ARITHMATIC OPRATION PROGRAM_@")
print("#_This is Menu_Driven program_#")
print(      "@@@@@@@@@@@@@@@@@@@@@@@@@@@@"       )
# this code used for choice section.
print("@_THIS IS CHOICE SECTION_@")
print("1.Addition.")
print("2.Substraction.")
print("3.Multiplication.")
print("4.Division.")
print("5.Exit.")
print(      "_@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@_"    )
# this is taking input form user...
a= int(input("enter a value of a: "))
b= int(input("enter a value of b: "))

def sum():
    """this operation for summation."""
    c= a+b
    return c
    
def sub():
    """this operation for substraction."""
    r= a-b
    return r

def mult():
    """this operation for multiplication."""
    m= a*b
    return m 

def div():
    """this operation for division."""
    y= a/b
    return y
    
while(True):
    ch = int(input("enter your choice no : "))
    if ch == 1:
        print("the addition is = ",sum())
        
    elif ch ==2:
        print("the substraction is = ",sub())
        
    elif ch == 3:
        print("the multiplication is =",mult())
        
    elif  ch == 4:
        print("the division is = ",div())
    elif ch == 5:
     exit
    else:
        print("please enter a valid choice.")