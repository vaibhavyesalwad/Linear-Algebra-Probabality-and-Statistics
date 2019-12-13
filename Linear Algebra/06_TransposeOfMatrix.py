"""Program to find transpose matrix of matrix given 3*3 matrix"""
# taking order of matrix from user
while True:
    try:
        rows = int(input('Enter number of rows for matrix:'))
        cols = int(input('Enter number of columns for matrix:'))
        break
    except ValueError:             # making sure integer input values
        print('Enter only integers')

input("Now filling matrix")
# taking values for matrix
while True:
    try:
        matrix = [[int(input(f'Enter value for matrix[{row}][{col}]:')) for col in range(cols)] for row in range(rows)]
        break
    except ValueError:
        print('Please enter only integer values')

# displaying matrix
print('matrix')
for row in matrix:
    print(row)

# Transpose will be of order cols*rows
# Transpose of matrix is swapping rows and columns
transpose = [[matrix[row][col] for row in range(rows)] for col in range(cols)]

print('Transpose')
for row in transpose:
    print(row)             # displaying result
