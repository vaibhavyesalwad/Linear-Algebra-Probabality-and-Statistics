"""Program to perform scalar multiplication of matrix and a number"""
# taking order of matrix from user
while True:
    try:
        rows = int(input('Enter number of rows for X matrix:'))
        cols = int(input('Enter number of columns for X matrix:'))
        break
    except ValueError:
        print('Enter only integers')

# taking values for scalar and matrix X from user
while True:
    try:
        scalar = int(input('Enter an integer as scalar:'))      # scalar is real number
        input("Let's start filling values in matrix X")
        # matrix is 2D list having numbers as it's elements here we are taking integers
        X = [[int(input(f'Enter value for X[{row}][{col}]:'))for col in range(cols)] for row in range(rows)]
        break
    except ValueError:
        print('Please enter only integer values')

# displaying matrix
print('Matrix X')
for row in X:
    print(row)

print(f'Scalar multiplication of matrix X and {scalar} (scalar)')
# multiplying each element of matrix X by with the scalar
scalar_multi = [[X[row][col] * scalar for col in range(cols)] for row in range(rows)]
for row in scalar_multi:
    print(row)                # displaying result
