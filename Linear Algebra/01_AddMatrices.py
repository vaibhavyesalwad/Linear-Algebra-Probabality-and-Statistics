"""Program to add matrices"""
# taking order of first matrix
while True:
    try:
        rows1 = int(input('Enter number of rows for X matrix:'))
        cols1 = int(input('Enter number of columns for X matrix:'))
        break
    except ValueError:                # making sure input values are integers
        print('Enter only integers')

print(f'Order of matrix X is {rows1}*{cols1}')

# taking order of second matrix & checking if it matches with first matrix
while True:
    try:
        rows2 = int(input('Enter number of rows for Y matrix:'))
        cols2 = int(input('Enter number of columns for Y matrix:'))
        print(f'Order of matrix Y is {rows2}*{cols2}')
        assert rows1 == rows2 and cols1 == cols2
        break
    except ValueError:
        print('Enter only integers')
    except AssertionError:
        print('Number of rows and columns for both matrices X & Y must match')

print(f'Order of both matrices X & Y is same i.e {rows2}*{cols2}, now we can add them')
input("Let's start filling matrix X")

# taking values for first matrix from user
while True:
    try:
        X = [[int(input(f'Enter value for X[{row}][{col}]:'))for col in range(cols1)] for row in range(rows1)]
        break
    except ValueError:
        print('Please enter only integer values')

input("Let's start filling matrix Y")

# taking values for second matrix from user
while True:
    try:
        Y = [[int(input(f'Enter value for Y[{row}][{col}]:')) for col in range(cols2)] for row in range(rows2)]
        break
    except ValueError:
        print('Please enter only integer values')

print('Matrix X')
for row in X:
    print(row)
print('Matrix Y')
for row in Y:
    print(row)

addition = [[X[row][col] + Y[row][col] for col in range(cols1)]for row in range(rows1)]
print('Addition of matrices X & Y')
for row in addition:
    print(row)             # displaying result
