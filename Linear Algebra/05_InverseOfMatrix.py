"""Program to find inverse matrix of matrix X"""


def minor(i, j):
    """Function returns determinant of remaining 2*2 matrix after ignoring given row & column in 3*3 matrix"""
    x = [k for k in range(3)]
    x.remove(i)                    # ignoring given row
    y = [k for k in range(3)]
    y.remove(j)                    # ignoring given column
    a, b = x
    c, d = y
    return X[a][c]*X[b][d] - X[b][c]*X[a][d]         # determinant of 2*2 matrix


X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

# determinant decides if inverse possible or not so calculating it first
determinant = X[0][0]*minor(0, 0) - X[0][1]*minor(0, 1) + X[0][2]*minor(0, 2)
if determinant:
    # finding minors matrix 3*3 using 2*2 matrices after ignoring current row & column
    minors_matrix = [[minor(i, j) for j in range(3)] for i in range(3)]
    # cofactors matrix is like chess box alternate positions are negated
    cofactors_matrix = [[-minors_matrix[i][j] if (i+j) % 2 else minors_matrix[i][j] for j in range(3)] for i in range(3)]
    # adjugate is transpose of cofactors matrix
    adjugate = [[cofactors_matrix[j][i] for j in range(3)] for i in range(3)]
    # inverse matrix is result of division of adjugate matrix by determinant of given matrix
    inverse = [[adjugate[i][j]/determinant for j in range(3)] for i in range(3)]
    for row in inverse:
        print(row)
else:
    print('Matrix has no inverse as determinant is 0')