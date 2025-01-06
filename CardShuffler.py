from random import shuffle

class Deck:
    suites = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self):
        self.mycardset = []
        for suite in self.suites:
            for value in self.values:
                self.mycardset.append(f"{value} of {suite}")

    def popCard(self):
        if len(self.mycardset) == 0:
            return "NO CARDS CAN BE POPPED FURTHER"
        else:
            return self.mycardset.pop()

class ShuffleCards(Deck):
    def __init__(self):
        super().__init__()

    def shuffle(self):
        if len(self.mycardset) < 52:
            print("Cannot shuffle the cards. The deck is incomplete.")
        else:
            shuffle(self.mycardset)
            return self.mycardset

objDeck = Deck()
player1Cards = objDeck.mycardset
print('\nPlayer 1 Cards:\n', player1Cards)

objShuffleCards = ShuffleCards()
player2Cards = objShuffleCards.shuffle()

if player2Cards:
    print('\nPlayer 2 Cards (Shuffled):\n', player2Cards)

print('\nRemoving a card from the deck:', objShuffleCards.popCard())
print('Removing another card from the deck:', objShuffleCards.popCard())
