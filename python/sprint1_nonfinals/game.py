# 82199522
from typing import Tuple


def trainer(finger: int, matrix: str) -> int:
    numbers = {}
    scores = 0
    for number in matrix:
        if number != '.':
            if number not in numbers:
                numbers[number] = 0
            numbers[number] = numbers.get(number, 0) + 1
    for i in numbers.values():
        if 0 < i <= 2 * finger:
            scores += 1
    return scores


def read_input() -> Tuple[int, str]:
    finger = int(input())
    matrix = ''.join(str(input()) for i in range(4))
    return finger, matrix


if __name__ == '__main__':
    finger, matrix = read_input()
    print(trainer(finger, matrix))
