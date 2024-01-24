import random

def user_choice1():
    user_choice = input("Choose ROCK, PAPER, or SCISSORS: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Please check your words-type rock, paper, or scissors.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()
    return user_choice

def compiler_choice1():
    return random.choice(['rock', 'paper', 'scissors'])

def finding_winner(user_choice, compiler_choice):
    if user_choice == compiler_choice:
        return "TIE UP!"
    elif (user_choice == 'rock' and compiler_choice == 'scissors') or \
         (user_choice == 'scissors' and compiler_choice == 'paper') or \
         (user_choice == 'paper' and compiler_choice == 'rock'):
        return "You WIN! CRACK IT!"
    else:
        return "You Lose TRY AGAIN!"

def display_result(user_choice, compiler_choice, result):
    print(f"\nYour choice: {user_choice}")
    print(f"Compiler's choice: {compiler_choice}")
    print(f"Game End: {result}\n")

def play_game():
    user_score = 0
    compiler_score = 0

    while True:
        user_choice = user_choice1()
        compiler_choice = compiler_choice1()

        result = finding_winner(user_choice, compiler_choice)
        display_result(user_choice, compiler_choice, result)

        if "You WIN!" in result:
            user_score += 1
        elif "You Lose" in result:
            compiler_score += 1

        print(f"Score - You: {user_score}  Compiler: {compiler_score}")

        play_again = input("Let's TRY AGAIN? (YES/NO): ").lower()
        if play_again != 'yes':
            print("GAME OVER!")
            break

if __name__== "__main__":
    print("Lets START! Rock-Paper-Scissors Game!")
    play_game()
