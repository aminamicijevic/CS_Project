# The question isn't completely visible, but I think we are supposed to transpose a matrix
import numpy as np

matrix = [[2, 4, 6, 8, 10], [1, 3, 7, 9, 11]]
my_matrix = np.array(matrix)
dim0_size, dim1_size = my_matrix.shape
my_matrix_transposed = [[my_matrix[i][j] for i in range(dim0_size)]
                        for j in range(dim1_size)]  # Your NESTED list comprehension here
print(my_matrix_transposed)  # Printed as a regular list
print(my_matrix.transpose())  # As a numpy array
