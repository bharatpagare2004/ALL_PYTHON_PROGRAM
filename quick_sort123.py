# function for accepting percentage of the student.
# creating taking_percentage function.
def taking_percentage():
    percentage = [] # creating empty list for storing the percentage of student
    number_of_student = int(input("enter the number of student you want to take:"))
    for i in range(number_of_student):
        marks = int(input("enter the percentage {0}: ".format(i+1)))
        percentage.append(marks)
    return percentage

################################################
# function for printing percentage of student.
def print_percentage(percentage):# passing the parameter percentage.

    for i in range(len(percentage)):
        print(percentage[i],sep = "\n")
#################################


# function for partition
def partition(percentage,start,end):
    pivot =percentage[start]
    lower_bound = start+1
    upper_bound = end
    while True :
        # when all condition become not cheak it trival


         while lower_bound <= upper_bound and percentage[lower_bound] <= pivot:
             lower_bound += 1
         while lower_bound <=upper_bound and percentage[upper_bound] >= pivot:
              upper_bound -=1


         if lower_bound <= upper_bound:
             percentage[lower_bound],percentage[upper_bound] = percentage[upper_bound],percentage[lower_bound] 

         else :
             break
         
    percentage[start],percentage[upper_bound] = percentage[upper_bound],percentage[start]
    return upper_bound
##########################################
# performing quick sort
def quick_sort(percentage, start,end):
    while start<end:
        partition1 = partition(percentage,start,end)
        quick_sort(percentage ,start,partition1 -1)
        quick_sort(percentage,partition1+1,end)
        return percentage
# main program
unsorted_list =[]
sorted_list =[]
flag =1
while flag ==1:
    print("\n###############menu##################")
    print("1.accept the percentage.")
    print("2.display percentage of student.")
    print("3.perform quick sort.")
    print("4.exit")

    ch = int(input("enter your choice number: "))
    if ch == 1:
        unsorted_list = taking_percentage()

    elif ch ==2 :
        print_percentage(unsorted_list)

    elif ch ==3 :
        print("percentage of student ")
        sorted_list = quick_sort(unsorted_list,0,len(unsorted_list)-1)
        print_percentage(sorted_list)
    elif ch == 4:
        flag =0
    else :
        print("invalid choice.") 



                 




