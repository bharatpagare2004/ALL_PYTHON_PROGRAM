list = []
n = int(input("enter the numbre of student you want to fill up marks:"))
for i in range(n):
     marks = int(input("enter the marks:"))
     list.append(marks)


def max_marks_student():
     m =max(list)
     print("max marks is:",m)
     y = min(list)
     print("min marks is :",y)


# for average
def average(list,n):
    sum1 = sum(list)
    avg = sum1 /n
    print("average is :",avg)

while(True):

  def menu():
     print("1.max and min marks")
     print("2.average marks")
     print("3.exit")

     ch = int(input("enter your choice:"))
     if(ch ==1):
      print(max_marks_student())
    
        
     elif(ch ==2):

      print("this is average marks:",average(list,n)) 

     elif(ch== 3):
         print("you are successfully exit")
         exit(0)   

     
  menu()
