/**
 * Ctci 7.1
 * Deck of Cards: Design the data structures for a generic deck of cards.
 * Explain how you would subclass the data structures to implement blackjack.
 * 
 * Clarifications:
 * 1) Who - sr. citizens in a nurising home
 * 2) Why - use it on game night to socialize;
 *          digital b/c of COVID-19
 * 3) what - deck of cards, 
 * 4) how - extended to make Blackjack
 * 5) When - weekly use
 * 6) Where - via a web app
 * 
 * Assumptions:
 * 1) we don't need to worry about making the cards readable
 * 2) we could have multiple decks of cards in play at the same time, so no need to use a singleton
 * 3) factory method might be useful
 * 4) only worrying about creating a standard deck of cards
 * 
 * Define Core Objects (one idea)
 * 1) Deck class = one to many relationship w/ Card class
 *      Properties:
 *          1) String gameType - at instaniation the client tells the constructor what kind of deck it wants
 *          - this lets us instaniate an array - maps each array index to a cardType needed in the game
 *          - and also a HashMap - maps each cardType to its current number of cards in the deck
 * 
 *          - another idea is of course
 *              - HashMap of 4 suits - array of 13 spaces for the ranks, marked one or zero depending on if the card is in play, or in the deck
 *          2) boolean includeJoker = sometimes games like Blackjack don't use it
 *          3) int isAceHigh = 1 means ace > king, 0 mean is both above king and below 2, -1 means it is "ace low"
 *      Methods:
 *          1) size
 *          2) drawCard 
 *          3) addCard
 *          4) shuffle?
 * 
 * 2) Card class = standard deck of 52
 *      Properties:
 *          1) String rank: 2-10, jack, queen, king, ace
 *          2) String suit: hearts, diamonds, spades, clubs
 * 
 *      Methods
 *          1) isRed = true if the suit is a diamond or heart, false otherwise
 *          2) isFace = true if rank is jack/queen/king
 *      
 * 
 *
 * 2) Suits of Card class are extended to fit several games - Blackjack, 
 * 
 */


import java.util.HashMap;


public class DeckOfCards {
    int isAceHigh;
    boolean includeJoker;
    String name;
    HashMap<String, int[]> cards;

    public DeckOfCards(int isAceHigh, boolean includeJoker, String name) {
        this.isAceHigh = isAceHigh;
        this.includeJoker = includeJoker;
        this.name = name;

        this.setCards();
    }

    public DeckOfCards() {
        if (this.name != null) {
            this.setCards();
        }
    }

    public void setCards() {
        // define the suit names
        String[] suits = {
            "heart", "diamond", "spade", "club"
        };
        // instantiate arrays to track each suit
        for (String suit: suits) {
            // all ranks start out in the deck (0) initially
            int[] availableCards = new int[13];
            this.cards.put(suit, availableCards);
        }
        // optional: include joker
        if (this.gameType.includeJoker == true) {
            this.cards.put("joker", new int[2]);
        }
    }

}

public class Card {
    // String rank:2-10,jack,queen,king,ace*2)
    // String suit:hearts,diamonds,spades,clubs,joker
    String rank, suit;

    public Card(String r, String s) {
        this.rank = r;
        this.suit = s;
    }
}


///////// BLACKJACK //////////

public class BlackJackDeck extends DeckOfCards {
    public BlackJackDeck() {
        // init the game rules
        super(0, false, "blackjack");
    }
}


