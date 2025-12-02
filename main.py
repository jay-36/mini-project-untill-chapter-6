        # expense tracker project
expenses = []  # List of all expenses in form of dictionaries
print("Welcome to the Expense Tracker!")
expense = {}
while True:
    print("=========Menu=========")
    print("1. Add Expense")
    print("2. View all Expenses")
    print("3. Delete Expense")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    # add expense
    if choice == '1':
        date = input("Enter date (YYYY-MM-DD): ")
        amount = float(input("Enter amount: "))
        category = input("Enter category (e.g., Food, Transport): ")
        description = input("Enter description: ")

        expense = {
            'date': date,
            'amount': amount,
            'category': category,
            'description': description
        }
        expenses.append(expense)
        print("Expense added successfully!")

    # view all expenses
    elif choice == '2':
        if not expenses:
            print("No expenses recorded.")
        else:
            print("All Expenses:")
            for idx, expense in enumerate(expenses, start=1):
                print(
                    f"{idx}. Date: {expense['date']}, Amount: {expense['amount']}, "
                    f"Category: {expense['category']}, Description: {expense['description']}"
                )

    # delete expense
    elif choice == '3':
        if not expenses:
            print("No expenses to delete.")
        else:
            print("Select the expense to delete:")
            for idx, expense in enumerate(expenses, start=1):
                print(
                    f"{idx}. Date: {expense['date']}, Amount: {expense['amount']}, "
                    f"Category: {expense['category']}, Description: {expense['description']}"
                )

            del_index = int(input("Enter the expense number to delete: ")) - 1

            if 0 <= del_index < len(expenses):
                deleted_expense = expenses.pop(del_index)
                print(
                    f"Deleted expense: Date: {deleted_expense['date']}, Amount: {deleted_expense['amount']}, "
                    f"Category: {deleted_expense['category']}, Description: {deleted_expense['description']}"
                )
            else:
                print("Invalid expense number.")

    # exit
    elif choice == '4':
        print("Exiting Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1 to 4.")
