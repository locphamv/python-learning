import numpy as np

values = np.arange(1, 13)

print("origingal array:")
print(values)

print("\nOriginal shape:", values.shape)
print("Original dimension:", values.ndim)

# 1. 3x4
matrix_3x4 = values.reshape(3, 4)

print("\nMatrix 3x4:")
print(matrix_3x4)
print("Shape:", matrix_3x4.shape)

# 2. 4x3
matrix_4x3 = values.reshape(4, 3)

print("\nMatrix 4x3:")
print(matrix_4x3)
print("Shape:", matrix_4x3.shape)

# 3. numpy auto count rows
auto_rows = values.reshape(-1, 3)

print("\nAuto rows, 3 column:")
print(auto_rows)
print("Shape:", auto_rows.shape)

# 4. auto count cols
auto_cols = values.reshape(3, -1)

print("\n3 rows, auto columns:")
print(auto_cols)
print("Shape:", auto_rows.shape)

# 5. sum
total = matrix_3x4.sum()
print("\nTotal:", total)

# 6. col sum
column_sums = matrix_3x4.sum(axis=0)
print("Column sums:", column_sums)

# 7. row sums
row_sums = matrix_3x4.sum(axis=1)
print("Row sums:", row_sums)

# 8. column averages
column_averages = matrix_3x4.mean(axis=0)
print(column_averages)

# 9. row averages
row_averages = matrix_3x4.mean(axis=1)
print(row_averages)

# 10. transpose matrix
transposed_matrix = matrix_3x4.T

print("\nTransposed matrix:")
print(transposed_matrix)
print("Transposed shape:", transposed_matrix.shape)

# 11. flatten
flattened_array = matrix_3x4.flatten()
print("\nFlattened array:")
print(flattened_array)
print("Flattened shape:", flattened_array.shape)

data = np.arange(1, 21).reshape(4, 5)
print("\nData:")
print(data)

print("First row:", data[0])
print("First column:", data[:, 0])

print("First two rows:")
print(data[:2])

print("Last two columns:")
print(data[:, -2:])

print("Maximum of each row:", data.max(axis=1))

print("Maximum of each column:", data.max(axis=0))

print("Argmax of each row:", data.argmax(axis=1))
