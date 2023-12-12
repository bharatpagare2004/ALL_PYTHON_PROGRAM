# quick sort
def taking_input():
      arr = []
      n = int(input("enter the how many time: "))
      for i in range(n):
            ma = int(input("enter the marks :"))
            arr.append(ma)
      return arr      

# for printing purpose
def print_marks(arr):
       for i in range(len(arr)):
             print(arr[i],sep = " ")




def partition(arr,low ,high):
       p = arr[low]
       i = low+1
       j = high 

       while True:
              while i <= j and arr[i] <= p:
                     
                     i +=1
              while i <=  j and arr[j] >= p:
                     j -=1 
              if i <= j:
                      arr[i],arr[j] = arr[j], arr[i]
              else:
                break
       arr[low] ,arr[j] = arr[j], arr[low]
       return j

def quick_sort(arr,low ,high):
        if low <high:
              p = partition(arr ,low ,high)
              quick_sort(arr,low,p-1)
              quick_sort(arr,p+1,high)
              return arr
        
     
        
        
        


sorted = []
unsorted = []


while(1):
      print("1.for display you entered number")
      print("2.display sorted element")
      ch = int(input("enter your choice:"))
      if ch == 1:
        unsorted = taking_input()
        print_marks(unsorted)
      elif ch == 2:
            
         sorted = quick_sort(unsorted,0,len(unsorted)-1)
         print_marks(sorted)


        

          



       
       
       


                
