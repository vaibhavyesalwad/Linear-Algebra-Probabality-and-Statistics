"""Program to add matrices"""
# taking order of first matrix
while True:
    try:
        rows1 = int(input('Enter number of rows for matrix1:'))
        cols1 = int(input('Enter number of columns for matrix1:'))
        print(f'Order of matrix1 is {rows1}*{cols1}')
        while True:
            try:
                rows2 = int(input('Enter number of rows for matrix2:'))
                cols2 = int(input('Enter number of columns for matrix2:'))
                print(f'Order of matrix2 is {rows2}*{cols2}')
                assert rows1 == rows2 and cols1 == cols2       # checking if rows & columns of 2 matrices match
                break
            except ValueError:
                print('Enter only integers')
            except AssertionError:
                print('Number of rows and columns for both matrices- matrix1 & matrix2 must match')
        break
    except ValueError:                # making sure input values are integers
        print('Enter only integers')


print(f'Order of both matrices- matrix1 & matrix2 is same i.e {rows2}*{cols2}, now we can add them')
input("Let's start filling matrix1")

# taking values for first matrix from user
while True:
    try:
        matrix1 = [[int(input(f'Enter value for matrix1[{row}][{col}]:'))for col in range(cols1)] for row in range(rows1)]
        break
    except ValueError:
        print('Please enter only integer values')

input("Let's start filling matrix2")

# taking values for second matrix from user
while True:
    try:
        matrix2 = [[int(input(f'Enter value for matrix2[{row}][{col}]:')) for col in range(cols2)] for row in range(rows2)]
        break
    except ValueError:
        print('Please enter only integer values')

# displaying matrices
print('matrix1')
for row in matrix1:
    print(row)

print('matrix2')
for row in matrix2:
    print(row)

# adding corresponding elements of matrices
addition = [[matrix1[row][col] + matrix2[row][col] for col in range(cols1)]for row in range(rows1)]
print('Addition of matrix1 & matrix2')
for row in addition:
    print(row)             # displaying result
