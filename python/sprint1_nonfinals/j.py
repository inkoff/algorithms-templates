from typing import List


def factorize(number: int) -> List[int]:
    Ans = []
    d = 2
    while d * d <= number:
        if number % d == 0:
            Ans.append(d)
            number //= d
        else:
            d += 1
    if number > 1:
        Ans.append(number)
    return Ans


result = factorize(int(input()))
print(" ".join(map(str, result)))
