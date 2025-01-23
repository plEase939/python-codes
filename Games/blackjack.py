import random

# Global Variables
cards = []
houseCards = []
playerCards = []

# Create the deck with values
def deckManager():
    global cards
    cards.clear()
    values = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # 10 is repeated for Jack, Queen, King
    for _ in range(4):  # 4 suits
        cards.extend(values)

# Deal cards to player and house
def cardDeal():
    global houseCards, playerCards
    houseCards.clear()
    playerCards.clear()
    
    for _ in range(2):  # Deal 2 cards to player and house
        houseCards.append(random.choice(cards))
        cards.remove(houseCards[-1])
        playerCards.append(random.choice(cards))
        cards.remove(playerCards[-1])
    
    print("Dealer has X and " + str(houseCards[1]))
    print("You have " + str(playerCards[0]) + " " + str(playerCards[1]))
    print("Your card value: " + str(calculateValue(playerCards)) + "\n")

# Calculate the value of a hand
def calculateValue(hand):
    value = 0
    ace_count = 0
    for card in hand:
        if card == "ace":
            value += 11
            ace_count += 1
        else:
            value += card
    while value > 21 and ace_count > 0:
        value -= 10  # Adjust for aces as 1 instead of 11
        ace_count -= 1
    return value

# Player's decision to hit or stand
def playHit():
    while True and calculateValue(playerCards) < 21:
        playerAction = input("Hit or Stand ?: ").strip().upper()
        if playerAction == "HIT" or playerAction == "H":
            new_card = random.choice(cards)
            cards.remove(new_card)
            playerCards.append(new_card)
            print(f"You got: {new_card}")
            print(f"Your Cards: {playerCards} \nYour Card Value: {calculateValue(playerCards)}")
        elif playerAction == "STAND" or playerAction == "S":
            break
        else:
            print("Invalid choice. Please enter 'Hit' or 'Stand'.")

# Check for Blackjack
def blackJackCheck():
    if calculateValue(playerCards) == 21:
        print("Blackjack! YOU WIN!")
    else:
        print("Dealer's turn...")

# Dealer's turn
def dealerHit():
    while calculateValue(houseCards) < 17:  # Dealer hits until the value is 17 or more
        new_card = random.choice(cards)
        cards.remove(new_card)
        houseCards.append(new_card)
        print(f"Dealer got: {new_card}")
    dealer_value = calculateValue(houseCards)
    print(f"Dealer's card value: {dealer_value}")
    
    if dealer_value > 21:
        print("Dealer Busts! You Win!")
    elif dealer_value >= calculateValue(playerCards):
        print(f"Dealer Wins! Dealer's cards: {houseCards}")
    else:
        print(f"You Win! Dealer's cards: {houseCards}")

# Game loop
while True:
    playerWantsToPlay = input("Play Blackjack? y/n : ").strip().upper()
    if playerWantsToPlay == "Y":
        print("Shuffling Deck...")
        deckManager()
        print(f"Cards remaining: {len(cards)}")
        
        # Start the game
        cardDeal()
        
        if calculateValue(playerCards) == 21:
            blackJackCheck()
        else:
            playHit()
            if calculateValue(playerCards) <= 21:
                dealerHit()
            else:
                print("You Lose! It's a bust! \n")
    else:
        print("Game Over \nThank you for playing <3")
        break
