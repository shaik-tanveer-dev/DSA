# Expense tracker

expenses = []

def add_expenses():
    name = input("Enter expense name: ")
    amount = input("Enter amount expense: ")
    expense = {
        "name":name,
        "amount":amount
    }
    expenses.append(expense)
    print("Expense amount.")

def view_expenses():
    for expense in expenses:
        print(expense["name"],"-", expense["amount"])

def show_menu():
    print("\nExpense Tracker")
    print("1. add expense")
    print("2. view Expense")
    print("3. exit")

def main():
    while True:
        show_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            add_expenses()
        elif choice =="2":
            view_expenses()
        elif choice =="3":
            print("Exiting the programm")
            break
        else:
            print("Invalid choice: Try again")

main()