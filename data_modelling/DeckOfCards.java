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
 * 
 * Define Core Objects (one idea)
 * 1) Deck class = one to many relationship w/ Card class
 *      Properties:
 *          String gameType - at instaniation the client tells the constructor what kind of deck it wants
 *          1) this lets us instaniate an array - maps each array index to a cardType needed in the game
 *          2) and also a HashMap - maps each cardType to its current number of cards in the deck
 *      Methods:
 *          1) size
 *          2) drawCard 
 *          3) addCard
 *          4) shuffle?
 *
 * 2) Suits of Card class are extended to fit several games - Blackjack, 
 * 
 */

public class DeckOfCards {
    
}
