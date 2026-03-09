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