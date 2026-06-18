import math

def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

def matrix_multiply(A, B):
    # Standard O(n^3) implementation
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result
