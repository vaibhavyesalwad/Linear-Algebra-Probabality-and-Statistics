"""Program to find inverse matrix of given matrix """
from copy import deepcopy                      # it is crucial for this program
# taking order of matrix from user
while True:
    try:
        # only square matrix can have inverse
        print('Only square matrix are invertible')
        rows = cols = int(input('Enter number of rows/columns for matrix:'))
        break
    except ValueError:  # making sure input integer values
        print('Enter only integers')

input("Now filling matrix")
# taking values for matrix
while True:
    try:
        matrix = [[int(input(f'Enter value for matrix[{row}][{col}]:')) for col in range(cols)] for row in range(rows)]
        break
    except ValueError:
        print('Please enter only integer values')


def minor(mat, r, c):
    """Function returns matrix ignoring given row & column of given matrix"""
    mat.pop(r)                 # ignoring row
    for row in mat:
        row.pop(c)             # ignoring column
    return mat


def determinant(mat):
    """Function recursively finds determinant of given matrix"""
    # when matrix of order is 1
    if len(mat) == 1:
        return mat[0][0]
    else:
        # finding determinant using first row
        # we have used deepcopy here because matrix has nested elements thus it allows matrix manipulation
        return sum(mat[0][col] * determinant(minor(deepcopy(mat), 0, col)) if col % 2 == 0
                   else -mat[0][col] * determinant(minor(deepcopy(mat), 0, col)) for col in range(len(mat)))


print('matrix')
# displaying matrix
for row in matrix:
    print(row)

det = determinant(matrix)
print(f'Determinant of matrix: {det}')

# inverse exists only if determinant is non-zero number
if det:
    # finding minors matrix after ignoring current row & column
    minors_matrix = [[determinant(minor(deepcopy(matrix), row, col)) for col in range(cols)] for row in range(rows)]
    print('matrix of minors')
    # displaying minors matrix
    for row in minors_matrix:
        print(row)

    # cofactors matrix is like chess box alternate positions are negated
    cofactors_matrix = deepcopy(minors_matrix)
    for row in range(rows):
        for col in range(cols):
            if row % 2 == 0:
                if col % 2:
                    cofactors_matrix[row][col] = -cofactors_matrix[row][col]
            else:
                if col % 2 == 0:
                    cofactors_matrix[row][col] = -cofactors_matrix[row][col]

    print('matrix of cofactors')
    # displaying cofactors matrix
    for row in cofactors_matrix:
        print(row)

    # adjoint is transpose of cofactors matrix
    adjoint = [[cofactors_matrix[col][row] for col in range(cols)] for row in range(rows)]
    print('adjoint')
    # displaying adjoint matrix
    for row in adjoint:
        print(row)

    # inverse matrix is result of division of adjoint matrix by determinant of given matrix
    inverse = [[adjoint[row][col]/det for col in range(cols)] for row in range(rows)]
    print('inverse of matrix')
    for row in inverse:
        print(row)                # displaying result


else:
    print(f'Matrix has no inverse as determinant is {det}')

