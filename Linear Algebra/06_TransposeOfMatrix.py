"""Program to find transpose matrix of matrix given 3*3 matrix"""
Y = [[5, 8, 1],
     [6, 7, 3],           # given 3*3 matrix
     [4, 5, 9]]

# Transpose of matrix is changing rows to columns and vice versa
transpose = [[Y[j][i] for j in range(3)] for i in range(3)]
for row in transpose:
    print(row)             # displaying result
