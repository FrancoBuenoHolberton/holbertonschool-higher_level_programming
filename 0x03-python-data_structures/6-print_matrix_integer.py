#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print()
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i.index[j] == len(i) -1:
                    print("{:d}".format(matrix[i][j]), end='')
                else:
                    print("{:d}".format(matrix[i][j]), end='')
            print()
