import random
computer = random.choice([1 , -1 , 0])
youstr = input("Enter your choice: ")
youdict = {"s": 1 , "w": -1 , "g": 0}  # user will enter s,w,g.
reversedict = {1 : "snake" , -1 : "water" , 0 : "gun"}

you = youdict[youstr]

# By now we have 2 (variables) , you and computer

print(f"You chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")

if (computer == you):
    print("It's a draw!")

else:
    if((computer - you == -1) or (computer - you == 2)):
        print("You lose!")
    else:
        print("You win!!")