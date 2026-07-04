# 💸 EXPENSE TRACKER — CLI

A command-line expense tracker written in Python. Add, view, delete and analyse your daily expenses — all from your terminal.

## Features

- **➕ Add expenses** — description, amount (₹), category, date
- **📋 View all expenses** — formatted table with total
- **🗑️ Delete expenses** — pick by number
- **📊 Summary report** — grand total, category breakdown (with %), monthly breakdown, average per expense
- **💾 Persistent storage** — data saves to `expenses.json`, survives restart

## Quick Start

```bash
python3 EXPENSE-TRACKER.py
```

No dependencies required. Python 3 only.

## How to Use

```
  MENU:
    1. ➕ Add an expense
    2. 📋 View all expenses
    3. 🗑️  Delete an expense
    4. 📊 Show summary / report
    5. 🚪 Exit
```

Press the number and follow prompts.

## Project Structure

```
├── EXPENSE-TRACKER.py   # Main program
├── expenses.json        # Data file (auto-created)
├── README.md            # This file
└── .gitignore
```

## What I Learned Building This

| Concept | Usage |
|---------|-------|
| Functions | `add_expense()`, `view_expenses()`, etc. |
| Lists & Dictionaries | Storing categories, expense records |
| File I/O (JSON) | Reading/writing `expenses.json` |
| Loops | `while True` menu loop |
| Error handling | `try/except` for invalid input |
| f-strings | `f"₹{amount:.2f}"` formatting |
| `datetime` | Auto-filling today's date |

