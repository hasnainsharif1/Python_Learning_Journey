import random
game_choices = ['Rock', 'Paper', 'Scissor']

def selection(a, b):
    if a == b:
        return "tie"
    elif (a == 'Rock' and b == 'Scissor') or (a == 'Scissor' and b == 'Paper') or (a == 'Paper' and b == 'Rock'):
        return a  # User wins
    else:
        return b  # Computer wins


while True:
    try:
        user_input = input("Select one:-  Rock | Paper | Scissor: ")
        user_input = user_input.capitalize()
        if user_input in game_choices:
            choice = random.choice(game_choices)
            winner = selection(user_input, choice)
            if user_input == winner:
                print(f"Computer Choice is {choice} and your choice is {user_input} And You Win!")
            elif choice == winner:
                print(f"Computer Choice is {choice} and your choice is {user_input} so Computer Win!")
            else:
                print(f"Computer Choice is {choice} and your choice is {user_input} Match Tie!")
            break
        else:
            print("Please Select:-  Rock | Paper | Scissor: ")
            
    except ValueError:
        print("Enter selected Values Only!")