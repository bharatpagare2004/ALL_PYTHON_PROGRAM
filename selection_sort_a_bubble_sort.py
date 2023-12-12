# selection sort and bubble sort
marks = []
n = int(input("enter how many times you want to add marks:"))
for i in range(n):
    ma = int(input("enter the marks:"))
    marks.append(ma)

 # for selection sort
def selection_sort(marks):
    for i in range(len(marks)):
        mid_index = i
        for j in range(i+1,len(marks)):
            if marks[mid_index]>marks[j]:
                    mid_index = j
        marks[i],marks[mid_index] = marks[mid_index],marks[i]
    print("selection sort")    
    for i in range(len(marks)):
         print(marks[i])
selection_sort(marks) 


def bubble_sort(marks):
    n = len(marks)
    for i in range(n-1):
          for j in range(n-i-1):
               if marks[j]>marks[j+1]:
                  marks[j],marks[j+i]= marks[j+1],marks[j]
    print("bubble sort")               
    for i in range(len(marks)):
          print(marks[i])
bubble_sort(marks)






        