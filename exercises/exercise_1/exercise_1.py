import numpy as np

# a)
print('Problem a)')
null_vector = np.zeros(10)
null_vector[4] = 1
print(f'null_vector = {null_vector}') 

# b)
print('\nProblem b)')
aranged_vector = np.arange(10, 50)
print(f'aranged_vector = {aranged_vector}')

# c)
print('\nProblem c)')
reversed_vector_1 = np.flip(aranged_vector)
reversed_vector_2 = aranged_vector[::-1]
print(f'reversed_vector_1 = {reversed_vector_1}')
print(f'reversed_vector_2 = {reversed_vector_2}')

# d)
print('\nProblem d)')
matrix_3x3 = np.reshape(np.arange(0, 9), [3, 3])
print(f'matrix_3x3 = \n{matrix_3x3}')

# e)
print('\nProblem e)')
vector = np.array([1, 2, 0, 0, 4, 0])
non_zero = np.where(vector != 0)[0]
print(f'non_zero = {non_zero}')

# f)
print('\nProblem f)')
random_vector = np.random.randint(0, 100, size = 30)
mean = np.mean(random_vector)
print(f'random_vector = {random_vector}')
print(f'mean = {mean:.2f}')

# g)
print('\nProblem g)')
n_rows = 6
n_cols = 10
array_2D = np.zeros(shape = [n_rows, n_cols])
array_2D[:, 0] = np.ones(n_rows)
array_2D[:, -1] = np.ones(n_rows)
array_2D[0, :] = np.ones(n_cols)
array_2D[-1, :] = np.ones(n_cols)
print(f'array_2D = \n{array_2D}')

# h)
print('\nProblem h)')
checkerboard = np.zeros(shape = [8, 8])

# Pick out odd rows
odd_rows = checkerboard[1::2]

# Set every second element in odd_rows to 1, and every second to zero
odd_rows[:, 1::2] = 1
odd_rows[:, 0::2] = 0 # it's zero to begin with, so not really necessary

# Pick out even rows
even_rows = checkerboard[0::2]

# Set every second element in even_rows 1 and every second to zero
even_rows[:, 0::2] = 1
even_rows[:, 1::2] = 0

print(f'checkerboard = \n{checkerboard}')

# i)
print('\nProblem i)')
matrix_2x2 = np.array([[0, 1], [1, 0]])
tile_checkerboard = np.tile(matrix_2x2, (4, 4))
print(f'tile_checkerboard = \n{tile_checkerboard}')

# j)
print('\nProblem j)')
z = np.arange(11)

# Negate numbers between 3 and 8.
z[(z > 3) & (z < 8)] *= -1
print(f'z = {z}')

# k)
print('\nProblem k)')
z_unsorted = np.random.random(10)
z_sorted = np.sort(z_unsorted)
print(f'Unsorted z = \n{z_unsorted}')
print(f'Sorted z = \n{z_sorted}')

# l)
print('\nProblem l)')
A = np.random.randint(0, 2, 5)
B = np.random.randint(0, 2, 5)

# Check if all elements are equal
equal = np.all(A == B)
print(f'A and B contain the same elements: {equal}')

# m)
print('\nProblem m)')
z = np.arange(10, dtype = np.int32)
print(f'Before conversion: {z.dtype}')
z = np.array(z, dtype = np.int64)
print(f'After conversion: {z.dtype}')

# n)
print('\nProblem n)')
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
diag = np.diag(C)
print(f'C = np.dot(A, B) = \n{C}')
print(f'Diagonal of C: {diag}')


















