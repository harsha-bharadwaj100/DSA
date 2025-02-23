# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# m, n = 3, 3
# # remove the first row, column and last row, column
# matrix = matrix[1:m][1:n]
# print(matrix)
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# Slicing to get the inner matrix
inner_matrix = [row[1:-1] for row in matrix[1:-1]]

print(inner_matrix)
