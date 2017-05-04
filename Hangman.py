'''
Assignment: Pair Programming Project
Authors: Aura Rose Jensen-Curtis
         Heather Keaty
Time spent on project: About 35 hours
Version 8 (Final)
Date: 11/27/2016
Honor Code: We pledge that this program represents our own program code.
We received help from no one in designing and debugging our code.
'''

import random   # Import random class


# Main function
def main():

    # Display welcome message
    print('\nWelcome to Hangman!\n'
          '\nCorrectly fill in the letters of the secret word to win.\n'
          'But be careful! It only takes 6 wrong guesses to lose.\n')

    # Initialize variables
    turns = 6   # return type integer
    total_instances = 0 # return type integer (accumulator)
    guesses = []  # empty list

    # invoke functions
    word = get_word()
    count = get_count(word)
    letters = get_letters(word, count)
    play_game(word, count, letters, total_instances, guesses, turns)


# Function opens a file and returns a random word from that file.
def get_word():

    # open file to read
    infile = open('words.txt', 'r')

    # Read lines in file and assign to variable
    wordlist = infile.readlines()

    # Close file
    infile.close()

    # Initialize variable to control loop
    index = 0

    # Begin while loop
    while index < len(wordlist):    # While index is less than list
        wordlist[index] = wordlist[index].rstrip('\n')  # Remove line break from each word
        index += 1  # Add index to accumulator

    # Assign random word from list to word variable
    word = random.choice(wordlist)

    return word


# Function returns the length of the word
def get_count(word):

    # Assign length of word to count variable and return count
    count = len(word)

    # Display the number of letters
    print('The word has', count, 'letters.')

    return count


# Function fills an empty list with letters of the word
def get_letters(word, count):

    # Initialize empty list
    letters = []

    # Begin for loop
    for i in range(count):  # For each letter in the word
        a = word[i]         # assign the letter to a variable
        letters.append(a)   # append the letter to the list
        print('_', end=' ')  # print an underscore for each letter
    # End loop and advance to next line
    print('\n')

    return letters


# Function takes a guess and determines next action by checking guess
# against the word.
def play_game(word, count, letters, total_instances, guesses, turns):

    # print('\n', letters, '\n') # Print letters for debugging

    # Begin loop and continue as long as total instances < count
    while total_instances < count:
        guess = get_guess(guesses)  # Invoke function to get guess
        instance = letters.count(guess)  # Count the times guess appears in letters
        guesses.append(guess)   # Append guess to guesses list
        print('\nGuesses used:', guesses)   # Print list of past guesses for the player
        total_instances += instance  # Add instance to the running total
        # print('Total instances:', total_instances) # print total instances for debugging

        # Begin if else loop
        if guess in letters:    # If guess is in the word
            print('The letter', guess, 'appears', instance, 'time(s).\n')
            show_letters(count, letters, guesses)    # Invoke function to repopulate
                                                        # list with guess
        else:   # If the guess is not in the word
            print('The letter', guess, 'is not in the word.\n')
            # Invoke function to decrement turns
            lose_turn(word, count, letters, total_instances, guesses, turns)

    else:   # Exit while loop
        print('Congratulations! You win!'   # Print congratulations message
              '\nThe word is', word, '.')   # Print the secret word
        play_again()    # Invoke function to play again or exit game

    return guesses


# Function gets letter guess from the player
def get_guess(guesses):
    # Begin loop
    while True:
        guess = input("Please enter your guess: ")  # Prompt for input
        guess = guess.lower()   # Converts guess variable to lowercase

        # Check for input errors
        if guess in guesses:    # Check guess against previously entered guesses
            print('You already guessed that letter. '    # Print error message
                  'Please try again.')                   # and prompt user to try again
        elif len(guess) != 1:   # If the guess entered is not a single character
            print('Please enter one letter at a time.')  # print error message
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':  # If guess is not in the alphabet
            print('Only letters can be guessed. '        # print error message
                  'Please try again.')                   # prompt user to try again
        else:   # Exit the loop
            return guess


# Function shows correct letters and underscores for missing letters
def show_letters(count, letters, guesses):

    display_word = '_' * count  # Set variable to display underscore
                                # for each letter in the word
    for i in range(count):  # Begin loop

        if letters[i] in guesses:   # Test whether the letter has been guessed and display the guessed letter
            display_word = display_word[:i] + letters[i] + display_word[i+1:]   # otherwise display underscore

    for i in display_word:  # For each index
        print(i, end=' ')   # print the letter or underscore followed by a space
    print('\n')     # Advance to next line

    return display_word


# Function decrements turns for each wrong guess
def lose_turn(word, count, letters, total_instances, guesses, turns):
    # Begin if else loop
    if turns > 1:   # If there are turns remaining
        turns -= 1  # Decrement turns by 1
        print('You have', turns, 'turns remaining.\n')  # Print remaining turns
        # Invoke play_game function and continue game
        play_game(word, count, letters, total_instances, guesses, turns)
    else:   # If there are no turns remaining
        print('Game over.\n'    # print game over message
              'The word was', word, '.')    # Print the secret word
        play_again()    # Invoke play_again function

    return turns


# Function prompts user to start another round or exit the game
def play_again():
    while True:     # Start the loop
        print("Would you like to play another round? ")  # Display message
        repeat = input("Type 'y' to play again, anything else to exit the game. ")  # Prompt for input
        repeat = repeat.lower()  # Convert variable to lowercase
        if repeat == 'y':   # If player enters y
            return main()   # restart the game
        else:
            print("Thank you for playing our game!")    # Print exit message
            exit()  # Exit the game


main()  # Invoke main function
