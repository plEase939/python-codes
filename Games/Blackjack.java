import java.util.ArrayList;
import java.util.Scanner;

public class Blackjack {

    private static final ArrayList<Object> cards = new ArrayList<>();
    private static final ArrayList<Object> houseCards = new ArrayList<>();
    private static final ArrayList<Object> playerCards = new ArrayList<>();
    private static final Scanner scanner = new Scanner(System.in);

    // Deck Manager
    private static void deckManager() {
        cards.clear();
        for (int count = 1; count <= 32; count++) {
            cards.add("ace");
            cards.add(10);
            cards.add(10);
            cards.add(10);
            for (int n = 2; n <= 10; n++) {
                cards.add(n);
            }
        }
    }

    // Deal cards to player and dealer
    private static void cardDeal() {
        houseCards.clear();
        playerCards.clear();
        for (int deal = 1; deal <= 2; deal++) {
            houseCards.add(drawCard());
            playerCards.add(drawCard());
        }
        System.out.println("Dealer has X and " + houseCards.get(1));
        handleAce(houseCards);
        System.out.println("You have " + playerCards.get(0) + " and " + playerCards.get(1));
        handleAce(playerCards);
        System.out.println("Your card value: " + calculateSum(playerCards) + "\n");
    }

    private static Object drawCard() {
        int randomIndex = (int) (Math.random() * cards.size());
        return cards.remove(randomIndex);
    }

    private static void handleAce(ArrayList<Object> hand) {
        if (hand.contains("ace")) {
            hand.remove("ace");
            hand.add(11);
        }
    }

    // Player chooses hit or stand
    private static void playHit() {
        while (calculateSum(playerCards) < 21) {
            System.out.print("Hit or Stand?: ");
            String action = scanner.nextLine();
            if (action.equalsIgnoreCase("hit") || action.equalsIgnoreCase("h")) {
                Object tempCard = drawCard();
                if (tempCard.equals("ace")) {
                    tempCard = 1;
                }
                playerCards.add(tempCard);
                System.out.println("You got: " + tempCard);
                System.out.println("Your cards: " + playerCards);
                System.out.println("Your card value: " + calculateSum(playerCards));
            } else {
                break;
            }
        }
    }

    // BlackJack check
    private static void blackJackCheck() {
        if (calculateSum(playerCards) == calculateSum(houseCards)) {
            System.out.println("Push! It's a DRAW.");
        } else {
            System.out.println("Blackjack! YOU WIN!");
            System.out.println("Dealer had: " + houseCards);
        }
    }

    // Dealer's turn
    private static void dealerHit() {
        int playerScore = calculateSum(playerCards);
        while (calculateSum(houseCards) < playerScore) {
            Object randomCard = drawCard();
            if (randomCard.equals("ace")) {
                randomCard = 1;
            }
            houseCards.add(randomCard);
            System.out.println("Dealer got: " + randomCard);
        }
        System.out.println("Dealer total card value: " + calculateSum(houseCards));
        if (calculateSum(houseCards) > playerScore && calculateSum(houseCards) <= 21) {
            System.out.println("House Wins! " + houseCards);
        } else {
            System.out.println("You Win!");
            System.out.println("Dealer Bust! His cards: " + houseCards);
        }
    }

    // Calculate hand value
    private static int calculateSum(ArrayList<Object> hand) {
        int sum = 0;
        for (Object card : hand) {
            if (card instanceof Integer) {
                sum += (int) card;
            } else if (card.equals("ace")) {
                sum += 11;
            }
        }
        return sum;
    }

    // Main game logic
    public static void main(String[] args) {
        while (true) {
            System.out.print("Play BlackJack? y/n: ");
            String playResponse = scanner.nextLine();
            if (playResponse.equalsIgnoreCase("y")) {
                System.out.println("Shuffling Deck...");
                deckManager();
                System.out.println("Deck size: " + cards.size()); //Test
            } else {
                System.out.println("Game Over \nThank you for playing <3");
                break;
            }

            // Game Logic
            cardDeal();
            if (calculateSum(playerCards) == 21) {
                blackJackCheck();
            } else {
                playHit();
                if (calculateSum(playerCards) < 21) {
                    dealerHit();
                } else {
                    System.out.println("You Lose! It's a bust!");
                }
            }
        }
    }
}
