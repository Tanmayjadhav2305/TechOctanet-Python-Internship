import getpass

class ATM:
    def __init__(self):
        self.balance = 1000  # Initial balance
        self.pin = "1234"  # Default PIN
        self.transactions = []
    
    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")
        self.transactions.append("Checked balance")
    
    def withdraw_cash(self):
        amount = float(input("Enter withdrawal amount: "))
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid amount!")
        else:
            self.balance -= amount
            print(f"Withdrawal successful! Your new balance is: ${self.balance}")
            self.transactions.append(f"Withdrew ${amount}")
    
    def deposit_cash(self):
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("Invalid amount!")
        else:
            self.balance += amount
            print(f"Deposit successful! Your new balance is: ${self.balance}")
            self.transactions.append(f"Deposited ${amount}")
    
    def change_pin(self):
        old_pin = getpass.getpass("Enter current PIN: ")  # getpass.getpass Hides input so you cant see what you are entering in terminal enter 1234 since it is the default pin and press enter.
        if old_pin == self.pin:
            new_pin = getpass.getpass("Enter new PIN: ") # Hide input 
            confirm_pin = getpass.getpass("Confirm new PIN: ")  # Hide input
            if new_pin == confirm_pin:
                self.pin = new_pin
                print("PIN changed successfully!")
                self.transactions.append("Changed PIN")
            else:
                print("PINs do not match!")
        else:
            print("Incorrect PIN!")
    
    def show_transaction_history(self):
        if self.transactions:
            print("Transaction History:")
            for transaction in self.transactions:
                print(f"- {transaction}")
        else:
            print("No transactions found.")

def main():
    atm = ATM()
    pin_attempts = 3
    
    while pin_attempts > 0:
        entered_pin = getpass.getpass("Enter your PIN: ")  # Hide input
        if entered_pin == atm.pin:
            while True:
                print("\nATM Menu:")
                print("1. Check Balance")
                print("2. Withdraw Cash")
                print("3. Deposit Cash")
                print("4. Change PIN")
                print("5. Transaction History")
                print("6. Exit")
                
                choice = input("Select an option: ")
                
                if choice == "1":
                    atm.check_balance()
                elif choice == "2":
                    atm.withdraw_cash()
                elif choice == "3":
                    atm.deposit_cash()
                elif choice == "4":
                    atm.change_pin()
                elif choice == "5":
                    atm.show_transaction_history()
                elif choice == "6":
                    print("Thank you for using our ATM. Goodbye!")
                    break
                else:
                    print("Invalid choice, please try again.")
            break
        else:
            pin_attempts -= 1
            print(f"Incorrect PIN. {pin_attempts} attempt(s) remaining.")
            if pin_attempts == 0:
                print("Too many incorrect attempts. Exiting.")
                break

if __name__ == "__main__":
    main()
