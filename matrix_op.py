# this is matrix operation
# print the matrix
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
               print("\t", matrix[i][j],end =" ")
        print("\n")  
           
# initilize the matrix with zero
def init_matrix(matrix,m,n):
    matrix = [[0 for j in range(0,n)] for i in range(0,m)]
    return matrix            
#input the matrix
def read_matrix():
    mat = []
    r = int(input("enter the rows in first matrix: "))
    c = int(input("enter the colums in the firstmatrix: "))
    mat = init_matrix(mat,r,c)
    for i in range(0,r):
        for j in range(0,c):
            mat[i][j] = int(input("enter an element: "))
    return mat ,r,c        

def add_mat(m1,m2,res,m,n):
    for i in range(0,m):
        for j in range(0,n):
            res[i][j] = m1[i][j] + m2[i][j]
    return res

def sub_mat(m1,m2,res,m,n):
    for i in range(0,m):
        for j in range(0,n):
            res[i][j] = m1[i][j]-m2[i][j]
    return res


def transpose(m1,res,r1,c1):
    for i in range(0,r1):
        for j in range(0,c1):
         res[j][i] = m1[i][j]
    return res     

    







matrix1 = []
matrix2 =[]
res_matrix = []
matrix1, r1,c1 =  read_matrix()
matrix2, r2,c2 = read_matrix()
res_matrix = init_matrix(res_matrix,r1,c2)
print("m1")
print_matrix(matrix1)
print("m2")
print_matrix(matrix2)
print("addition")



bharat =1
while bharat:
      print("menu")
      print("1.addition")
      print("2.substraction")
      print("3.transpose")
      choice =int(input("enter your choice: "))
      if choice ==1:
           if r1 == r2 and c1==c2:
            print("addition matrix is ")
            

            res_matrix = add_mat(matrix1,matrix2,res_matrix,r1,c1)
            print_matrix(res_matrix)

      elif choice == 2:
          if r1 ==r2 and c1 ==c2:
              print("substraction matrix")
              res_matrix = sub_mat(matrix1,matrix2,res_matrix,r1,c1)

              print_matrix(res_matrix) 
          else:
              print("substraction not perform")  

      elif choice == 3:
          res_matrix1 = []
          res_matrix1 = init_matrix(res_matrix1,c1,r1) 
          res_matrix = transpose(matrix1,res_matrix1,r1,c1)
          print_matrix(res_matrix)            
      else:
           print("no output")


bharat = 0      