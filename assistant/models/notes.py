from collections import UserDict
from assistant.models import BotError, Note

class Notes(UserDict):

   def add_note(self, text, tags):
      note = Note(text, tags)
      self.data[note.id] = note
      return note


   def find(self, note_id):
      note = self.data.get(note_id)

      if not note:
         raise BotError("Note not found.")

      return note


   def delete(self, note_id):
      if note_id not in self.data:
         raise BotError("Note not found.")

      return self.data.pop(note_id)


   def search(self, query):
      query = query.lower()

      return [
         note for note in self.data.values()
         if query in note.text.lower()
      ]


   def search_by_tag(self, tag):
      return [
         note for note in self.data.values()
         if tag in note.tags
      ]


   def sort_by_tags(self, tags):
      all_notes = list(self.data.values())
      sorted_notes = []
      used_ids = set()

      for tag in tags:
         for note in all_notes:
               if note.id not in used_ids and tag in note.tags:
                  sorted_notes.append(note)
                  used_ids.add(note.id)

      for note in all_notes:
         if note.id not in used_ids:
               sorted_notes.append(note)

      return sorted_notes


   def all(self):
      return list(self.data.values())


   def __str__(self):
      if not self.data:
         return "No notes found."

      return "\n".join(str(note) for note in self.data.values())