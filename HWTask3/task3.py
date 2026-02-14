from colorama import init, Fore


def load_logs(file_path: str) -> list:
    """
    Завантажує лог-файл та повертає його вміст у вигляді списку рядків.
    Args:
        file_path (str): Шлях до лог-файлу.
    Returns:
        list: Список рядків з лог-файлу.
    Raises:
        FileNotFoundError: Якщо файл не знайдено за вказаним шляхом
    """
    try:
        logs = list()
        with open(file_path, 'r', encoding="utf-8") as file:
            for line in file.readlines():
                logs.append(parse_log_line(line))
        return logs
    except UnicodeDecodeError:
        raise
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл за шляхом {file_path} не знайдено.")


def parse_log_line(line: str) -> dict:
    """
    Розбирає рядок з лог-файлу та повертає словник з інформацією про запит.
    Args:
        line (str): Рядок з лог-файлу.
    Returns:
        dict: Словник з інформацією про запис в протоколі, включаючи дату та час (datetime), рівень запису (level) та коментар (comment)
    """
    try:
        parts = line.split()
        return {
            "datetime": " ".join(parts[:2]),
            "level": parts[2],
            "comment": " ".join(parts[3:]),
        }
    except (IndexError, ValueError):
        raise ValueError(f"Невірний формат рядка: {line}")


def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Фільтрує лог-записи за вказаним рівнем.
    Args:
        logs (list): Список лог-записів у вигляді словників.
        level (str): Рівень для фільтрації (наприклад, "ERROR", "INFO").
    Returns:
        list: Список лог-записів, які відповідають вказаному рівню.
    """
    return [log for log in logs if log["level"] == level]


def count_logs_by_level(logs: list) -> dict:
    """
    Рахує кількість лог-записів для кожного рівня.
    Args:
        logs (list): Список лог-записів у вигляді словників.
    Returns:
        dict: Словник, де ключами є рівні логів, а значеннями - кількість записів для кожного рівня.
    """
    log_counts = {}
    for log in logs:
        level = log["level"]
        log_counts[level] = log_counts.get(level, 0) + 1
    return log_counts


def display_log_counts(counts: dict) -> str:
    """
    Виводить кількість лог-записів для кожного рівня у зручному форматі.
    Args:
        counts (dict): Словник, де ключами є рівні+  логів, а значеннями - кількість записів для кожного рівня.
    """
    init(autoreset=True)
    output = "Рівень логування | Кількість\n"
    leftpadding = len("Рівень логування ")
    output += "-" * leftpadding + "|" + "-" * len(" Кількість") + "\n"
    for level, count in counts.items():
        if level == "ERROR":
            output += f"{Fore.RED}"

        output += f"{level}{Fore.RESET}"
        output += f"{(' ' * (leftpadding - len(level)))}| {count}\n"
    return output


if __name__ == "__main__":
    pass
