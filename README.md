# 💸 Personal Expense Tracker

A simple, interactive **Command Line Interface (CLI)** application built with **Python** to help users record, manage, and analyze their daily expenses. The application stores data in a JSON file, making it lightweight and easy to use without requiring a database.

---

## 📌 Features

* ➕ Add new expenses
* 📋 View all recorded expenses
* 🗑️ Delete existing expenses
* 📊 Expense summary and analytics
* 📅 Monthly expense tracking
* 🏷️ Categorize expenses
* 💰 Automatic total expense calculation
* 📈 Average expense calculation
* 💾 Persistent data storage using JSON
* ✅ Input validation and error handling

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Data Storage:** JSON
* **Modules Used:**

  * json
  * os
  * datetime

---

## 📂 Project Structure

```text
Expense-Tracker/
│
├── Expense-Tracker.py      # Main application
├── expenses.json           # Stores expense data (generated automatically)
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8 or above

Verify Python installation:

```bash
python --version
```

or

```bash
python3 --version
```

---

### Installation

1. Clone the repository

```bash
git clone https://github.com/RITESH-KUMAR-SRIVASTAVA/Expense-Tracker.git
```

2. Navigate to the project directory

```bash
cd Expense-Tracker
```

3. Run the application

```bash
python Expense-Tracker.py
```

or

```bash
python3 Expense-Tracker.py
```

---

## 📸 Sample Menu

```text
==================================================
      💸 PERSONAL EXPENSE TRACKER 💸
==================================================

MENU

1. Add an Expense
2. View All Expenses
3. Delete an Expense
4. Show Summary / Report
5. Exit
```

---

## 📊 Expense Summary

The application provides useful statistics including:

* Grand Total Expenses
* Category-wise Spending
* Monthly Expense Report
* Average Expense
* Expense Breakdown by Category

---

## 💾 Data Storage

All expenses are stored in a local JSON file.

Example:

```json
[
  {
    "id": 1720012345.12,
    "description": "Lunch",
    "amount": 250,
    "category": "Food & Drinks",
    "date": "2026-07-04"
  }
]
```

---

## 📚 Concepts Demonstrated

This project demonstrates:

* Functions
* File Handling
* JSON Operations
* Exception Handling
* Loops
* Dictionaries
* Lists
* Input Validation
* Menu-Driven Programming
* Data Processing
* Modular Programming Practices

---

## 👨‍💻 Author

Ritesh Kumar Srivastava

* GitHub: https://github.com/RITESH-KUMAR-SRIVASTAVA

---

Your support is appreciated!
