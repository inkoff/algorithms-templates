# 82564736
def fibonacci(n):
    if n in (0, 1):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    n, k = int(input().split())
    print(fibonacci(n))