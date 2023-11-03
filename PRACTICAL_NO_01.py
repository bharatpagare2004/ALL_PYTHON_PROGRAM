# this program is first practical of fds subject.
# a) average score of class.
# b) higest score and lowest score of class.
# c) count of student who were absent for the test.
# d) display mark with highest frequency.

# this all codition we want perform.
# we write user defined function for calculate average score of class.
def average_marks(l):
    sum = 0
    cnt = 0
    for i in range(len(l)):
        if l[i]!=-1:
         sum +=l[i]
         cnt+=1
    avg = sum/cnt
    print("total marks are = ",sum )
    return(avg)
# we write user defined function for calculate the highest score in class.
def highest_mark(l):
    Max = l[0]
    for i in range(len(l)):
       if l[i]>Max:
          Max = l[i]
    return(Max) 

# we write user defined function for calculate the lowest score in class.
def lowest_mark(l):
    for i in range(len(l)):
     if[i] != -1:
        Min =l[i]
        break
    for j in range(i+1,len(l)):
       if l[j] != -1 and l[j]<Min:
          Min = l[j]
    return(Min)
          
  # we write user defined function for calculate the how many student absent in test.
def absent(l):
   cnt = 0 
   for i in range(len(l)):
      if l[i]  ==-1 :
       cnt +=1
   return(cnt)
# display  mark with highest frequency
def maxFre(l):
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
                            
        

# taking no of student and their marks.
MARKS_FDS_SUBJECT = []
NO_STUDENT = int(input("enter a number of student = "))
for i in range(NO_STUDENT):
   marks =  int(input("enter a student marks = " +str(i+1)+":"))
   MARKS_FDS_SUBJECT.append(marks)



BHARAT = 1
while BHARAT ==1:
         print("@@@@@_THIS IS MENU_@@@@@")
         print("@@@@@@@@@@@@@@@@@@@@@@@@")
         print("(1). the average score of class.")
         print("(2). the highest score of class.")
         print("(3). the lowest score of class.")
         print("(4). the count of absent student of class.")
         print("(5). the marks with high frequency.")
         print("(6). exit.")
   # this for choice ...
         choice = int(input("enter your choice : "))
         if choice == 1:
            print( "the average marks is :",average_marks(MARKS_FDS_SUBJECT))
           
         elif choice ==2 :
            print("the highest mark is  = ",highest_mark(MARKS_FDS_SUBJECT))
         elif choice == 3:
            print("the lowest is = ",lowest_mark(MARKS_FDS_SUBJECT))
         elif choice == 4:
           print("the absent student in the class is = ",absent(MARKS_FDS_SUBJECT))
         elif choice == 5:
           print("marks with high frequency is = ",maxFre(MARKS_FDS_SUBJECT))
         elif choice == 6:
           print("you are successfully exit  ")
           break
         else:
            print("wrong choice ")