import random

def get_user_choice():
    print("Choose: Rock, Paper, or Scissors")
    user_choice = input().capitalize()
    return user_choice

def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    print(f"You chose {user_choice}")
    print(f"Computer chose {computer_choice}")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
