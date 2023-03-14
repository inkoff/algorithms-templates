# 82718941
ERROR_MESSAGE = 'error'
ERROR_COMMAND = 'Error in command: {command}'


class Deque:
    def __init__(self, max_size):
        self.__items = [None] * max_size
        self.__max_size = max_size
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def __check_full_queue(self):
        return self.__size == self.__max_size

    def __check_empty_queue(self):
        return self.__size == 0

    def push_front(self, value):
        if self.__check_full_queue():
            raise RuntimeError(ERROR_MESSAGE)
        if not self.__check_empty_queue():
            self.__head = (self.__head - 1) % self.__max_size
        if self.__check_empty_queue():
            self.__head = 0
            self.__tail = 0
        self.__items[self.__head] = value
        self.__size += 1

    def push_back(self, value):
        if self.__check_full_queue():
            raise RuntimeError(ERROR_MESSAGE)
        if not self.__check_empty_queue():
            self.__tail = (self.__tail + 1) % self.__max_size
        if self.__check_empty_queue():
            self.__head = 0
            self.__tail = 0
        self.__items[self.__tail] = value
        self.__size += 1

    def pop_front(self):
        if self.__check_empty_queue():
            raise RuntimeError(ERROR_MESSAGE)
        value = self.__items[self.__head]
        self.__head = (self.__head + 1) % self.__max_size
        self.__size -= 1
        return value

    def pop_back(self):
        if self.__check_empty_queue():
            raise RuntimeError(ERROR_MESSAGE)
        value = self.__items[self.__tail]
        self.__tail = (self.__tail - 1) % self.__max_size
        self.__size -= 1
        return value


if __name__ == '__main__':
    command_count = int(input())
    deque = Deque(max_size=int(input()))
    for _ in range(command_count):
        try:
            command, *params = input().strip().split(' ')
            result = getattr(deque, command)(*params)
            if 'pop' in command:
                print(result)
        except RuntimeError:
            print(ERROR_MESSAGE)
        except AttributeError:
            raise ValueError(ERROR_COMMAND.format(command=command))
