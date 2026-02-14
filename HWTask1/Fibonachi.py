from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    """
    Функція для обчислення чисел Фібоначчі з використанням кешування результатів.

    Returns:
        Callable[[int], int]: Функція, яка обчислює число Фібоначчі для заданого значення x.
    """
    cachedresult = {0: 0, 1: 1}

    def inner(x: int) -> int:
        # використовуємо nonlocal, щоб змінити змінну в замиканні
        nonlocal cachedresult
        if cachedresult.get(x):
            return cachedresult[x]

        result = fibonacci(x)
        cachedresult[x] = result
        return result

    return inner


def fibonacci(x: int) -> int:
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)


if __name__ == "__main__":
    pass
