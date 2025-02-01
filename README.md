# PythonCardGame
This project implements a 52-card deck simulator in Python. It includes features such as creating a deck, shuffling the cards, and drawing individual cards. Designed as a foundational tool for card-based games or learning Python object-oriented programming.

Section 1 :
Here we are importing Shuffle function from the Random Module . This is used make cards in the deck random .

Section 2 :
The Deck class is the heart of this project. It creates a proper deck of cards with all 52 cards using the four suits (Hearts, Diamonds, Clubs, Spades) and the 13 values (A, 2-10, J, Q, K). When you create an object of this class, it automatically generates the deck and stores it in a list called mycardset. There is also a popCard method, which lets you remove one card from the top of the deck. If all cards are already removed, it will simply tell you that no cards are left.

Section 3 :
The ShuffleCards class is an extension of the Deck class. It does everything the Deck class can do, but on top of that, it can shuffle the cards. There’s a shuffle method that mixes up the order of the deck. But one small thing – if the deck is incomplete (like if some cards are already popped out), it will not shuffle and will give a message instead.

Section 4 :
Here, the program creates an object of the Deck class and generates the complete deck of 52 cards. These cards are then assigned to a variable called player1Cards, which represents the cards for Player 1. At this stage, the deck is in order, meaning no shuffling has happened yet. The program prints out all the cards so you can see what Player 1 has.

Section 5:
This part shows how the ShuffleCards class works. First, it creates an object of ShuffleCards and shuffles the deck. After shuffling, the cards are assigned to player2Cards and printed to show the new order. Then the program uses the popCard method to remove and display two cards from the shuffled deck. This is just to demonstrate how the popping feature works and how the deck updates after cards are removed. 
