from colorama import init
from assistant.utils import console, parse_input, print_commands_table
from assistant.storage import load_data, save_data
from assistant.handlers import (
   add_contact,
   edit_contact, 
   delete_contact,
   search_contacts,
   show_all_contacts,
   upcoming_birthdays,
   add_note,
   edit_note,
   delete_note,
   search_notes,
   search_notes_by_tag,
   show_notes
)

COMMANDS = {
   "add-contact": {
      "handler": add_contact,
      "category": "CONTACT",
      "description": "Add new contact",
      "usage": "add-contact <name> <phone>",
   },
   "edit-contact": {
      "handler": edit_contact,
      "category": "CONTACT",
      "description": "Edit contact",
      "usage": "edit-contact <name> <field> <value>",
   },
   "delete-contact": {
      "handler": delete_contact,
      "category": "CONTACT",
      "description": "Delete contact",
      "usage": "delete-contact <name>",
   },
   "search-contact": {
      "handler": search_contacts,
      "category": "CONTACT",
      "description": "Search contacts",
      "usage": "search-contact <query>",
   },
   "all-contacts": {
      "handler": show_all_contacts,
      "category": "CONTACT",
      "description": "Show all contacts",
      "usage": "all-contacts",
   },
   "contacts-birthdays": {
      "handler": upcoming_birthdays,
      "category": "CONTACT",
      "description": "Upcoming birthdays",
      "usage": "contacts-birthdays <days>",
   },
   "add-note": {
      "handler": add_note,
      "category": "NOTE",
      "description": "Add note",
      "usage": "add-note <text>",
   },
   "edit-note": {
      "handler": edit_note,
      "category": "NOTE",
      "description": "Edit note",
      "usage": "edit-note <id> <text>",
   },
   "delete-note": {
      "handler": delete_note,
      "category": "NOTE",
      "description": "Delete note",
      "usage": "delete-note <id>",
   },
   "search-note": {
      "handler": search_notes,
      "category": "NOTE",
      "description": "Search notes",
      "usage": "search-note <query>",
   },
   "search-note-by-tag": {
      "handler": search_notes_by_tag,
      "category": "NOTE",
      "description": "Search notes by tag",
      "usage": "search-note-by-tag <tag>",
   },
   "all-notes": {
      "handler": show_notes,
      "category": "NOTE",
      "description": "Show all notes",
      "usage": "all-notes",
   },
   "help": {
      "handler": None,
      "category": "SYSTEM",
      "description": "Show help table",
      "usage": "help",
   },
   "exit": {
      "handler": None,
      "category": "SYSTEM",
      "description": "Exit program",
      "usage": "exit",
   },
   "close": {
      "handler": None,
      "category": "SYSTEM",
      "description": "Exit program",
      "usage": "close",
   },
}


def main():
   init(autoreset=True)
   contacts, notes = load_data()

   console("👋  WELCOME TO THE PERSONAL ASSISTANT!")
   print_commands_table(COMMANDS)

   while True:
      user_input = input("➤  Enter a command: ")
      command, *args = parse_input(user_input)

      if not command:
         continue

      if command in ["close", "exit"]:
         console("👋  Good bye!")
         break

      if command == "help":
         print_commands_table(COMMANDS)
         continue

      cmd = COMMANDS.get(command)

      if not cmd:
         console("Invalid command!", "error")
         continue

      handler = cmd["handler"]
      category = cmd["category"]

      if category == "CONTACT":
         handler(args, contacts)
      else:
         handler(args, notes)

      save_data(contacts, notes)
      

if __name__ == "__main__":
   main()