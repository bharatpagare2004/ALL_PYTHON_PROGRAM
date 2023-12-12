# this program for selection sort
marks =[]
n = int(input("enter the time:"))
for i in range(n):
    m = int(input("enter the marks:"))
    marks.append(m)


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