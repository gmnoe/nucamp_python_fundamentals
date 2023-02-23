class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password

class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0.0

    def show_balance(self):
        print(self.name, 'has an account balance of:', self.balance)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def transfer_money(self, amount):
        print('\nYour are transferring $', amount, 'to ', user1.name)
        print('User authentication is required...')

        while True:
            pin = int(input('Enter your PIN:'))
            if pin == self.pin:
                self.balance -= float(amount)
                user1.balance += float(amount)
                print('Transfer authorized')
                print('Transferring $', amount, 'to ', user1.name)
                print(self.name, 'has an account balance of: ', self.balance)
                print(user1.name, 'has an account balance of: ', amount)
                return True
            else:
                print("Invalid")
                break

    def request_money(self, amount,):
        print('\nYou are requesting $', float(amount), 'from ', user1.name)
        print('User authentication is required...')
        
        while True:
            pin = int(input(f"Enter {user1.name}'s PIN:"))
            if pin == user1.pin:
                password = str(input("Enter your password: "))
                if password == self.password:
                    self.balance += amount
                    user1.balance -= amount
                    print("Request Authorized")
                    print(self.name, "sent ", float(amount))
                    return
                else:
                    print('Invalid Password. transaction is cancelled')
                    break
            else:
                print('Invalid PIN. Transaction cancelled')
                break

''' Driver Code for Task 1 '''
# user1 = User('Bob', 1234, 'password')
# print(user1.name, user1.pin, user1.password)

''' Driver Code for Task 2 '''
# user1 = User('Bob', 1234, 'password')
# print(user1.name, user1.pin, user1.password)
# user1.change_name('Bobby')
# user1.change_pin(4321)
# user1.change_password('newpassword')
# print(user1.name, user1.pin, user1.password)

''' Driver Code for Task 3 '''
# user1 = BankUser('Bob', 1234, 'password')
# print(user1.name, user1.pin, user1.password, user1.balance)

''' Driver Code for Task 4 '''
# user1 = BankUser('Bob', 1234, 'password')
# user1.show_balance()
# user1.deposit(123)
# user1.show_balance()
# user1.withdraw(33)
# user1.show_balance()

''' Driver Code for Task 4 '''
user1 = BankUser('Bob', 1234, 'password')
user2 = BankUser('Alice', 5678, 'pw')
user2.deposit(5000)
user1.show_balance()
user2.transfer_money(500)
user1.show_balance()
user2.show_balance()
user2.request_money(250)
user1.show_balance()
user2.show_balance()