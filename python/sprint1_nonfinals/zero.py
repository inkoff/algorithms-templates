# 82125129
from typing import List, Tuple


def calculate(length: int, numbers: List[int]) -> List[int]:
    distance = [0 for _ in range(length)]
    zero_position = None
    for i, value in enumerate(numbers):
        if value == 0:
            zero_position = i
            continue
        if zero_position is not None:
            distance[i] = i - zero_position
        else:
            distance[i] = length
    zero_position = None
    for i in range(length - 1, -1, -1):
        if numbers[i] == 0:
            zero_position = i
            continue
        if zero_position is not None:
            distance[i] = min(distance[i], zero_position - i)
    return distance


def read_input() -> Tuple[int, List[int]]:
    length = int(input())
    number_street = [int(num) for num in input().split(' ')]
    return length, number_street


if __name__ == '__main__':
    length, number_street = read_input()
    print(*calculate(length, number_street), sep=' ')
