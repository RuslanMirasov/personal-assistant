from assistant.utils import console, input_error
from assistant.validators import validate_args

@input_error
def add_contact(args, contacts):
    validate_args(args, 2, "Give me name and phone please.")
    return console("add_contact called", "success")


@input_error
def edit_contact(args, contacts):
    validate_args(args, 3, "Give me name, field and new value.")
    return console("edit_contact called", "success")


@input_error
def delete_contact(args, contacts):
    validate_args(args, 1, "Give me contact name.")
    return console("delete_contact called", "success")


@input_error
def search_contacts(args, contacts):
    validate_args(args, 1, "Give me search query.")
    return console("search_contacts called", "success")


@input_error
def show_all_contacts(args, contacts):
    return console("show_all_contacts called", "success")


@input_error
def upcoming_birthdays(args, contacts):
    validate_args(args, 1, "Give me number of days.")
    return console("upcoming_birthdays called", "success")