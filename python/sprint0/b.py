from typing import List, Tuple


def zipper(a: List[int], b: List[int], n: int) -> List[int]:
    lst: list = list()
    for i in range(n):
        lst.append(a[i])
        lst.append(b[i])
    return lst


def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b, n


a, b, n = read_input()


print(" ".join(map(str, zipper(a, b, n))))
