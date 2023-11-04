def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            array[j], array[j-1] = array[j-1], array[j]
            j = j - 1
    return array



        

def print_sorted(array):
    for i in range(len(array)):
        print(array[i],sep = "\n")

unsorted_list = []
sorted_list = []

array =  []
n = int(input("enter the element you want :"))
for i in range(n):
    mark = int(input("enter the marks:"))
    array.append(mark)


sorted_list =insertion_sort(array)
print("after insertion sort ")    
print_sorted(sorted_list)
