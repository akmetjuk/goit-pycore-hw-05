from HWTask1 import Fibonachi
from HWTask2 import task2
from HWTask3 import task3
import sys
import pathlib

if __name__ == "__main__":
    current_dir = pathlib.Path(__file__).parent
    print(f"{'=' * 8} task #1 checking")

    # Отримуємо функцію fibonacci
    fib = Fibonachi.caching_fibonacci()

    # Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610

    print(f"{'=' * 8} task #2 checking")
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = task2.sum_profit(text, task2.generator_numbers)
    print(f"Загальний дохід: {total_income}")

    print(f"{'=' * 8} task #2 checking with no numbers")
    text = "У цьому тексті немає чисел, лише слова та символи."
    total_income = task2.sum_profit(text, task2.generator_numbers)  
    print(f"Загальний дохід: {total_income}")

    print(f"{'=' * 8} task #3 checking")
    
    args = sys.argv[1:]  # Отримуємо аргументи командного рядка, пропускаючи ім'я скрипта
    try:
        path = args[0] if args else current_dir / "HWTask3" / "Log.txt"
        filter = args[1].upper().strip() if len(args) > 1 else "ERROR"
    except:
        pass

    logs = task3.load_logs(path)
    log_counts = task3.count_logs_by_level(logs)
    print(task3.display_log_counts(log_counts))

    print(f"Деталі логів для рівня '{filter}'")
    error_logs = task3.filter_logs_by_level(logs, filter)
    for log in error_logs: 
        print(f"{log['datetime']} - {log['comment']}")
