"""Program to multiply matrices"""

X = [[12, 7, 3],
     [4, 5, 6],               # For multiplication of matrices columns in matrix1 must be equal to rows in matrix2
     [7, 8, 9]]               # Both matrices X and Y are of order 3*3
Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

# resultant matrix will be of size 3*3 (for matrices of m*n and n*p resultant matrix will be m*p)
# multiplying rows of X with columns of Y
multiplication = [[sum(X[i][k]*Y[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
for row in multiplication:
    print(row)                     # displaying result

