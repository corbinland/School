# final.py
# Rock Paper Scissors Game


import random

# File to store scores
SCORE_FILE = "scores.txt"

def load_scores():
    """Loads scores from the file. Returns a dictionary."""
    scores = {"Player": 0, "Computer": 0}
    try:
        with open(SCORE_FILE, "r") as file:
            for line in file:
                name, score = line.strip().split(":")
                scores[name] = int(score)
    except FileNotFoundError:
        save_scores(scores)  # Create file if not exists
    return scores

def save_scores(scores):
    """Saves scores to the file."""
    with open(SCORE_FILE, "w") as file:
        for name, score in scores.items():
            file.write(f"{name}:{score}\n")

def get_player_choice():
    """Prompts player for choice. Returns 'rock', 'paper', or 'scissors'."""
    choices = ["rock", "paper", "scissors"]
    while True:
        print("\nChoose:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        choice = input("Your choice: ")
        if choice in ["1", "2", "3"]:
            return choices[int(choice) - 1]
        print("Invalid input, try again.")

def get_computer_choice():
    """Randomly returns 'rock', 'paper', or 'scissors'."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    """Determines winner. Returns 'Player', 'Computer', or 'Tie'."""
    if player == computer:
        return "Tie"
    if (player == "rock" and computer == "scissors") or \
       (player == "scissors" and computer == "paper") or \
       (player == "paper" and computer == "rock"):
        return "Player"
    return "Computer"

def main_menu():
    """Displays the main menu."""
    print("\n==== Rock Paper Scissors ====")
    print("1 - Play Game")
    print("2 - Show Scores")
    print("3 - Quit")

def play_game(scores):
    """Plays one round of the game."""
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    winner = determine_winner(player_choice, computer_choice)
    if winner == "Player":
        print("You win!")
        scores["Player"] += 1
    elif winner == "Computer":
        print("Computer wins!")
        scores["Computer"] += 1
    else:
        print("It's a tie!")

    save_scores(scores)

def show_scores(scores):
    """Displays the current scores."""
    print(f"\nCurrent Scores:\nPlayer: {scores['Player']}\nComputer: {scores['Computer']}")

def main():
    """Main program loop."""
    scores = load_scores()
    while True:
        main_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            play_game(scores)
        elif choice == "2":
            show_scores(scores)
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
