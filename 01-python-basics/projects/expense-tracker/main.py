expenses = [
    {"name": "breakfast","amount": 35000},
    {"name": "coffee", "amount": 45000},
    {"name": "buy books", "amount": 180000},
    {"name": "bus fares", "amount": 20000}
]

def show_expenses(expenses):
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}.{expense['name']}: {expense['amount']}")

def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]

    return total

def find_largest_expense(expenses):
    if not expenses:
        return None
    largest_expense = expenses[0]

    for expense in expenses:
        if expense["amount"] > largest_expense["amount"]:
            largest_expense = expense
    return largest_expense

def add_expense(expenses):
    name = input("\nEnter the expense name: ").strip()

    while True:
        try:
            amount = int(input("Enter the amount"))

            if amount < 0:
                print("The amount cannot be nagative.")
                continue

            break

        except ValueError:
            print("Please enter a valid interger.")

    expenses.append({
        "name": name,
        "amount": amount
    })
    print("Expense added successfully.")

def show_expenses_over_50000(expenses):
    print("\nExpenses greater than 50000:")

    found = False

    for expense in expenses:
        if expense["amount"] >50000:
            print(f"-{expense['name']}: {expense['amount']}")
            found = True

    if not found:
        print("There are no expenses greater than 50000.")

def sort_expenses_descending(expenses):
    return sorted(
        expenses,
        key= lambda expense: expense["amount"],
        reverse = True
    )

print("Expense list: ")
show_expenses(expenses)

total = calculate_total(expenses)
print(f"\nTotal expenses: {total}")

largest = find_largest_expense(expenses)

if largest is not None:
    print(
        f"Largest expense: "
        f"{largest['name']}- {largest['amount']}"
    )

add_expense(expenses)

print("\nExpense list after adding a new expense:")
show_expenses(expenses)

show_expenses_over_50000(expenses)

sorted_expenses = sort_expenses_descending(expenses)

print("\nExpenses sorted from highest to lowest: ")
show_expenses(sorted_expenses)

