from functools import wraps
from address_book import BotError, Record

# Декоратор для обробки помилок введення користувача
def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BotError as error:
            return str(error)

    return inner

# Функція розбору введеної команди
def parse_input(user_input):
   cmd, *args = user_input.split()
   cmd = cmd.strip().lower()
   return cmd, *args

# Функція валідує аргументи по кількості
def validate_args(args, expected_count, message):
    if len(args) < expected_count:
        raise BotError(message)

# Обробник команди додавання контакту
@input_error
def add_contact(args, book):
    validate_args(args, 2, "Give me name and phone please.")

    name, phone = args[:2]
    record = book.find(name)

    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    else:
        message = "Contact updated."

    record.add_phone(phone)
    return message

# Обробник команди зміни контакту
@input_error
def change_contact(args, book):
    validate_args(args, 3, "Give me name, old phone and new phone.")

    name, old_phone, new_phone = args[:3]
    record = book.find(name)

    if record is None:
        raise BotError("Contact not found.")

    record.edit_phone(old_phone, new_phone)
    return "Contact updated."

# Обробник команди перегляду телефону контакту
@input_error
def show_phone(args, book):
    validate_args(args, 1, "Enter user name.")

    name = args[0]
    record = book.find(name)

    if record is None:
        raise BotError("Contact not found.")

    if not record.phones:
        return "No phones found."

    return "; ".join(p.value for p in record.phones)

# Обробник команди виведення всіх контактів  
@input_error
def show_all(args, book):
    if not book.data:
        return "No contacts found."
    return str(book)

# Обробник команди додавання дня народження контакту
@input_error
def add_birthday(args, book):
    validate_args(args, 2, "Give me name and birthday.")

    name, birthday = args[:2]
    record = book.find(name)

    if record is None:
        raise BotError("Contact not found.")

    record.add_birthday(birthday)
    return "Birthday added."

# Обробник команди перегляду дня народження контакту
@input_error
def show_birthday(args, book):
    validate_args(args, 1, "Enter user name.")

    name = args[0]
    record = book.find(name)

    if record is None:
        raise BotError("Contact not found.")

    if record.birthday is None:
        raise BotError("Birthday not set.")

    return record.birthday.value.strftime("%d.%m.%Y")

# Обробник команди виведення найближчих днів народження
@input_error
def birthdays(args, book):
    upcoming = book.get_upcoming_birthdays()

    if not upcoming:
        return "No upcoming birthdays."

    return "\n".join(
        f"{item['name']}: {item['congratulation_date']}"
        for item in upcoming
    )