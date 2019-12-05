"""Perform multiplication of given matrix and vector"""
X = [[5, 1, 3],
     [1, 1, 1],      # vector multiplication of matrix possible only when no. of columns in matrix equals rows in vector
     [1, 2, 1]]         # matrix is order 3*3
Y = [1, 2, 3]       # vector considered as single column 3*1

# resultant matrix will of size 3*1((columns in matrix)*1)
# multiplying columns of matrix with single column of vector
vector_multi = [[X[i][j]*Y[j] for j in range(3)] for i in range(3)]

for row in vector_multi:
    print(row)               # displaying result
