import random
print("Welcome to my snake,water and gun game")
print("Press 1 for snake")
print("Press 2 for water")
print("Press 3 for gun")

chances=3
l1=["Snake","Gun","Water"]
choice_of_computer=random.choice(l1)
for i in range(1,chances+1):
    player_choice=int(input("Enter choice : \n"))
    if player_choice>3:
        print("Please give number till 3.")
    if player_choice==1 and choice_of_computer=="Snake":
        
        print("Ooops,yours and computer's choice is same")
    elif player_choice==2 and choice_of_computer=="Water":
        
        print("Ooops,yours and computer's choice is same")
    elif player_choice==3 and choice_of_computer=="Gun":
        
        print("Ooops,yours and computer's choice is same")
    #other matching finding.
    elif player_choice==1 and choice_of_computer=="Water":
        
        print("Ooops,you drinked all the water and my choice was",choice_of_computer)
    elif player_choice==1 and choice_of_computer=="Gun":
        
        print("Yeah,I killed you and my choice was",choice_of_computer)
    elif player_choice==2 and choice_of_computer=="Snake":
        
        print("I drinked your all the water and my choice was",choice_of_computer)
    elif player_choice==2 and choice_of_computer=="Gun":
        
        print("Oops, my gun fell in water and my choice was",choice_of_computer)
    elif player_choice==3 and choice_of_computer=="Snake":
        
        print("Oops,you killed my snake and my choice was",choice_of_computer)
    elif player_choice==3 and choice_of_computer=="Water":
        
        print("Yeah,your gun fell in my water and my choice was",choice_of_computer)
if chances==3:
    print("Game Over \n")
    print("Thanks for playing.................")
        
