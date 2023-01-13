import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} de {self.suit}'

    def get_value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11
        else:
            return int(self.rank)

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['Inima rosie', 'Romb', 'Trefla', 'Inima neagra']:
            for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def draw(self, deck):
        card = deck.deal()
        self.hand.append(card)
        self.score += card.get_value()

    def show_hand(self):
        for card in self.hand:
            print(card)

    def get_score(self):
        return self.score

def play_blackjack():
    deck = Deck()
    deck.shuffle()

    player = Player('Player')
    dealer = Player('Dealer')

    player.draw(deck)
    player.draw(deck)
    player.show_hand()

    dealer.draw(deck)
    dealer.draw(deck)

    while player.get_score() < 21:
        choice = input('Vrei sa tragi sau te opresti? ')
        if choice.lower() == 'trag':
            player.draw(deck)
            player.show_hand()
        else:
            break

    if player.get_score() > 21:
        return f'{player.name} pierdut! {dealer.name} castiga.'
    else:
        while dealer.get_score() < 17:
            dealer.draw(deck)

        if dealer.get_score() > 21:
            return f'{dealer.name} pierde! {player.name} castiga.'
        elif dealer.get_score() > player.get_score():
            return f'{dealer.name} castiga cu un scor de {dealer.get_score()}'
        elif dealer.get_score() < player.get_score():
            return f'{player.name} castiga cu un scor de {player.get_score()}'
        else:
            return "Egal!"

result = play_blackjack()
print(result)



