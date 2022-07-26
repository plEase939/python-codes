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
    print("Your card Value: " +str(sum(playerCards)))
    


def playHit():
    playerAction = input("Hit or Stand?: ")
    if playerAction.upper() == "HIT":
        newCard = random.choice(cards)
        playerCards.append(newCard)


    
def blackJackCheck():
    if sum(playerCards) == sum(houseCards):
        print("Push! It's a DRAW")
    else:
        print("Blackjack! YOU WIN!")
        print("Dealer Had :")
        print(houseCards)


#Game Load
while True:
    playerWantsToPlay = input("Play BlackJack? y/n : ")
    if playerWantsToPlay.upper() == "Y":
        initiate = True
        print("Shuffling Deck...")
        deckManager()
        #houseCards.clear() depreciated
        #playerCards.clear() depreciated
        
    else: 
        print("Game Over \nThank you for Playing <3")
        initiate = False
        break
    
    #Game Logic
    #1 player 1 house
    houseCards = []
    playerCards = []
    cardDeal() #Randomly Give cards to house and player
    if 'ace' in playerCards:
        playerCards.remove("ace")
        playerCards.append(11)
    if sum(playerCards) == blackjack:
        blackJackCheck()
    else:
        playHit()
