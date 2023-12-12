# this program for matrix operation

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print("\t",matrix[i][j],end = " ")
        print("\n")  

# initialize the matrix

def inti_matrix(matrix,m,n):
    matrix =[ [0 for j in range(0,n)] for i in range(0,m)]         
    return matrix 


# read the matrix
def read_matrix():
    mat = []
    r= int(input("enter the rows:"))
    c = int(input("enter the colume:"))
    mat = inti_matrix(mat,r,c)
    for i in range(0,r):
        for j in range(0,c):
          mat[i][j]= int(input("enter the element:"))
    return mat,r,c         



matrix1 = []
matrix2 = []
result_matrix = []
matrix1,r1,c1 = read_matrix()
matrix2 ,r2,c2 = read_matrix()
#result_matrix = inti_matrix(result_matrix,matrix1,matrix2,r1,c2)
print("the matrix one is:")

print_matrix(matrix1)

print("print matrix two:")
print_matrix(matrix2)
