# this program for find the saddle point
a = [] # list
n = int(input("enter the row and colume:")) # for row and colume
for i in range(n):
    b = []
    for  j in range(n):
        j = int(input("enter the element:"))
        b.append(j)
    a.append(b)    

# for printing purpose
for i in range(n):
    for  j in range(n):
        print("\t",a[i][j],end = "")
    print("\n")


# finding for saddle point
f = 0
for i in range(n):
    min = a[i][0]
    c =0
    for j in range(n):
        if a[i][j]<min:
            min = a[i][j]
            c = j
    max = a[0][j]
    for k in range(n):
        if a[k][c]>max:
            max = a[k][c]
    if min == max:
        print("saddle",min) 
        f = 1  

if f ==0:
    print("no saddle")


