#!/usr/bin/python3
"""Pascal's Triangle function."""


def pascal_triangle(n):
    """To Representing Pascal's Triangle of size n.
    Returns list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        triang = triangle[-1]
        tmp = [1]
        for i in range(len(triang) - 1):
            tmp.append(triang[i] + triang[i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle
