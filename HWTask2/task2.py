from typing import Callable


def is_float(value: str) -> bool:
    """Перевіряє, чи є рядок числом з плаваючою точкой.
    Args:
        value (str): Рядок для перевірки.
    Returns:
        bool: True, якщо рядок є числом з плаваючою точкой, інакше False.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


def generator_numbers(text: str):
    """
    Генератор, який витягує числа з рядка тексту.
    Args:
        text (str): Вхідний рядок тексту.
    Yields:
        float: Числа, знайдені в тексті.
    """
    for word in text.split(" "):
        if is_float(word):
            yield float(word)


def sum_profit(text: str, func: Callable) -> float:
    """
    Обчислює суму чисел, знайдених у тексті за допомогою переданої функції.
    Args:
        text (str): Вхідний рядок тексту.
        func (Callable): Функція, яка генерує числа з тексту.
    Returns:
        float: Сума чисел, знайдених у тексті.
    """
    return sum(func(text))


if __name__ == "__main__":
    pass
