import random
def computer_choice():
    number = random.randint(1,1000)
    return(number)

def player_choice():
    player_choice = int(input("Enter a choice! (numbers 1-1000) "))
    return(player_choice)
    
def check_win(number, player_choice): 
    if player_choice == number:
        return("You've guessed it! You win!")
    elif player_choice > number:
        return("The number you chose is to big! Have another try!")
    else:
        return("The number you chose is to small! Have another try!")
number = computer_choice()
while True:
    player = player_choice()
    result = check_win(number, player)
    print(result)
    if "win" in result:
        break


