# this program for find the saddle point
"""a = [] # taking empty list
n = int(input("enter number of row and colume: "))
for i in range(n):
     b = [] #creating empty list
     for j in range(n):
          j = int(input("enter a number element :"))
          b.append(j)
     a.append(b)
print(" the matrix is ____")
for  i in range(n):
     for j in range(n):
           print(a[i][j],end =" ")
     print()"""
""""
bharat = [] # create empty list
n = int(input("enter a number of rows and colume: ")) # enter the number of colume and row 
for i in range(n): # number of row and colume
      bharat2 =[]  # again creating empty list.
      for j in range(n): # for colume.
            m = int(input("enter the element:["+str(i)+"]["+str(j)+"] "))
            bharat2.append(m) # element are append to the bharat2 list
      bharat.append(bharat2) #bharat2 list append to the original list bharat.


# printing the matrix
for i in range(n):
      for j in range(n):
            print(bharat[i][j],end =" ")
      print()  
f = 0
 # finding the saddle Point
for i in range(n):
       min = bharat[i][0]
       c = 0
       for j in range(n):
             if bharat[i][j]<min:
                   min = bharat[i][j]
                   c =j           
       max = bharat[0][c]
       for k in range(n):
             if bharat[k][c]>max:
                max =bharat[k][c]
       if min == max:
            print("saddle point is ",min)
            f =1
if f == 0:
         print("no saddle point")

""" 
v= []# taking empty list
n = int(input("enter number of row and colume: "))
for i in range(n):
    b = []
    for j in range(n):
        a = int(input("enter the element:["+str(i)+"]["+str(j)+"] "))  
        b.append(a)
    v.append(b)
f = 1
# printing the matrix
for i in range(n):
    for j in range(n):
        print(v[i][j],end = " ")
    print() 

# finding the saddle element
for i in range(n):
        min = v[i][0]
        c = 0
        for j in range(n):
            if v[i][j]<min:
                min = v[i][j] 
                c = j                
        max = v[0][c]
        for k in range(n):
             if v[k][c]>max:
                 max = v[k][c]
        if min == max:
            print("saddle point",min)
            f = 1    
if f ==0:
      print("no saddle point")

      
             