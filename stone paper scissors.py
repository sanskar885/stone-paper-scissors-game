import random
def result(player_choice,Computer_choice):
    if player_choice==Computer_choice:
        return "It's a tie!"
    if  (player_choice=="stone" and Computer_choice=="scissors")or\
        (player_choice=="paper" and Computer_choice=="stone")or\
        (player_choice=="scissors" and Computer_choice=="paper"):
        print("User wins")
    else:
        print("You lose")
choices=["stone","paper","scissors"]
def mygame():
    print("Welcome to the game")
    player_choice=input("Enter your Choice(stone/paper/scissors): ").lower()
    if player_choice  not in choices:
        print("you have selected the wrong choice")
        return
    Computer_choice=random.choice(choices)
    print(f"computer chose:{Computer_choice}")
    game_result=result(player_choice , Computer_choice)
    print(game_result)
if __name__ == "__main__":
    mygame()
        