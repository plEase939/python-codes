import random

#Global Variables
play =1
playerScore = 0
computerScore = 0


possibleActions = ("rock", "paper", "scissor")

#Game Logic
while True:
    play = input("Play? y/n: ")
    if play.upper() != "N":
        play = 1
    else:
        print("Game End")
        break
    userAction = input("Choose your move rock or paper or scissor: ")
    computerAction = random.choice(possibleActions)
    if userAction == computerAction:
        print("You chose " + userAction + " and computer chose " + computerAction + "\n")
        print("It's a draw!")
    elif userAction == "rock" and computerAction == "scissor":
        print("You chose " + userAction + " computer chose " + computerAction + "\n You win!")
        playerScore +=1
        print("Score: " + " Your Score: " + str(playerScore) + " Computer Score: " + str(computerScore))
    elif userAction == "paper" and computerAction == "rock":
        print("You chose " + userAction + " computer chose " + computerAction + " \n You win!")
        playerScore +=1
        print("Score: " + " Your Score: " + str(playerScore) + " Computer Score: " + str(computerScore))
    elif userAction == "scissor" and computerAction == "paper":
        print("You chose " + userAction + " computer chose " + computerAction + "\n You win!")
        playerScore +=1
        print("Score: " + " Your Score: " + str(playerScore) + " Computer Score: " + str(computerScore))
    else:
        print("you chose " + userAction + " computer chose " + computerAction + " \n You Lose!")
        computerScore += 1
        print("Score: " + " Your Score: " + str(playerScore) + " Computer Score: " + str(computerScore))
print("Thank you for playing <3 ")
