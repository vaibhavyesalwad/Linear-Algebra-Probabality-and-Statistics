"""Program to add matrices"""
X = [[12, 7, 3],
     [4, 5, 6],               # For addition of matrices order of matrices must be same
     [7, 8, 9]]               # Both matrices X and Y are of order 3*3
Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

addition = [[X[i][j] + Y[i][j] for j in range(3)]for i in range(3)]    # added corresponding terms in matrices
for row in addition:
    print(row)             # displaying result
