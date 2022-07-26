import random

cards = []
initiate = 0
blackjack = 21

#deck Manager WORKING
def deckManager():
    count = 1
    cards.clear()
    while count <= 32:
        cards.append("ace")
        cards.append(10)
        cards.append(10)
        cards.append(10)
        n = 2
        while n <= 10:
            cards.append(n)
            n += 1

        count += 1

#cards Dealing  WORKING
def cardDeal():
    houseCards.clear()
    playerCards.clear()
    for deal in range(1, 2):
        for houseDeal in range (0, 2):
            randomHouse = random.choice(cards)
            houseCards.append(randomHouse)
            cards.remove(randomHouse)
            randomPlayer = random.choice(cards)
            playerCards.append(randomPlayer)
            cards.remove(randomPlayer)
    print("Dealer has X and " +str(houseCards[1]))
    if 'ace' in houseCards:
        houseCards.remove("ace")
        houseCards.append(11)
    print("You have " +str(playerCards[0]) + " " + str(playerCards[1]))
    if "ace" in playerCards:
        playerCards.remove("ace")
        playerCards.append(11)
    print("Your card Value: " +str(sum(playerCards)) + "\n")
    
    


def playHit():
    while True and sum(playerCards) < 21:
        playerAction = input("Hit or Stand ?: ")
        if playerAction.upper() == "HIT" and sum(playerCards) <= 21:
            tempCard = random.choice(cards)
            if tempCard == "ace":
                cards.remove("ace")
                tempCard = 1
                playerCards.append(tempCard)
            else:
                cards.remove(tempCard)
                playerCards.append(tempCard)
            print("You got: " +str(tempCard)  + "\n Your Cards: " +str(playerCards) + "\n Your Card Value: " + str(sum(playerCards)))
        else:
            break
            


    
def blackJackCheck():
    if sum(playerCards) == sum(houseCards):
        print("Push! It's a DRAW")
    else:
        print("Blackjack! YOU WIN!")
        print("Dealer Had :")
        print(houseCards)

def dealerHit():
    beat = sum(playerCards)
    while sum(houseCards) < sum(playerCards):
        randomCard = random.choice(cards)
        if randomCard == "ace":
            randomCard = 1
            print(" Dealer Got " +str(randomCard))
        else:
            cards.remove(randomCard)
            houseCards.append(randomCard)
            print(" Dealer Got " +str(randomCard))
    print("Dealer total card value : " +str(sum(houseCards)) + "\n")
    if sum(houseCards) > sum(playerCards) and sum(houseCards) <= 21:
        print("House Wins!")
    else:
        print("You Win! \n")
        print("Dealer Bust! His Cards:  " + str(houseCards))
    print("\n")
            

#Game Load
while True:
    playerWantsToPlay = input("Play BlackJack? y/n : ")
    if playerWantsToPlay.upper() == "Y":
        initiate = True
        print("Shuffling Deck...")
        deckManager()
        print(len(cards))
        
    else: 
        print("Game Over \nThank you for Playing <3")
        initiate = False
        break
    
    #Game Logic
    #1 player 1 house
    houseCards = []
    playerCards = []
    cardDeal() #Randomly Give cards to house and player
    if sum(playerCards) == blackjack:
        blackJackCheck()
    else:
        playHit()
    if sum(playerCards) < 22:
        dealerHit()
    else:
        print("You lose! its a Bust")
