"""Program to add matrices"""
X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]
Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

addition = [[X[i][j] + Y[i][j] for j in range(3)]for i in range(3)]    # added corresponding terms in matrices
for row in addition:
    print(row)             # displaying result
