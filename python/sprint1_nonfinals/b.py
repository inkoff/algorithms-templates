def check_parity(a: int, b: int, c: int) -> bool:
    a = a % 2 == 0
    b = b % 2 == 0
    c = c % 2 == 0
    return a == b and b == c


def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")


a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
