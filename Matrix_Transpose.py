# This program will transpose the given matrix

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [10, 11, 12, 13], [14, 15, 16, 17, 18]]

print("Let's Check if its a square matrix")


def check_square_matrix(matrix: list):
    flag = False
    length_mat = len(matrix)
    for i in range(length_mat):
        if len(matrix[i]) == length_mat:
            flag = True
        else:
            flag = False
            return flag
    return flag


if __name__ == "__main__":
    if check_square_matrix(matrix) == True:
        transposed_1 = []
        size_mat = len(matrix)
        for i in range(size_mat):
            lst = []
            for j in range(size_mat):
                lst.append(matrix[j][i])
            transposed_1.append(lst)
        print("Original Matrix is {}".format(matrix))
        print("Transposed matrix is {}".format(transposed_1))
    else:
        print("{} is not a square matrix ".format(matrix))

# Following is another way of transposing the matrix
"""
transposed = []
for i in range(4):
    lst = []
    for row in matrix:
        lst.append(row[i])
    transposed.append(lst)
print("Transposed matrix is {}".format(transposed))"""
