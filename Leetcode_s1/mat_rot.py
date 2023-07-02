
"""
This is a quite decent problem till date
"""


def rotate_matrix(matrix):
    """
    Rotate a square matrix clockwise by 90 degrees.

    Parameters:
        matrix (List[List[int]]): The input square matrix.

    Returns:
        List[List[int]]: The rotated matrix.
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp
    return matrix
