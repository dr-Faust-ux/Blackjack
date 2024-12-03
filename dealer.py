class Dealer:
    def __init__(self):
        self.cards = []
    
    def receive_card(self, card):
        self.cards.append(card)
    
    def calculate_hand(self):
        total = 0
        ace_count = 0
        for card in self.cards:
            if card[0] in ['J', 'Q', 'K']:
                total += 10
            elif card[0] == 'A':
                total += 11
                ace_count += 1
            else:
                total += int(card[0])
        
        while total > 21 and ace_count:
            total -= 10
            ace_count -= 1
        
        return total

