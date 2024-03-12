class User:
    def __init__(self):
        self.name = input("Please enter your name: ")
        self.age = int(input("Please enter your age: "))
        self.balance = 0

    def display_user_details(self):
        print("Name:", self.name)
        print("Age:", self.age, "(years old)")


class Bank(User):
    def __init__(self):
        super().__init__()

    def deposit(self):
        deposit_amount = int(input("How much do you want to deposit today: "))
        self.balance += deposit_amount
        print(f"You have deposited £{deposit_amount}. Your new balance is £{self.balance}")
        with open('transactions.txt', 'w') as transacfile:
            transacfile.write(f"*DEPOSIT*\nCustomer name: {self.name}\nCustomer age: {self.age}\nAmount deposited: £{deposit_amount}\nBalance: £{self.balance}")

    def withdraw(self):
        withdraw_amount = int(input("How much would you like to withdraw today: "))
        if self.balance < withdraw_amount:
            print("Sorry, you do not have enough funds to make this transaction")
        else:
            self.balance -= withdraw_amount
            print(f"You have withdrawn £{withdraw_amount}. Your current account balance is £{self.balance}")
        with open('transactions.txt', 'a') as transacfile:
            transacfile.write(f"\n\n\n*WITHDRAWAL*\nCustomer name: {self.name}\nCustomer age: {self.age}\nAmount withdrawn: £{withdraw_amount}\nBalance: £{self.balance}")

    def check_balance(self):
        print(f"Your current balance is £{self.balance}")


user = Bank()

while True:
    user_action = input("Hi, welcome to the bank of MARTINA ARDUINI! \nWhat would you like to do today (deposit, withdraw, balance, quit)?: ")
    user_action = user_action.lower()

    if user_action == "deposit":
        user.deposit()
    elif user_action == "withdraw":
        user.withdraw()
    elif user_action == "balance":
        user.check_balance()
    elif user_action == "quit":
        break
    else:
        print("You have not selected a valid option.")
