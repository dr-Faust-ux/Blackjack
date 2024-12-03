class Betting:
    def __init__(self, player):
        self.player = player
    
    def place_bet(self):
        bet = int(input(f"Your balance: {self.player.balance}. Place your bet: "))
        if bet > self.player.balance or bet <= 0:
            return None
        self.player.balance -= bet
        return bet

