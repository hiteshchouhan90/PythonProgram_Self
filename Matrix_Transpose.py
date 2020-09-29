# This program will transpose the given matrix

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [10, 11, 12, 13], [14, 15, 16, 17]]

transposed_1 = []
size_mat = len(matrix)
for i in range(size_mat):
    lst = []
    for j in range(size_mat):
        lst.append(matrix[j][i])
    transposed_1.append(lst)
print("Transposed matrix is {}".format(transposed_1))

transposed = []
for i in range(4):
    lst = []
    for row in matrix:
        lst.append(row[i])
    transposed.append(lst)
print("Transposed matrix is {}".format(transposed))