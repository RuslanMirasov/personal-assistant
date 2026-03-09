import pickle
from pathlib import Path

DATA_DIR = Path.home() / ".personal_assistant"
CONTACTS_FILE = DATA_DIR / "contacts.pkl"
NOTES_FILE = DATA_DIR / "notes.pkl"

def ensure_data_dir():
    DATA_DIR.mkdir(exist_ok=True)

def load_data():
    ensure_data_dir()

    if CONTACTS_FILE.exists():
        with open(CONTACTS_FILE, "rb") as f:
            contacts = pickle.load(f)
    else:
        contacts = {}

    if NOTES_FILE.exists():
        with open(NOTES_FILE, "rb") as f:
            notes = pickle.load(f)
    else:
        notes = {}

    return contacts, notes


def save_data(contacts, notes):
    ensure_data_dir()

    with open(CONTACTS_FILE, "wb") as f:
        pickle.dump(contacts, f)

    with open(NOTES_FILE, "wb") as f:
        pickle.dump(notes, f)