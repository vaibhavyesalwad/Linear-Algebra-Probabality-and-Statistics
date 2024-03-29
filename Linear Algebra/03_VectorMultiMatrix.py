"""Perform multiplication of given matrix and vector"""

# taking order of matrix from user
while True:
    try:
        rows = int(input('Enter number of rows for matrix:'))
        cols = int(input('Enter number of columns for matrix:'))
        while True:
            try:
                # vector is single column/row matrix eventually considered column matrix
                vector_rows = int(input('Enter number of rows/columns in vector matrix:'))
                assert vector_rows == cols             # condition for vector multiplication
                break
            except ValueError:
                print('Enter only integer for number of rows in vector')
            except AssertionError:
                print("Number of columns in matrix & number of rows in vector don't match")
        break
    except ValueError:           # making sure input values are integers
        print('Enter only integers')

print("Let's start filling matrix")
# taking values for matrix from user
while True:
    try:
        matrix = [[int(input(f'Enter value for matrix[{row}][{col}]:')) for col in range(cols)] for row in range(rows)]
        input("Now filling vector")
        vector = [int(input(f'Enter value for vector[{row}]:')) for row in range(vector_rows)]
        break
    except ValueError:
        print('Please enter only integer values')

# displaying matrix
print('matrix')
for row in matrix:
    print(row)

# displaying vector
print('Vector')
for num in vector:
    print(f'[{num}]')

# multiplying columns of matrix with single column of vector
vector_multi = [sum(matrix[row][col]*vector[col] for col in range(cols)) for row in range(rows)]

print('Vector multiplication of matrix X & above vector')
for row in vector_multi:
    print(f'[{row}]')               # displaying result
