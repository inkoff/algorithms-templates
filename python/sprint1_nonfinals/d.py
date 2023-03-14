from typing import List, Tuple


def get_weather_randomness(temperatures: List[int]) -> int:
    r = 0
    n = len(temperatures)
    if n == 1:
        r += 1
        return r
    if temperatures[0] > temperatures[1]:
        r += 1
    if temperatures[-1] > temperatures[-2]:
        r += 1
    for i in range(1, n - 1):
        if temperatures[i - 1] < temperatures[i] > temperatures[i + 1]:
            r += 1
    return r


def read_input() -> Tuple[List[int]]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


temperatures = read_input()
print(get_weather_randomness(temperatures))
