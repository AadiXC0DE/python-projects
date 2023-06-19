accounts = {}  # Dictionary to store bank accounts

def create_account(account_number, customer_name, initial_balance=0):
    if account_number not in accounts:
        accounts[account_number] = {"customer_name": customer_name, "balance": initial_balance, "transaction_history": []}
        print("Account created successfully.")
    else:
        print("Account number already exists.")

def deposit(account_number, amount):
    if account_number in accounts:
        if amount > 0:
            accounts[account_number]["balance"] += amount
            accounts[account_number]["transaction_history"].append(f"Deposited: {amount}")
            print(f"Amount {amount} deposited successfully.")
        else:
            print("Invalid amount. Deposit failed.")
    else:
        print("Account not found.")

def withdraw(account_number, amount):
    if account_number in accounts:
        if 0 < amount <= accounts[account_number]["balance"]:
            accounts[account_number]["balance"] -= amount
            accounts[account_number]["transaction_history"].append(f"Withdrew: {amount}")
            print(f"Amount {amount} withdrawn successfully.")
        else:
            print("Insufficient funds. Withdrawal failed.")
    else:
        print("Account not found.")

def check_balance(account_number):
    if account_number in accounts:
        print(f"Account Balance: {accounts[account_number]['balance']}")
    else:
        print("Account not found.")

def display_transaction_history(account_number):
    if account_number in accounts:
        print("Transaction History:")
        for transaction in accounts[account_number]["transaction_history"]:
            print(transaction)
    else:
        print("Account not found.")

# Main Bank App

def main():
    while True:
        print("\n===== Bank App Menu =====")
        print("1. Create an account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check balance")
        print("5. Display transaction history")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            account_number = input("Enter account number: ")
            customer_name = input("Enter customer name: ")
            initial_balance = float(input("Enter initial balance: "))
            create_account(account_number, customer_name, initial_balance)

        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            deposit(account_number, amount)

        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            withdraw(account_number, amount)

        elif choice == "4":
            account_number = input("Enter account number: ")
            check_balance(account_number)

        elif choice == "5":
            account_number = input("Enter account number: ")
            display_transaction_history(account_number)

        elif choice == "6":
            print("Thank you for using the Bank App. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
