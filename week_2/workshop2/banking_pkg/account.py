def show_balance(balance):
    print("Current Balance: $", balance)

def deposit(balance):
    amount = input("Enter amount to deposit: $")
    return balance + float(amount)

def withdraw(balance):
    amount = input("Enter amount to withdraw: $")
    if float(amount) > balance:
        print("Insufficient Funds!")
        return balance
    else:
        return balance - float(amount)

def logout(name):
    print("Goodbye ", name, "!")