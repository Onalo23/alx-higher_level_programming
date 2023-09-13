#!/usr/bin/python3
"""defined a Pascal Triangle"""


def pascal_triangle(n):
    """Represents Pascal Triangle of size n

    Return list of lists of integer representing the triangle
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for j in range(len(tri) - 1):
            tmp.append(tri[j] + tri[j + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
