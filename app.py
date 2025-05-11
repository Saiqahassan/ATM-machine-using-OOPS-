class ATM:
    def __init__(self):
        self.pin = "1001"
        self.balance = 1000.0
        self.is_authenticated = False

   # Function to check pin
    def check_pin(self, input_pin):
        if input_pin == self.pin:
            self.is_authenticated = True
            print("Pin entered is correct.🔓\n")
        else:
            print("❌Incorrect pin. Please try again.\n")

    # Function to check balance
    def check_balance(self):
        if self.is_authenticated:
            print(f"\nYour current balance is: ${self.balance:.2f}\n")
        else:
            print("Please authenticate first and correct pin first.\n")

    # Function to deposit money
    def deposit(self, amount):
        if self.is_authenticated:
            if amount > 0:
                self.balance += amount
                print(f"\nDeposited ${amount:.2f}. New balance: ${self.balance:.2f}\n")
            else:
                print("❌Invalid deposit amount. Please enter a positive number.\n")
        else:
            print("Please authenticate first and correct pin first.\n")

    # Function to withdraw money
    def withdraw(self, amount):
        if self.is_authenticated:
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                print(f"\nWithdrew ${amount:.2f}. New balance: ${self.balance:.2f}\n")
            else:
                print("❌Insufficient balance. Please deposit some amount first!\n")
        else:
            print("Please authenticate first and correct pin first.\n")

    # Function to exit the ATM
    def exit(self):
        print("Thank you for using the ATM. Goodbye!")
        self.is_authenticated = False

    # Main function to run the ATM program
    def menu(self):
        attempts = 0
        while attempts < 3:
            pin_input = input("\nPlease enter your 4-digit pin: ")
            self.check_pin(pin_input)
            if self.is_authenticated:
                break
            else:
             attempts += 1
             print(f"❌Incorrect pin. You have {3 - attempts} attempts left.\n")

        else:
            print("❌Too many incorrect attempts. Exiting the ATM.")
            return

        while True:
            print("======Welcome to the ATM!======\n")

            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("\nPlease select an option (1-4): \n")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                try:
                    amount = float(input("\nEnter the amount to deposit: $\n"))
                    self.deposit(amount)
                except ValueError:
                    print("❌Invalid input. Please enter a valid number.\n")
            elif choice == "3":
                try:
                    amount = float(input("Enter the amount to withdraw: $"))
                    self.withdraw(amount)
                except ValueError:
                    print("❌Invalid input. Please enter a valid number.\n")
            elif choice == "4":
                self.exit()
                break
            else:
                print("❌Invalid choice. Please select a valid option (1-4).\n")

if __name__ == "__main__":
    atm = ATM()
    atm.menu()
            


