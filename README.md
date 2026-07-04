# 💸 Personal Expense Tracker (Beginner Python Project)

A command-line app that:
- ✅ Adds expenses (description, amount, category, date)
- ✅ Views all expenses in a table
- ✅ Deletes expenses
- ✅ Shows a summary (total, category breakdown, monthly spending)

Your data is saved in `expenses.json` — it stays even after you close the program.

---

## 📘 TABLE OF CONTENTS

1. [What You Need (No Knowledge Required)](#1-what-you-need)
2. [How to Run This Project](#2-how-to-run-this-project)
3. [How to Use the Expense Tracker](#3-how-to-use-the-expense-tracker)
4. [What Each Part of the Code Does](#4-what-each-part-of-the-code-does)
5. [How to Push This Project to GitHub](#5-how-to-push-this-project-to-github)
6. [How to Deploy This Project Online](#6-how-to-deploy-this-project-online-free)
7. [How to Make More Python Projects (Next Steps)](#7-how-to-make-more-python-projects)
8. [Project Ideas to Try Next](#8-project-ideas-to-try-next)

---

## 1. What You Need

Zero experience required. You just need:

| Thing | Do you have it? | How to check |
|-------|-----------------|-------------|
| **Python 3** | ✅ Yes | Open Terminal and type: `python3 --version` |
| **A text editor** (VS Code) | ✅ Yes | You're using VS Code right now |
| **Git** (to push to GitHub) | ❓ Maybe | Open Terminal and type: `git --version` |

> **If Git is not installed:** Download from https://git-scm.com/download/mac — install it using the default options (next → next → install).

> **If you don't have a GitHub account:** Go to https://github.com/signup and create one (free).

---

## 2. How to Run This Project

### ⚠️ IMPORTANT: Your folder path has an apostrophe (RITESH's)

Because of this, you should use the **VS Code terminal** instead of the Mac Terminal app — VS Code's terminal is ALREADY in the right folder.

### Method A: Use VS Code's built-in terminal (EASIEST — use this)

1. In VS Code, go to **Terminal → New Terminal** (or press `` Ctrl+` ``)
2. The terminal will open in the correct folder automatically
3. Just type:
   ```bash
   python3 Pro.py
   ```

### Method B: Use the Mac Terminal app

If you must use the Mac Terminal app, copy-paste this EXACT command (all one line):

```bash
cd "/Users/riteshkumarsrivastava/Documents/Documents - RITESH's MacBook Air/Developer/Python/PROJECTS"
```

Then type:
```bash
python3 Pro.py
```

> 🟢 **The path is in double-quotes** which handles the apostrophe correctly.

That's it. You'll see a menu. Choose options 1-5 and press Enter.

---

## 3. How to Use the Expense Tracker

### Add an expense (option 1)
```
  Description: Coffee
  Amount: ₹150
  Categories:
    1. Food & Drinks
    2. Transport
    3. Shopping
    4. Bills & Utilities
    5. Entertainment
    6. Health
    7. Education
    8. Rent
    9. Other
  Choose category number: 1
  Date (YYYY-MM-DD, press Enter for today): [press Enter]
  ✅ Added: Coffee — ₹150.00 [Food & Drinks]
```

### View all expenses (option 2)
Shows a table with all your expenses and a total at the bottom.

### Delete an expense (option 3)
Shows the table, then asks for the `#` number to delete.

### Show summary (option 4)
Shows:
- Grand total
- Breakdown by category (with percentages)
- Breakdown by month
- Average per expense

### Exit (option 5)
Closes the program.

---

## 4. What Each Part of the Code Does

Here is `Pro.py` explained in plain English (you don't need to memorize this):

### Imports (top of file)
```python
import json          # lets us save data to a file
import os            # lets us check if a file exists
from datetime import datetime, date  # handles dates/times
```

### `load_expenses()` and `save_expenses()`
- `load_expenses()` → opens `expenses.json` and reads your expenses
- `save_expenses()` → writes your expenses back to `expenses.json`
- If `expenses.json` doesn't exist yet, `load_expenses()` returns an empty list

### `get_amount()`
- Asks the user for a number
- If they type "abc" (not a number), it says "❌" and asks again
- Won't accept 0 or negative numbers

### `get_category()`
- Shows a numbered list of categories
- Asks the user to pick one (1-9)
- Keeps asking until they pick a valid number

### `add_expense()`
- Asks for description, amount, category, date
- Creates a dictionary (like a mini database record)
- Saves it to `expenses.json`

### `view_expenses()`
- Loads all expenses and prints them in a formatted table
- Shows the total at the bottom

### `delete_expense()`
- Shows the table
- Asks which # to delete
- Removes it from the list and saves

### `show_summary()`
- Calculates total, category breakdown, monthly breakdown, average

### `main()`
- Shows the menu in a loop
- Keeps running until the user picks option 5

### `if __name__ == "__main__":`
- This is the **entry point** — Python starts here

### Concepts you just learned by reading this code:
| Concept | What it means |
|---------|---------------|
| Variable | A named box that holds a value (e.g., `description = "Coffee"`) |
| Function | A reusable block of code (e.g., `def add_expense():`) |
| List | An ordered collection `["Food", "Transport", ...]` |
| Dictionary | A key-value map `{"description": "Coffee", "amount": 150}` |
| Loop | Repeating something (e.g., `while True:` runs forever until `break`) |
| If/else | Making decisions (`if choice == "1":`) |
| Try/except | Handling errors gracefully |
| File I/O | Reading/writing files (`open()`, `json.load()`, `json.dump()`) |
| `input()` | Getting text from the user |
| `f-string` | Formatted strings: `f"Total: ₹{total}"` |

---

## 5. How to Push This Project to GitHub

### First time ever using Git? Start here:

#### Step 1: Set up Git (do this ONCE on your computer)
```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

> Use whatever name/email you used for GitHub.

#### Step 2: Create a new repository on GitHub
1. Go to https://github.com — log in
2. Click the green **"New"** button (or + icon → New repository)
3. **Repository name:** `expense-tracker`
4. **Description (optional):** `A personal expense tracker CLI app in Python`
5. **Public** ✅ (select Public)
6. **DO NOT** check "Initialize this repository with a README" (we already have one)
7. Click **"Create repository"**

#### Step 3: Connect your local folder to GitHub & push

Run these commands in Terminal **one by one**:

```bash
# Go to your project folder
cd /Users/riteshkumarsrivastava/Documents/Documents\ -\ RITESH\'s\ MacBook\ Air/Developer/Python/PROJECTS

# Initialize Git in this folder (only needed once)
git init

# Add all your files to the "staging area"
git add Pro.py README.md

# (Optional) Create a .gitignore file so you don't upload expenses.json
echo "expenses.json" > .gitignore
git add .gitignore

# Commit the files (save a snapshot)
git commit -m "Initial commit: Expense Tracker CLI app"

# Tell Git where your GitHub repo is
git remote add origin https://github.com/RITESH-KUMAR-SRIVASTAVA/expense-tracker.git

# Push your code to GitHub
git push -u origin main
```


> 💡 If Git asks for a username/password, use a **Personal Access Token** (not your regular password):
> 1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
> 2. Generate new token, check `repo`, copy it
> 3. Paste the token when asked for password

#### Step 4: Verify
Go to `https://github.com/RITESH-KUMAR-SRIVASTAVA/expense-tracker` — you should see your files.

### After making changes (adding features, fixing bugs):

```bash
git add Pro.py
git commit -m "Added feature: export to CSV"
git push
```

Three commands. That's it.

---

## 6. How to Deploy This Project Online (Free)

A CLI app runs in **your terminal**. To let **other people use it online**, you have options:

### Option A: Run on Replit (easiest, free)
1. Go to https://replit.com/~ — sign up (free)
2. Click **"Create Repl"** → Choose **"Import from GitHub"**
3. Paste your GitHub URL: `https://github.com/RITESH-KUMAR-SRIVASTAVA/expense-tracker`
4. Click **"Import from GitHub"**
5. Click **"Run"** button — it works instantly
6. Share the URL with anyone

### Option B: Turn it into a Web App (for beginners who want to learn Flask)
This is a NEXT STEP project. But here's the overview:
- Install Flask: `pip3 install flask`
- Create a simple web page with buttons instead of terminal prompts
- Deploy on Render/Railway for free

---

## 7. How to Make More Python Projects

Here is the **process** you follow for ANY project:

### Step 1: Pick a tiny idea
Don't try to build "YouTube" or "Instagram." Start with something that fits in one file.

### Step 2: Plan on paper first
```
What does it do? (e.g. "A to-do list that saves tasks to a file")
What are the features? (add task, view tasks, delete task, mark done)
What data do I need? (task name, done/not done, date)
```

### Step 3: Write the skeleton
```python
def add_task(): pass
def view_tasks(): pass
def delete_task(): pass
def main(): pass
```

### Step 4: Fill in one function at a time
- Write `add_task()` — test it
- Write `view_tasks()` — test it
- Keep going

### Step 5: Test after EVERY change
Run your program after every function. Fix errors immediately.

### Step 6: Add file saving LAST
Make it work in memory first (data disappears when you close). Save to a file only after everything works.

---

## 8. Project Ideas to Try Next

| Project | What you learn | Difficulty |
|---------|---------------|-----------|
| **To-Do List** | Lists, file I/O, user input | ⭐ Easy |
| **Password Generator** | Random module, strings, loops | ⭐ Easy |
| **Quiz Game** | Dictionaries, scoring, conditionals | ⭐⭐ Medium |
| **Notes App** | File I/O, search, timestamps | ⭐⭐ Medium |
| **Weather CLI** | API calls (requests library), JSON | ⭐⭐ Medium |
| **Flashcard App** | CSV reading, spaced repetition | ⭐⭐⭐ Harder |
| **Expense Tracker Web App** (Flask) | Flask, HTML, CSS, deployment | ⭐⭐⭐ Harder |

Each one builds on the previous. Try them in order.

---

## 🧠 Quick Reference: Common Terminal Commands

```bash
pwd                     # Print working directory (where am I?)
ls                      # List files in current folder
ls -la                  # List all files (including hidden)
cd folder_name          # Go into a folder
cd ..                   # Go up one folder
cd ~                    # Go to your home folder
mkdir my_project        # Create a new folder
python3 file.py         # Run a Python file
code .                  # Open VS Code in current folder
clear                   # Clear the terminal screen
```

---

## ✅ You've Got This

You have:
- ✅ A working Python program
- ✅ The complete code explained line-by-line
- ✅ Step-by-step instructions to run it
- ✅ Instructions to push to GitHub
- ✅ Instructions to deploy on Replit
- ✅ A roadmap to learn more

**Your next step right now:** Open Terminal and run `python3 Pro.py`. Try adding 3 expenses and viewing the summary. That's all.

Then push it to GitHub. Then try the To-Do List project.
