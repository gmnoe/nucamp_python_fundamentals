def login(database, username, password):
    for user in database:
        if user == username:
            if database[user] == password:
                print('Welcome back', username, "!\n")
            else: print('Incorrect password for', username, '\n')
            return ''

    print('User not found. Please register. \n')
    return ''