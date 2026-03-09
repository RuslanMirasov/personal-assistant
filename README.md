# Personal Assistant

**Personal Assistant** is a Python-based command-line application for managing contacts and notes in a simple and efficient way.
The tool allows users to store contact details, validate phone numbers and emails, track upcoming birthdays,
and organize notes with search and tagging features — all directly from the terminal.

## Setup

Clone the repository and go to the project folder.

```bash
git clone https://github.com/RuslanMirasov/personal-assistant.git
cd personal-assistant
```

## Create virtual environment

Windows (Git Bash / PowerShell / CMD)

```bash
python -m venv .venv
```

## Activate virtual environment

### Git Bash

```bash
source .venv/Scripts/activate
```

### PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### CMD

```cmd
.venv\Scripts\activate
```

After activation you should see:

```
(.venv)
```

in your terminal.

## Install project

```bash
pip install -e .
```

This installs the project in **editable mode** and installs all dependencies from `pyproject.toml`.

## Run

```bash
assistant
```

## Available Commands

### SYSTEM COMMANDS

```bash
┌──────────────────────────────┬──────────────────────┐
│ Command                      │ Description          │
├──────────────────────────────┼──────────────────────┤
│ help                         │ Shows commands table │
│ exit                         │ Exit program         │
│ close                        │ Exit program         │
└──────────────────────────────┴──────────────────────┘
```

### CONTACT COMMANDS

```bash
┌──────────────────────────────┬──────────────────────┐
│ Command                      │ Description          │
├──────────────────────────────┼──────────────────────┤
│ add-contact <name> <phone>   │ Add new contact      │
│ edit-contact <name> <field>  │ Edit contact         │
│ delete-contact <name>        │ Delete contact       │
│ search-contact <query>       │ Search contacts      │
│ all-contacts                 │ Show all contacts    │
│ contacts-birthdays <days>    │ Upcoming birthdays   │
└──────────────────────────────┴──────────────────────┘
```

### NOTE COMMANDS

```bash
┌──────────────────────────────┬──────────────────────┐
│ Command                      │ Description          │
├──────────────────────────────┼──────────────────────┤
│ add-note <text>              │ Add note             │
│ edit-note <id> <text>        │ Edit note            │
│ delete-note <id>             │ Delete note          │
│ search-note <query>          │ Search notes         │
│ search-note-by-tag <tag>     │ Search notes by tag  │
│ all-notes                    │ Show all notes       │
└──────────────────────────────┴──────────────────────┘
```

## Project structure:

```bash
assistant
├─ handlers
├─ models
├─ storage
├─ validators
├─ utils
└─ main.py
```
