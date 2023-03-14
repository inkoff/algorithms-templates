def get_longest_word(line: str) -> str:
    words = line.split()
    length: int = len(words)
    if length == 1:
        return ''.join(words)
    current_word: str = words[0]
    for i in range(1, length):
        if len(words[i]) > len(current_word):
            current_word = words[i]
    return current_word


def read_input() -> str:
    _ = input()
    line = input().strip()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


print_result(get_longest_word(read_input()))
