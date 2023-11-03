# accepting percentage form student 
# creating function
def input_percentage():
     percent = []
     number_of_student = int(input("enter the how many student you want take:"))
     for i in range(number_of_student):
          percent1 = int(input("enter the percentage{0}:".format(i+1)))
          percent.append(percent1)
     return percent
#&&&&&&&&&&&&&&&&&&&&&&&&&
# for printing this percentage
def print_percentage(percent):
     for i in range(len(percent)):
      print(percent[i],sep = "\n")

 # for the partition
def partition(percent,s ,end):
    p = percent[s]
    l = s+1
    u = end

    while True:
        while l < u and percent[l] <= p:
            l +=1
        while l <= u and percent[u] >= p:
          u -=1
        if l <= u:

        
    
            percent[l],percent[u] = percent[u],percent[l]
        
        else:
          break
    percent[s],percent[u] = percent[u],percent[s]
    return u  
def Quick_sort(percent,s,end):
    while s<end:
        partition1 = partition(percent,s ,end)
        Quick_sort(percent,s, partition1-1)
        Quick_sort(percent,partition1+1,end)
        return percent

          

unsorted_list = []
sorted_list = []


# creating unsorted list
unsorted_list = input_percentage()
print_percentage(unsorted_list)

# for sorted list 
print("sorted list is ")
sorted_list = Quick_sort(unsorted_list,0,len(unsorted_list)-1)
print_percentage(sorted_list)