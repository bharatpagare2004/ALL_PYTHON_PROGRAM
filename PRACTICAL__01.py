#python practical program.
def AVG_MARK(l):
    sum = 0
    cnt = 0
    for i in range(len(l)):
        if l[i]!=-1:
         sum +=l[i]
         cnt+=1
    avg = sum/cnt
    print("total marks are:",sum )
    return(avg)


def HIGH_MARK(l):
    Max = l[0]
    for i in range(len(l)):
       if l[i]>Max:
          Max = l[i]
    return(Max)


def LOWEST_MARK(l):
    for i in range(len(l)):
     if[i] != -1:
        Min =l[i]
        break
    for j in range(i+1,len(l)):
       if l[j] != -1 and l[j]<Min:
          Min = l[j]
    return(Min)
       

def  ABSENT(l):
   cnt = 0 
   for i in range(len(l)):
      if l[i]  ==-1 :
       cnt +=1
   return(cnt)
      
      
def MAX_FRE(l):
   i=0
   Max = 0 
   print("marks for frequency count")
   for ele in l:
      if l.index(ele)==i:
         print(ele,"--->",l.count(ele))
         if l. count(ele)>Max:
            Max = l.count(ele)
            mark = ele
            i +=1
      return ( mark,Max)
   
MARKS_IN_FDS = []
NO_Student = int(input("enter a number of student: "))
for i in range(NO_Student):
   
      marks =  int(input("enter a student marks: " +str(i+1)+":"))
      MARKS_IN_FDS.append(marks)
                            
KALPESH = 1
while KALPESH ==1:
        print("&&&__MENU___&&&")
        print("************************")
        print("(1). THE AVERAGE SCORE OF CLASS.")
        print("(2). THE HIGHEST SCORE OF CLASS.")
        print("(3). THE LOWEST SCORE OF CLASS.")
        print("(4). THE COUNT OF ABSENT STUDENT.")
        print("(5).  DISPLAY MARK WITH HIGH FREQUENCY.")
        print("(6). exit.")
   # this for choice ...
        choice = int(input("enter your choice : "))
        if  choice == 1:
            print( "the average marks is :",AVG_MARK(MARKS_IN_FDS))
           
        elif choice ==2 :
            print("the highest mark is  = ",HIGH_MARK(MARKS_IN_FDS))
        elif choice == 3:
            print("the lowest is = ",LOWEST_MARK(MARKS_IN_FDS))
        elif choice == 4:
           print("the absent student in the class is = ",ABSENT(MARKS_IN_FDS))
        elif choice == 5:
           print("marks with high frequency is = ",MAX_FRE(MARKS_IN_FDS))
        elif choice == 6:
             print("you are successfully exit  ")
             break
        else:
             print("wrong choice ")        
     
             