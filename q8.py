import numpy as np

mat = np.array([[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10],
               [11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20],
               [21, 22, 23, 24, 25]])

# Extract the submatrix:
submatrix = mat[2:5, 1:5]
print(submatrix)

# Extract specific rows and columns
specific_rows_columns = mat[[1, 2, 3], [1]]
print(specific_rows_columns)

# Get the sum of all values in mat
total_sum = np.sum(mat)
print(total_sum)

# Get the sum of rows and columns in mat:
row_sums = np.sum(mat, axis=1)
column_sums = np.sum(mat, axis=0)

print("Row sums:", row_sums)
print("Column sums:", column_sums)

