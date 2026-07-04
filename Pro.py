#!/usr/bin/env python3
"""
Personal Expense Tracker
A CLI tool to track, view, and analyze daily expenses.
Run it with: python3 Pro.py
"""

import json
import os
from datetime import datetime, date

# ============================================================
# FILE WHERE EXPENSES ARE STORED
# ============================================================
DATA_FILE = "expenses.json"


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def load_expenses():
    """Load expenses from the JSON file. Returns empty list if file doesn't exist."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_expenses(expenses):
    """Save the expenses list to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)


def get_amount():
    """Ask user for a valid amount (positive number)."""
    while True:
        try:
            amt = float(input("  Amount: ₹"))
            if amt <= 0:
                print("  ❌ Amount must be greater than 0.")
                continue
            return amt
        except ValueError:
            print("  ❌ Please enter a valid number (e.g. 250.50).")


def get_category():
    """Ask user for a category from a predefined list."""
    categories = [
        "Food & Drinks", "Transport", "Shopping", "Bills & Utilities",
        "Entertainment", "Health", "Education", "Rent", "Other"
    ]
    print("\n  Categories:")
    for i, cat in enumerate(categories, 1):
        print(f"    {i}. {cat}")
    while True:
        try:
            choice = int(input("  Choose category number: "))
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            print(f"  ❌ Choose a number between 1 and {len(categories)}.")
        except ValueError:
            print("  ❌ Please enter a number.")


# ============================================================
# FEATURES
# ============================================================

def add_expense():
    """Add a new expense."""
    print("\n━━━ ADD NEW EXPENSE ━━━")
    description = input("  Description: ").strip()
    if not description:
        print("  ❌ Description cannot be empty.")
        return

    amount = get_amount()
    category = get_category()

    # Ask for date (optional — default to today)
    date_str = input(f"  Date (YYYY-MM-DD, press Enter for today): ").strip()
    if not date_str:
        date_str = date.today().isoformat()

    expense = {
        "id": datetime.now().timestamp(),  # unique-ish ID
        "description": description,
        "amount": amount,
        "category": category,
        "date": date_str,
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)

    print(f"  ✅ Added: {description} — ₹{amount:.2f} [{category}]")


def view_expenses():
    """Display all expenses in a table."""
    expenses = load_expenses()
    if not expenses:
        print("\n📭 No expenses recorded yet. Add one first!")
        return

    print("\n━━━ ALL EXPENSES ━━━")
    print(f"{'#':<4} {'Date':<12} {'Description':<25} {'Category':<18} {'Amount':<10}")
    print("-" * 70)
    total = 0
    for i, exp in enumerate(expenses, 1):
        amt = exp["amount"]
        total += amt
        print(f"{i:<4} {exp['date']:<12} {exp['description']:<25} {exp['category']:<18} ₹{amt:<8.2f}")
    print("-" * 70)
    print(f"{'':>50} TOTAL: ₹{total:.2f}")
    print()


def delete_expense():
    """Delete an expense by its number."""
    expenses = load_expenses()
    if not expenses:
        print("\n📭 No expenses to delete.")
        return

    view_expenses()
    try:
        num = int(input("Enter the # number to delete (0 to cancel): "))
        if num == 0:
            return
        if 1 <= num <= len(expenses):
            removed = expenses.pop(num - 1)
            save_expenses(expenses)
            print(f"  🗑️ Deleted: {removed['description']} — ₹{removed['amount']:.2f}")
        else:
            print(f"  ❌ Number must be between 1 and {len(expenses)}.")
    except ValueError:
        print("  ❌ Enter a valid number.")


def show_summary():
    """Show a summary: total, category breakdown, monthly stats."""
    expenses = load_expenses()
    if not expenses:
        print("\n📭 No expenses to summarize.")
        return

    print("\n━━━ EXPENSE SUMMARY ━━━")

    # Total
    total = sum(e["amount"] for e in expenses)
    print(f"\n  💰 Grand Total: ₹{total:.2f}")

    # By category
    print("\n  📊 By Category:")
    cats = {}
    for e in expenses:
        cats[e["category"]] = cats.get(e["category"], 0) + e["amount"]
    for cat, amt in sorted(cats.items(), key=lambda x: x[1], reverse=True):
        pct = (amt / total) * 100
        print(f"    {cat:<18} ₹{amt:<8.2f}  ({pct:.1f}%)")

    # By month
    print("\n  📅 By Month:")
    months = {}
    for e in expenses:
        month_key = e["date"][:7]  # "2026-07"
        months[month_key] = months.get(month_key, 0) + e["amount"]
    for month, amt in sorted(months.items()):
        print(f"    {month}  ₹{amt:.2f}")

    # Average per expense
    avg = total / len(expenses)
    print(f"\n  📈 Average per expense: ₹{avg:.2f}")
    print()


# ============================================================
# MAIN MENU
# ============================================================

def main():
    """Main program loop with menu."""
    print("\n" + "=" * 50)
    print("  💸  PERSONAL EXPENSE TRACKER  💸")
    print("=" * 50)

    while True:
        print("\n  MENU:")
        print("    1. ➕ Add an expense")
        print("    2. 📋 View all expenses")
        print("    3. 🗑️  Delete an expense")
        print("    4. 📊 Show summary / report")
        print("    5. 🚪 Exit")
        choice = input("\n  Your choice (1-5): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            print("\n  👋 Bye! Happy saving!\n")
            break
        else:
            print("  ❌ Invalid choice. Enter 1-5.")


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
