"""Program to find inverse matrix of given 3*3 matrix """


def minor(row, col):
    """Function returns determinant of remaining 2*2 matrix after ignoring given row & column in 3*3 matrix"""
    rows = [k for k in range(3)]
    rows.remove(row)                    # ignoring given row
    cols = [k for k in range(3)]
    cols.remove(col)                    # ignoring given column
    a, b = rows
    c, d = cols
    return X[a][c]*X[b][d] - X[b][c]*X[a][d]         # determinant of 2*2 matrix


X = [[12, 7, 3],
     [4, 5, 6],                      # given matrix
     [7, 8, 9]]

# determinant decides if inverse possible or not so calculating it first
determinant = X[0][0]*minor(0, 0) - X[0][1]*minor(0, 1) + X[0][2]*minor(0, 2)
if determinant:
    # finding minors matrix 3*3 using 2*2 matrices after ignoring current row & column
    minors_matrix = [[minor(row, col) for col in range(3)] for row in range(3)]
    # cofactors matrix is like chess box alternate positions are negated
    cofactors_matrix = [[-minors_matrix[row][col] if (row+col) % 2 else minors_matrix[row][col] for col in range(3)] for row in range(3)]
    # adjugate is transpose of cofactors matrix
    adjugate = [[cofactors_matrix[col][row] for col in range(3)] for row in range(3)]
    # inverse matrix is result of division of adjugate matrix by determinant of given matrix
    inverse = [[adjugate[row][col]/determinant for col in range(3)] for row in range(3)]
    for row in inverse:
        print(row)                # displaying result
else:
    print('Matrix has no inverse as determinant is 0')