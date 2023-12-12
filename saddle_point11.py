# this program for find saddle point
a = []
n = int(input("enter the row and col:"))
for i in range(n):
    b = []
    for j in range(n):
        j = int(input("enter the element:"))
        b.append(j)
    a.append(b) 



print("matrix is ")
for i in range(n):
    for j in range(n):
        print("\t",a[i][j],end = "")
    print("\n")   

f = 1
# for saddle point
for i in range(n):
    min = a[i][0]# for row
    c =0
    for j in range(n):
        if a[i][j]<min:
            min = a[i][j]
            c = j
    max = a[0][c]
    for k in range(n):
        if a[k][c]>max:
            max = a[k][c]
    if min == max:
        print("saddle point of matrix is ",min)

if f == 0:
    print("no saddle point")