from typing import Tuple, List


def transpose(row: int, col: int, matrix: List[str]) -> List[List[int]]:
    transpose_matrix = [[0 for _ in range(row)] for _ in range(col)]
    for i in range(row):
        for j in range(col):
            transpose_matrix[j][i] = matrix[i][j]
    return transpose_matrix


def read_input() -> Tuple[int, int, List[str]]:
    row = int(input())
    col = int(input())
    matrix = [input().strip().split() for i in range(row)]
    return row, col, matrix


if __name__ == '__main__':
    row, col, matrix = read_input()
    for _ in transpose(row, col, matrix):
        print(*_, sep=' ')
