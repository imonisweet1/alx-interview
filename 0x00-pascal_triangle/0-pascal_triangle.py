#!/usr/bin/python3
"""0-pascal_triangle"""


def pascal_triangle(n):
    """function that creates a pascal trinagle  of n sisize"""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[- 1][j - 1] + triangle[- 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
