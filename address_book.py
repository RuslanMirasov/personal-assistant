from collections import UserDict
from datetime import datetime, timedelta

# =====================
# Base Errors
# =====================

class BotError(Exception):
    pass


# =====================
# Fields
# =====================

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value or not value.strip():
            raise BotError("Name cannot be empty.")
        
        super().__init__(value.strip())

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise BotError("Phone number must contain 10 digits.")
        
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            birthday_date = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise BotError("Invalid date format. Use DD.MM.YYYY")
        
        super().__init__(birthday_date)


# =====================
# Record
# =====================

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def add_phone(self, phone):
        for existing_phone in self.phones:
            if existing_phone.value == phone:
                raise BotError(f"User {self.name} already have this phone number.")

        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def find_phone(self, phone):
        for existing_phone in self.phones:
            if existing_phone.value == phone:
                return existing_phone
        raise BotError("Phone not found.")

    def remove_phone(self, phone):
        existing_phone = self.find_phone(phone)
        self.phones.remove(existing_phone)

    def edit_phone(self, old_phone, new_phone):
        existing_phone = self.find_phone(old_phone)
        existing_phone.value = Phone(new_phone).value
    
    def __str__(self):
        phones_str = "; ".join(p.value for p in self.phones)
        birthday_str = self.birthday.value.strftime("%d.%m.%Y") if self.birthday else "None"
        return f"Contact name: {self.name.value}, phones: {phones_str}, birthday: {birthday_str}"


# =====================
# AddressBook
# =====================

class AddressBook(UserDict):

    def add_record(self, record):
        if record.name.value in self.data:
            raise BotError(f"Record with name '{record.name.value}' already exists.")
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name not in self.data:
            raise BotError(f"Record with name '{name}' not found.")
        del self.data[name]

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming = []

        for record in self.data.values():
            if record.birthday is None:
                continue

            birthday_date = record.birthday.value 
            birthday_this_year = birthday_date.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            days_until = (birthday_this_year - today).days

            if 0 <= days_until <= 7:
                congratulation_date = birthday_this_year

                weekday = congratulation_date.weekday()
                if weekday == 5:
                    congratulation_date += timedelta(days=2)
                elif weekday == 6:
                    congratulation_date += timedelta(days=1)

                upcoming.append({
                    "name": record.name.value,
                    "congratulation_date": congratulation_date.strftime("%d.%m.%Y")
                })

        return sorted(
            upcoming,
            key=lambda item: datetime.strptime(item["congratulation_date"], "%d.%m.%Y").date()
        )

    def __str__(self):
        if not self.data:
            return "Address book is empty."
        return "\n".join(str(record) for record in self.data.values())