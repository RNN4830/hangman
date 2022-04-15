def hangman_game():
    name = input('What is your name?')
    print ("Hey there," + name, "time to play some hangman!")
    print ("Please guess a letter!")
    turns = 10
    guesses = "" # variable with empty value
    word = "secret"
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print ('_')
                failed += 1
        if failed == 0:
            print("Great job! You won!")
            break
        guess = input("Please guess a letter:")
        guesses += guess
        if guess not in word:
            turns -= 1
            print ("Wrong guess")
        print("You have", + turns, "more guesses")
        if turns == 0:
            print("Better luck next time, game over.")
    check = input("Would you like to play again? Y/N")
    if check == "Y":
        hangman_game()

hangman_game()


