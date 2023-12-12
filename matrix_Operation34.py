# this program for matrix operation

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print("\t",matrix[i][j],end = " ")
        print("\n")

# for initialise the matrix
def in_mat(matrix,m,n):
    matrix = [[0 for j in range(0,m)] for i in range(0,n)]
    return matrix

def read_matrix():
    mat = []
    r = int(input("enter the row:"))
    c = int(input("enter the colume:"))
    mat = in_mat(mat,r,c)
    for i in range(0,r):
        for j in range(0,c):
            mat[i][j] = int(input("enter the element:"))
    return mat,r,c

def addition(m1,m2,res ,m,n):
    for i in range(0,m):
        for j in range(0,n):
            res[i][j] = m1[i][j] +m2[i][j]
    return res

matrix1 = []
matrix2 = []
res_mat = []
matrix1 ,r1,c1 = read_matrix()
matrix2 ,r2,c2 = read_matrix()
res_mat = in_mat(res_mat,r1,c2)

print("matrix no:1")
print_matrix(matrix1)
print("matrix no:2")
print_matrix(matrix2)
print("addition of two matrix is:")
res_matrix = addition(matrix1,matrix2,res_mat,r1,c1)
print_matrix(res_mat)