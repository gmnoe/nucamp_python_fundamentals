def login(database, username, password):
    for user in database:
        if user == username:
            if database[user] == password:
                print('Welcome back', username, "!\n")
            else: print('Incorrect password for', username, '\n')
            return ''
    print('User not found. Please register. \n')
    return ''

def register(database, username):
    if username in database:
        print('Username already registered. \n')
        return ''
    else:
        print('Username has been registered. \n')
        return username

def donate(username):
    donation_amt = input('Enter amount to donate: ')
    donation= print(username, ' donated $', donation_amt)
    print('Thank you for your donation!')
    return donation

def show_donations(donations):
    print('\n--- All Donations ---')
    if donations == []:
        print('Currently there are no donations.')
    else:
        for x in donations:
            print(x)