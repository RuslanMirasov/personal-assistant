from colorama import Fore
from tabulate import tabulate

def console(message, type="message"):
    if type == "error":
        print(f"{Fore.LIGHTRED_EX}⚠  {message}")

    elif type == "success":
        print(f"{Fore.LIGHTGREEN_EX}✅  {message}")

    else:
        print(f"{Fore.LIGHTBLUE_EX}{message}")



def print_commands_table(commands):

    categories = {
        "CONTACT": [],
        "NOTE": [],
        "SYSTEM": []
    }

    for cmd in commands.values():
        categories[cmd["category"]].append([
            cmd["usage"],
            cmd["description"]
        ])

    tables = []

    for category in ["CONTACT", "NOTE", "SYSTEM"]:
        tables.append(
            tabulate(
                categories[category],
                headers=["Command", "Description"],
                tablefmt="simple"
            )
        )

    console(
        tabulate(
            [tables],
            headers=["CONTACT COMMANDS", "NOTE COMMANDS", "SYSTEM COMMANDS"],
            tablefmt="fancy_grid"
        )
    )


def print_notes_table(notes):

    if not notes:
        console("No notes found.", "error")
        return

    table = []

    for note in notes:
        tags = " ".join(note.tags) if note.tags else "-"
        table.append([
            note.id,
            note.text,
            tags
        ])

    console(
        tabulate(
            table,
            headers=["NOTE ID", "NOTE TEXT", "NOTE TAGS"],
            tablefmt="fancy_grid"
        )
    )