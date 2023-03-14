from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:
    first_number = list(map(int, first_number[::-1]))
    second_number = list(map(int, second_number[::-1]))
    len1 = len(first_number)
    len2 = len(second_number)
    max_size = max(len1, len2)
    first_number += [0] * (max_size - len1)
    second_number += [0] * (max_size - len2)
    overflow = 0
    result = []
    for obj in zip(first_number, second_number):
        value = obj[0] + obj[1] + overflow
        overflow = value // 2
        result.append(value % 2)
    if overflow == 1:
        result.append(1)
    result = result[::-1]
    return ''.join(map(str, result))


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
