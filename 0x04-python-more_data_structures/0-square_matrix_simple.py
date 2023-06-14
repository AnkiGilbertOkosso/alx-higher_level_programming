#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    cur_matrix = matrix.copy()

    for n in range(len(matrix)):
        cur_matrix[n] = list(map(lambda x: x**2, matrix[n]))

    return (cur_matrix)
