import random

def guess_random_number(tries, start, stop):
    number = random.randint(start, stop)

    while tries != 0:
        print(f'Number of tries left: {tries}')
        guess = int(input(f'Guess a number between {start} and {stop}: '))
        if (guess == number):
            print('You guessed the correct number!')
            return
        elif (guess < number):
            print('Guess higher!')
        elif (guess > number):
            print('Guess Lower')
        tries -=1

        if (tries == 0):
            print(f'You have failed to guess the number. The correct number was {number}')

def guess_random_num_linear(tries, start, stop):
    number = random.randint(start, stop)
    print(f'The number for the program to guess is... {number}')

    for x in range(start, stop):
        print(f'Number of tries left: {tries}')
        print(f'The program is guessing ... {x}')
        if x == number:
            print("The program has guessed the correct number!")
            return
        tries -= 1
        if tries == 0:
            print("The program has failed to guess the correct number.")
            return

def guess_random_num_binary(tries, start, stop):
    number = random.randint(start, stop)
    lower_bound = start
    upper_bound = stop
    print(f'Random number to find is: {number}')

    while tries != 0:
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = pivot
        tries -=1

        if pivot_value == number:
            print(f'Found it! {number}')
            return
        elif pivot_value > number:
            upper_bound = pivot - 1
            print('Guessing Lower!')
        else:
            lower_bound = pivot + 1
            print('Guessing Higher!')
    else:
        print('Your program has failed to find the number!')


# guess_random_number(5, 0, 10)
# guess_random_num_linear(5, 0, 10)
guess_random_num_binary(5, 0, 100)