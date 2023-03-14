from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    tmp = list(longer)
    for c in shorter:
        if c in longer:
            tmp.remove(c)
    return ''.join(tmp)


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
