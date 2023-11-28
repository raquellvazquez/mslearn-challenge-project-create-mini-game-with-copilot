import random

def get_player_choice():
    """Get the player's choice (rock, paper, or scissors)."""
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    """Randomly choose the computer's move."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
    """Determine the winner based on the choices."""
    if player_choice == computer_choice:
        return "Tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "Player"
    else:
        return "Computer"

def main():
    player_score = 0
    computer_score = 0

    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        print(f"Computer chose {computer_choice}.")

        winner = determine_winner(player_choice, computer_choice)
        if winner == "Player":
            player_score += 1
            print("You win this round!")
        elif winner == "Computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print(f"Final scores: Player {player_score} - Computer {computer_score}")

if __name__ == "__main__":
    main()