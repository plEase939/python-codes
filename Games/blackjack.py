import random

cards = []
suites = 4
eachSuite = 13
deck = 52
totalDeck = 8*deck
suiteCards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #The last three 10 are jack queen and king. ACE login is pending
initiate = 0
blackjack = 21


#A standard deck of cards has four suites: hearts, clubs, spades, diamonds. Each suite has thirteen cards: ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen and king. 
# Thus the entire deck has 52 cards total.
#13 cards are repeated 

#GAME LOGIC MAIN

def playerAction():
    updatedValue = playerHas
    playerHit = "HIT"
    while playerHit == "HIT":
        playerHit = input("Hit or Stand ?: ")
        if playerHit.upper() == "HIT" and updatedValue < 21:
            playerGot = random.choice(cards)
            playerCards.append(playerGot)
            updatedValue = playerHas + playerGot
            print("You got " + str(playerGot))
            print("Your new Card Value: " + str(updatedValue))
        elif updatedValue > 21:
            return updatedValue
            print("Its a Bust!")
        else:
            return updatedValue

    


            




def cardsWithHouse():  #Need Update: Don't show first card only show second card
    totalDealerCards = len(houseCards)

    print(houseCards)
    dealerHas = sum(houseCards)
    for i in range(0, totalDealerCards):
        print("House has " + str(houseCards[i]))
    print("House Card Value: " + str(dealerHas))
    return dealerHas

def cardsWithPlayer():

    totalPlayerCards = len(playerCards)
    
    print(playerCards)
    playerHas = sum(playerCards)
    for i in range(0, totalPlayerCards):
        print("You have " + str(playerCards[i]))
    print("Your Card Value: " + str(playerHas))
    return playerHas
        
    




#cards Dealing  WORKING
def cardDeal():
    for deal in range(1, 2):
        for houseDeal in range (0, 2):
            randomHouse = random.choice(cards)
            houseCards.append(randomHouse)
            randomPlayer = random.choice(cards)
            playerCards.append(randomPlayer)
            
            
def blackjackcheck():
    if playerHas == dealerHas:
        print("Push! Its a draw")
    else:
        print("BLACKJACK! You win!!!")



#deck Manager WORKING
def deckManager():
    count = 1
    while count <= 32:
        cards.append(11)
        cards.append(10)
        cards.append(10)
        cards.append(10)
        n = 2
        while n <= 10:
            cards.append(n)
            n += 1

        count += 1

#Game Initiate
while True:
    playerWantsToPlay = input("Play BlackJack? y/n : ")
    if playerWantsToPlay.upper() == "Y":
        initiate = True
        print("Shuffling Deck...")
        deckManager()
        #houseCards.clear()
        #playerCards.clear()
        
    else: 
        print("Game Over \nThank you for Playing <3")
        initiate = False
        break
    
    #Game Logic
    #1 player 1 house
    houseCards = []
    playerCards = []
    cardDeal() #Randomly Give cards to house and player
    playerHas = cardsWithPlayer() 
    dealerHas = cardsWithHouse()
    #Checking if player has 
    if playerHas == blackjack:
        winner = blackjackcheck()
    else:
        newValue = playerAction()
    

    

    
    



