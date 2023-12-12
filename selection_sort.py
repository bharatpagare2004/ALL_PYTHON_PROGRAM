# program for selection sort
"""
marks = [78,45,23,65,78]
def selection_sort(marks):
    for i in range(len(marks)):
        mid_index = i
        for j in range(i+1,len(marks)):
            if marks[mid_index] > marks[j]:
                mid_index = j
        marks[i],marks[mid_index] = marks[mid_index],marks[i]



    for i in range(len(marks)):
        print(marks[i])           


selection_sort(marks)"""

marks = []
n = int(input("enter the time:"))
for i in range(n):
    marks1 = int(input("enter the element:"))
    marks.append(marks1)

# for selection sort
def selection_sort(marks):
    for i in range(len(marks)):
        mid_index = i
        for j in range(i+1,len(marks)):
            if marks[mid_index]>marks[j]:
                mid_index = j
        marks[i],marks[mid_index] = marks[mid_index],marks[i]


    for i in range(len(marks)):
        print(marks[i])  

selection_sort(marks)                  
