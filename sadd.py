# what is saddle point
# in short minimum in row and maximum in colume



# this program for saddle point
a= []
n = int(input("enter the row and colume :"))
for i in range(n):
    b = []
    for j in range(n):
        j = int(input("enter the element:"))
        b.append(j)
    a.append(b)

# for printing the element

for i in range(n):
    for j in range(n):
        print("\t",a[i][j],end = " ")
    print("\n")
f =0
for i in range(n):
      min = a[i][0]# for row 
      c = 0
      for j in range(n):
          if a[i][j]<min:
              min = a[i][j]
              c= j
      max = a[0][c]
      for k in range(n):
          if a[k][c]>max:
              max = a[k][c]



      if min == max :
          print("the saddle point is :",min)
          f =1

if f == 0:
   print("no saddle point")





