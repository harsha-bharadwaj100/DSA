# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# m, n = 3, 3
# # remove the first row, column and last row, column
# matrix = matrix[1:-1][1:-1]
# print(matrix)
# # matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# # # Slicing to get the inner matrix
# # inner_matrix = [row[1:-1] for row in matrix[1:-1]]

# # print(inner_matrix)

from tabnanny import check


s1 = {3, 4, 7, 1, 0}
s2 = {4, 1}
print(s2.issubset(s1))
print(s1 - s2)
# set operations

# intersection
print(s1 & s2)
# union
print(s1 | s2)
# difference
print(s1 - s2)
# symmetric difference
print(s1 ^ s2)
