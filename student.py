# first assignment.
# 1) average score of the class.
# 2) highest score in the class.
# 3) lowest score in the class.
# 4) count absent student for the test.
# 5) display the mark with highest frequency.

# calculating highest marks
def average(l): # always end with :
    sum = 0
    count = 0
    for i in range(len(l)):
        if l[i] != -1:
            sum +=l[i]
            count +=1
    avg = sum /count
    print("total marks is :",sum)
    return(avg)

# for highest marks 
def high(l):
    Max = l[0]
    for i in range(len(l)):
         if l[i]>Max:
             Max = l[i]
    return(Max)

def low(l):
     for i in range(len(l)):
          if [i] != -1:
               Min = l[i]
               break
     for j in range(i+1,len(l)):
          if l[j] !=-1 and l[j]<Min:
               Min = l[j]
     return(Min) 
def absent(l):
     cnt = 0
     AB = -1
     for i in range(len(l)):
          if l[i] ==-1:
                
               cnt +=1
     return(cnt)  


def Maxf(l):

   i =0
   Max = 0
   print("marks for frequency count: ")
   for ele in l:
      if l.index(ele) == i:
         print(ele,"--->",l.count(ele))
         if l.count(ele)>Max:
            Max = l.count(ele)
            mark = ele
            i +=1
      return(mark ,Max)             
                  

          
marks_in_fds = []
n = int(input("enter how many student marks you want to fill up:"))
for i in range(n):
    marks =int(input("enter the marks,FOR(ABSENTS_STUDENT = -1):"+str(i+1)+":"))
    marks_in_fds.append(marks)
     
# imp statement for menu driven program.
b = 1
while b ==1:
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("menu_driven")
    print("1.average_marks") 
    print("2.highest_marks")
    print("3.lowest_marks")
    print("4.absent student count")
    print("5.marks with highest frequency")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    ch = int(input("enter your choice: "))

    if ch == 1:
            print("the average marks is : ",average(marks_in_fds))
    elif ch ==2:
         print("the highest marks is : ",high(marks_in_fds))
    elif ch ==3:
         print("the lowest marks is:",low(marks_in_fds)) 
    elif ch ==4:
         print(" the absent student in the class:",absent(marks_in_fds))
    elif ch ==5:
         print("the marks with highest frequency",Maxf(marks_in_fds))        
    else:
         break             