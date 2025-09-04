import random

def get_computer_choice():
    return random.choice(['stone', 'paper', 'scissors'])

def get_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == "stone" and computer == "scissors") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def play_game():
    print("Welcome to Stone, Paper, Scissors Game!")
    user_score = 0
    computer_score = 0

    while True:
        print("\nChoices: stone / paper / scissors")
        user_choice = input("Enter your choice: ").lower()

        if user_choice not in ['stone', 'paper', 'scissors']:
            print("Invalid choice. Try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = get_winner(user_choice, computer_choice)

        if winner == "draw":
            print("It's a draw!")
        elif winner == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Scores => You: {user_score} | Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Run the game
play_game()
