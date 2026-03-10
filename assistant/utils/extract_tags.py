from assistant.validators import validate_tag

def extract_tags(words):

    tags = []
    text_words = []

    for word in words:
        if word.startswith("#"):
            validate_tag(word)
            tags.append(word)
        else:
            text_words.append(word)

    text = " ".join(text_words)

    return text, tags