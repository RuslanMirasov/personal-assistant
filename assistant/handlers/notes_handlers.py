from assistant.utils import console, input_error
from assistant.validators import validate_args

@input_error
def add_note(args, notes):
   validate_args(args, 1, "Give me Note text.")
   text = " ".join(args)
   return console(f"add_note called: {text}", "success")


@input_error
def edit_note(args, notes):
   validate_args(args, 2, "Give me Note ID and new text.")
   note_id = args[0]
   text = " ".join(args[1:])
   return console(f"edit_note called: id={note_id}, text={text}", "success")


@input_error
def delete_note(args, notes):
   validate_args(args, 1, "Give me Note ID.")
   note_id = args[0]
   return console(f"delete_note called: id={note_id}", "success")


@input_error
def search_notes(args, notes):
   validate_args(args, 1, "Give me search query.")
   query = " ".join(args)
   return console(f"search_notes called: {query}", "success")


@input_error
def search_notes_by_tag(args, notes):
   validate_args(args, 1, "Give me Tag.")
   tag = args[0]
   return console(f"search_notes_by_tag called: {tag}", "success")


@input_error
def show_notes(args, notes):
   return console("show_notes called", "success")