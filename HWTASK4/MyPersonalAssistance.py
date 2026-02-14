import re

__commands__ = ["hello", "add", "change", "phone", "help", "all", "close", "exit"]


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError as e:
            return f"Key error: {e}"
        except IndexError:
            return "Enter the argument for the command"
    return inner


def normalize_phone(phone_number: str) -> str:
    """Нормалізувати номер телефону та додати префікс +38.

    Args:
        phone_number: Телефонний номер з будь-якими символами

    Returns:
        Нормалізований номер у форматі +38XXXXXXXXXX

    Raises:
        ValueError: Якщо не вдалося виділити 10-значний номер
    """
    pattern = r'\d+'
    ph = ''.join(re.findall(pattern, phone_number))
    if not ph.startswith('38'):
        ph = f'38{ph}'
    if len(ph) != 12:
        raise ValueError(f'unable to extract phone number => {phone_number}')
    return f"+{ph}"


@input_error
def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 2:
        raise IndexError("Invalid number of arguments. Expecting NAME and PHONE.")
    name, phone = args
    if name in contacts:
        raise KeyError("Contact already exists.")
    try:
        phone = normalize_phone(phone)
    except ValueError:
        raise ValueError(f"Invalid phone number: {phone}")
    contacts[name] = phone
    return f"Contact '{name}' added."


@input_error
def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 2:
        raise ValueError("Invalid number of arguments. Expecting NAME and PHONE.")
    name, phone = args
    if name not in contacts:
        raise KeyError(f"Contact '{name}' not found.")
    try:
        phone = normalize_phone(phone)
    except ValueError:
        raise ValueError(f"Invalid phone number: {phone}")
    contacts[name] = phone
    return f"Contact '{name}' updated."


@input_error
def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 1:
        raise IndexError("Invalid number of arguments. Expecting NAME.")
    name = args[0]
    if name not in contacts:
        raise KeyError(f"Contact '{name}' not found.")
    return contacts[name]


def show_all(contacts: dict[str, str]) -> str:
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def parse_input(user_input: str) -> tuple[str, ...]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    if cmd not in __commands__:
        raise ValueError(f"Invalid command. Use the following commands: {', '.join(__commands__)}")
    return cmd, *args


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")

        try:
            command, *args = parse_input(user_input)
        except ValueError as e:
            print(e)
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "help":
            print(f"Use the following commands: {', '.join(__commands__)}")


if __name__ == "__main__":
    main()
