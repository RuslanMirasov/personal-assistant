from functools import wraps
from assistant.models.bot_error import BotError
from assistant.utils.console import console


def input_error(func):
   @wraps(func)
   def inner(*args, **kwargs):
      try:
         return func(*args, **kwargs)
      except BotError as error:
         return console(str(error), "error")

   return inner