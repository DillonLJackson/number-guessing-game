import random
def play_game(chances, ran_num):
        for i in range(chances - 1, -1, -1):

            guess = input("Take a guess: ")

            if int(guess) < ran_num:
                print(f"Incorrect! The number is higher than {guess}")
            if int(guess) > ran_num:
                print(f"Incorrect! The number is lower than {guess}")
            if int(guess) == ran_num:
                attempts_used = 10 - i
                print(f"Congratulations! you guessed the correct number in {attempts_used} attempts.")
                return
        else:
            print(f"You're out of attempts, the number was {ran_num}")



def main():

    print("Welcome to the Number Guessing Game! \n"
    "I'm thinking of a number between 1 and 100. \n"
    "You have 5 changes to guess the correct number. \n\n")

    print("Please select the difficulty level: \n"
    "1. Easy (10 chances) \n"
    "2. Medium (5 chances) \n"
    "3. Hard (3 chances) \n")

    choice = input("Enter your choice: ") 
    print("\n")

    if choice == "1":
        print("Great! you selected the Easy difficulty level. \n"
        "Let's start the game! \n")
        chances = 10
    elif choice == "2":
        print("Great! You selected the Medium difficulty level. \n"
        "Let's start the game! \n")
        chances = 5
    elif choice == "3":
        print("Great! You selected the Hard difficulty level. \n"
        "Let's start the game! \n")
        chances = 3
    else:
        print("Please enter a valid choice.")
        return

    ran_num = random.randint(1, 100)
    play_game(chances, ran_num)
    
    main()