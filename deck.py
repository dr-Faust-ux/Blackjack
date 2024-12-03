import random

class Deck:
    def __init__(self):
        self.cards = [
            [str(i), suit] for i in range(2, 11) for suit in ['♠', '♦', '♣', '♥']
        ] + [[face, suit] for face in ['J', 'Q', 'K', 'A'] for suit in ['♠', '♦', '♣', '♥']]
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self):
        return self.cards.pop()

