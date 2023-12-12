# THIS PROGRAM FOR MATRIX OPERATION
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
           print("\t",matrix[i][j],end = " ")
        print("\n")


def in_ma(matrix,m,n):
    matrix = [[0 for i in range(0,m)] for i in range(0,n)]
    return matrix 


def read_mat():
    mat = []
    r = int(input("enter the row:"))
    c = int(input("enter the colume:"))
    mat = in_ma(mat,r,c)
    for i in range(0,r):
        for j in range(0,c):
            mat[i][j] = int(input("enter the element:"))
    return mat ,r,c

def addition(m1,m2,res,m,n):
    for i in range(0,m):
        for j in range(0,n):
            res[i][j] = m1[i][j]+m2[i][j]
    return res 

matrix1 = []
matrix2 = []
result_mat = []
matrix1 ,r1,c1 = read_mat()
matrix2 ,r2,c2  = read_mat()
result_mat = in_ma(result_mat,r1,c2)
print("matrix 1")
print_matrix(matrix1)
print("matrix 2")
print_matrix(matrix2)


result_mat = addition(matrix1,matrix2,result_mat,r1,c1)
print_matrix(result_mat)
