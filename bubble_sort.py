# this program for selection sort and bubble sort
marks = []
n = int(input("enter the time:"))
for i in range(n):
   marks1 = int(input("enter the marks:"))
   marks.append(marks1)



def selection_sort(marks):
    for i in range(len(marks)):
        mid_index = i
        for j in range(i+1,len(marks)):
            if marks[mid_index]>marks[j]:
                mid_index = j
        marks[i],marks[mid_index] = marks[mid_index],marks[i] 

    print("selection sort:")
    for i in range(len(marks)):
        print(marks[i])

                   

def bubble_sort(marks):
    n = len(marks)
    for i in range(n-1):
        for j in range(n-i-1):
            if marks[j]>marks[j+1]:
               marks[j],marks[j+1]= marks[j+1],marks[j]

    print("bubble_sort")           
    for i in range(len(marks)):
        print(marks[i])           
def top_five(marks):
    for i in range(n-1,n-6,-1):
        print(marks[i])
    



while(1):
    print("\n 1.selection sort")
    print("\n 2.bubble sort")
    print("\n 3.print top five element")
    print("\n 4.exit")

    ch = int(input("enter the choice:"))

    if ch ==1:
        selection_sort(marks) 
    elif ch == 2:
        bubble_sort(marks) 
    elif ch == 3:
        top_five(marks)
    elif ch == 4:
        exit(0)

