from assistant.utils import console, input_error, extract_tags, print_notes_table
from assistant.validators import validate_args, validate_tag

@input_error
def add_note(args, notes):
    validate_args(args, 1, "Give me Note text.")

    text, tags = extract_tags(args)

    for tag in tags:
        validate_tag(tag)

    note = notes.add_note(text, tags)

    console(f"Note added with id {note.id}", "success")


@input_error
def edit_note(args, notes):
    validate_args(args, 1, "Give me Note ID.")

    note_id = args[0]
    text, tags = extract_tags(args[1:])

    for tag in tags:
        validate_tag(tag)

    note = notes.find(note_id)

    note.edit(
        new_text=text if text else None,
        new_tags=tags if tags else None
    )

    console("Note updated.", "success")


@input_error
def delete_note(args, notes):
    validate_args(args, 1, "Give me Note ID.")

    note_id = args[0]
    notes.delete(note_id)

    console("Note deleted.", "success")

@input_error
def remove_tag(args, notes):
    validate_args(args, 2, "Give me Note ID and Tag.")

    note_id = args[0]
    tag = args[1]

    validate_tag(tag)

    note = notes.find(note_id)
    note.remove_tag(tag)

    console("Tag removed.", "success")


@input_error
def search_notes(args, notes):
    validate_args(args, 1, "Give me search query.")

    query = " ".join(args)
    results = notes.search(query)

    print_notes_table(results)


@input_error
def search_notes_by_tag(args, notes):
    validate_args(args, 1, "Give me Tag.")

    tag = args[0]
    validate_tag(tag)
    results = notes.search_by_tag(tag)

    print_notes_table(results)


@input_error
def sort_notes_by_tags(args, notes):
    validate_args(args, 1, "Give me at least one tag.")

    for tag in args:
        validate_tag(tag)

    sorted_notes = notes.sort_by_tags(args)
    print_notes_table(sorted_notes)


@input_error
def show_notes(args, notes):
    all_notes = notes.all()
    print_notes_table(all_notes)