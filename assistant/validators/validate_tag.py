import re
from assistant.models import BotError

TAG_PATTERN = r"^#[a-zA-Z0-9_]+$"

def validate_tag(tag):
    if not re.match(TAG_PATTERN, tag):
        raise BotError("Invalid tag format. Tag must start with #")