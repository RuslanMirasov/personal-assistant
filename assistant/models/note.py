import uuid
from assistant.models import BotError

class Note:

   def __init__(self, text, tags=None):
      self.id = str(uuid.uuid4())[:8]
      self.text = text
      self.tags = tags or []


   def edit(self, new_text=None, new_tags=None):

      if not new_text and not new_tags:
         raise BotError("Nothing to update.")

      if new_text:
         self.text = new_text

      if new_tags:
         for tag in new_tags:
               if tag not in self.tags:
                  self.tags.append(tag)


   def remove_tag(self, tag):

      if tag not in self.tags:
         raise BotError("Tag not found.")

      self.tags.remove(tag)


   def __str__(self):
      tags = " ".join(self.tags) if self.tags else ""
      return f"[{self.id}] {self.text} {tags}".strip()