from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

print("          === Automated Teller Machine ===          ")
balance = 0
while True:
    name = input("Enter name to register: ")
    if len(name) <1 or len(name) >10:
        print("Name must be between 1 and 10 characters, please try again!")
        continue
    else:
        break
while True:
    pin = input("Enter PIN: ")
    if len(pin) != 4:
        print("PIN must be 4 digits, please try again!")
        continue
    else:
        break

print(name,"has been registered with a starting balance of $", float(balance))

while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login Successful!")
        break
    if name_to_validate != name or pin_to_validate != pin:
        print("Invalid Credentials!")

while True:
    atm_menu(name)
    option = input("Choose and option: ")
    if option == "1":
        account.show_balance(float(balance))
    elif option == "2":
        balance = account.deposit((balance))
        account.show_balance((balance))
    elif option == "3":
        balance = account.withdraw(float(balance))
        account.show_balance(float(balance))
    else:
        account.logout(name)
        break
