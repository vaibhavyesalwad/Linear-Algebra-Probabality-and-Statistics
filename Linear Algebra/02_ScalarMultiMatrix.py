"""Program to perform scalar multiplication of matrix and a number"""
X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]
Y = 9                               # scalar

scalar_multi = [[X[i][j] * Y for j in range(3)] for i in range(3)]      # multiplying each element of matrix with scalar
for row in scalar_multi:
    print(row)                # displaying result
