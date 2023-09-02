# this things are display for information...   
print("This is First Assignment.")
print("This is Menu Driven program.")
print("The student gets the marks in fds test.")
m11=[67,90,67,90,34,56]
print(m11)
print(     "    ##############################    "      )
# this is choice section.
print("this is choice Section")
print("1.higest marks.")
print("2.lowest marks.")
print("   ##################    ")
# this program for marks evalution..
# this is first function...
m= [67,90,67,90,34,56]
m1=max(m)
# this is second function...
n= min(m)


while(True):
 ch = int(input("enter your choice:  "))
 if ch == 1:
     print("this highest marks = ",m1)
     print("@@@@@@@@@@@@@@")

     
 elif ch == 2:
     print("this is lowest marks = ",n)
     print("@@@@@@@@@@@@@@") 


 elif ch == 3:
     print("this is a invalid choice. ")
     print("@@@@@@@@@@@@@@")


 else:
     print("exit") 