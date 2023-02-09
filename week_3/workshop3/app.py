from donations_pkg.homepage import *
from donations_pkg.user import login
from donations_pkg.user import register
from donations_pkg.user import donate
from donations_pkg.user import show_donations

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
        password = input('Enter password: ')
        authorized_user = login(database, username, password)
    elif option == '2':
        username = input('Enter username: ')
        password = input('Enter password: ')
        authorized_user = register(database, username)
        
        if authorized_user != '':
            database[username] = password 
    elif option == '3':
        if not authorized_user == '':
            print("You are not logged in.")
        else:
            donation = donate(authorized_user)
            donations.append(donation)
    elif option == "4":
        show_donations(donations)

    elif option == "5":
        print("Leaving DonateMe ...\n")
        break
