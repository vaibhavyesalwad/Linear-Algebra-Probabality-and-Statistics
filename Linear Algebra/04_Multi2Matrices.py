"""Program to multiply matrices"""
# taking order of two matrices from user
while True:
    try:
        rows1 = int(input('Enter number of rows for matrix1:'))
        cols1 = int(input('Enter number of columns for matrix1:'))
        while True:
            try:
                rows2 = int(input('Enter number of rows for matrix2:'))
                cols2 = int(input('Enter number of columns for matrix2:'))
                assert cols1 == rows2             # condition for matrix multiplication
                break
            except ValueError:
                print('Enter only integers')
            except AssertionError:
                print("Number of columns in matrix1 & number of rows in matrix2 don't match")
        break
    except ValueError:            # making sure inputs are integers
        print('Enter only integers')

input("Let's start filling matrix1")
# taking values for matrix1
while True:
    try:
        matrix1 = [[int(input(f'Enter value for matrix1[{row}][{col}]:')) for col in range(cols1)] for row in range(rows1)]
        break
    except ValueError:
        print('Please enter only integer values')

input("Now filling matrix2")
# taking values for matrix2
while True:
    try:
        matrix2 = [[int(input(f'Enter value for matrix2[{row}][{col}]:')) for col in range(cols2)] for row in range(rows2)]
        break
    except ValueError:
        print('Please enter only integer values')

print('matrix1')
# displaying first matrix
for row in matrix1:
    print(row)

print('matrix2')
# displaying second matrix
for row in matrix2:
    print(row)

# resultant matrix will be of order rows1*cols2
# multiplying rows of X with columns of Y
multiplication = [[sum(matrix1[row][k]*matrix2[k][col] for k in range(cols1)) for col in range(cols2)] for row in range(rows1)]

print('Multiplication of matrix1 & matrix2')
for row in multiplication:
    print(row)                     # displaying result

