# for selection sort 
def selection(marks):
    for i in range(len(marks)):
        mid_index = i 
        for j in range(i+1,len(marks)):
            if marks[mid_index]>marks[j]:
                mid_index = j


         # swaping of minimum element
        marks[i],marks[mid_index]  = marks[mid_index],marks[i]
    # for printing the marks 
    print("marks of student after performing")
    for i in range(len(marks)):
        print(marks[i])
# for bubble sort 
def bubble_sort(marks):
     n = len(marks )
     for i  in range(n - 1):
         for j in range(n-i-1):
             if marks[j]>marks[j+1]:
                 
                 temp =marks[j]
                 marks[j] = marks[j+1]
                 marks[j+1] = temp
     print("marks of student after performing bubble sort")
     for i in range(len(marks)):
             print(marks[i])         
                    

# for taking input from user 
marks =[]
n = int(input("enter the number of student:"))
for i in range(n):
    mark = int(input("enter the marks :"))
    marks.append(mark)

#selection(marks)
bubble_sort(marks)

    

