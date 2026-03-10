from functools import wraps
from assistant.models import BotError
from assistant.utils import console


def input_error(func):
   @wraps(func)
   def inner(*args, **kwargs):
      try:
         return func(*args, **kwargs)
      except BotError as error:
         return console(str(error), "error")

   return inner