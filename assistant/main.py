from colorama import init
from assistant.utils import console, parse_input
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
   # CONTACT COMMANDS
    "add-contact": add_contact,
    "edit-contact": edit_contact,
    "delete-contact": delete_contact,
    "search-contact": search_contacts,
    "all-contacts": show_all_contacts,
    "contacts-birthdays": upcoming_birthdays,
   # NOTES COMMANDS
    "add-note": add_note,
    "edit-note": edit_note,
    "delete-note": delete_note,
    "search-note": search_notes,
    "search-note-by-tag": search_notes_by_tag,
    "all-notes": show_notes,
}



def main():
   init(autoreset=True)
   contacts, notes = load_data()

   console("👋  Welcome to the personal assistant!")

   while True:
      user_input = input("➤  Enter a command: ")
      command, *args = parse_input(user_input)

      if command in ["close", "exit"]:
         console("👋  Good bye!")
         break

      if command in ["hello", "hi"]:
         console("How can I help you?")
         continue

      handler = COMMANDS.get(command)

      if not handler:
         console("Invalid command.", "error")
         continue

      if "contact" in command:
         handler(args, contacts)
      else:
         handler(args, notes)

      save_data(contacts, notes)
      

if __name__ == "__main__":
   main()