# Find saddle point position if present
def saddle(m):
     for i in range(0, len(m)):
# Find the minimum element of row i.
# Also find column index of the minimum  element
            min_row = m[i][0]
            col_ind = 0
            for j in range(1, len(m[0])):
               if min_row > m[i][j]:
                min_row = m[i][j]
                col_ind = j

# Check if the minimum element of row is also
# the maximum element of column or not
            flag = 0
            for k in range(0, len(m)):
                 if min_row < m[k][col_ind]:
                  flag = 1
                  break
            if flag == 0:
                print("Saddle point is : ", min_row)
                print("Saddle point is present atlocation m[{0}][{1}]".format(i, col_ind)) 
            return
     print("No Saddle point present") 
     return
# Read the matrix
def read_mat():
    row = int(input(" Enter the rows in the matrix :"))
    col = int(input(" Enter the columns in thematrix : "))
# Accept the matrix of size row X col
# Initialize matrix
    mat = []
    print("Enter the elements rowwise:")
# For user input
    for i in range(0, row): # A for loop for row entries
        a = []
        for j in range(0, col): # A for loop for column entries
           a.append(int(input("Enter element : ")))
           mat.append(a)
        return mat, row, col

matrix = []

# example of no saddle point
#matrix = [[1, 2, 3], [4, 5, 6], [10, 18, 4]]
# example of saddle point
# matrix = [[1,2,3],[4,5,6],[7,8,9]]

matrix, row, col = read_mat()
# Print Matrix
print("The matrix is : ")
for i in range(0, row):
    for j in range(0, col):
          print(matrix[i][j], end = " ")
          print()
saddle(matrix)