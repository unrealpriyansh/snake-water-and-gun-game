import random
print('''Welcome to Snake Water And Gun Game \n Press 1 for Snake.\n Press 2 for Gun.\n Press 3 for water''')
list_of_options=["Snake","Gun","Water"]
choice_of_computer=random.choice(list_of_options)
for poplu in range(3):
    choice_of_computer=random.choice(list_of_options)
    user_choice=int(input("Enter a number between 1 and 3 : \n"))
    if (user_choice==1):
        if (choice_of_computer=="Snake"):
            print("Ohh!! My choice was also same.Our snake started fighting.")
        elif(choice_of_computer=="Gun"):
            print("I killed your snake.My choice was gun")
        elif(choice_of_computer=="Water"):
            print("My choice was water and your snake drank all the water")
    if(user_choice==2):
        if(choice_of_computer=="Snake"):
            print("You killed my snake.My choice was snake")
        elif(choice_of_computer=="Gun"):
            print("A big collision of our guns...!! My choice was gun.")
        elif(choice_of_computer=="Water"):
            print("Your gun fell in the water. My choice was water")
    if (user_choice==3):
        if(choice_of_computer=="Snake"):
            print("My snake drank all the water.My choice was snake")
        elif(choice_of_computer=="Gun"):
            print("My gun fell in the water.My choice was gun.")
        elif(choice_of_computer=="Water"):
            print("Ohhh!! Same choices..Lot  of water there..!!!")
    if(user_choice>=4):
        print("Please give number between 1 and 3")
print('''Game Over\nThanks for playing.....''')
