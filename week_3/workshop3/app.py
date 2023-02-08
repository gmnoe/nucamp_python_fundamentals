from donations_pkg.homepage import *
from donations_pkg.user import login

database = {"admin":"password123"}
donations = []
authorized_user = ''

while True:
    show_homepage()
    if authorized_user == '':
        print('You must be logged in to donate.')
    else:
        print('Logged in as: ', authorized_user)

    option = input("Please choose an option: ")
    if option == '1':
        username = input('Enter username: ')
        password = input('Enter password:')
        authorized_user = login(database, username, password)
    if option == '2':
        print('TODO: Write Register Functionality\n')
        continue
    if option == '3':
        print('TODO: Write Donate Functionality\n')
        continue
    if option == '4':
        print('TODO: Write Show Donations Functionality\n')
        continue
    if option == '5':
        print('Leaving DonateMe...\n')
        break
