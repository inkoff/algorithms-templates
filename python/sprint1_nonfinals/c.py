from typing import List, Tuple


def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    lll: List[int] = []
    if row > 0:
        lll.append(matrix[row - 1][col])
    if col > 0:
        lll.append(matrix[row][col - 1])
    if col < len(matrix[0]) - 1:
        lll.append(matrix[row][col + 1])
    if row < len(matrix) - 1:
        lll.append(matrix[row + 1][col])
    lll.sort()
    return lll


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col


matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))
