from deck import Deck
from player import Player
from dealer import Dealer
from betting import Betting

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        self.betting = Betting(self.player)
    
    def start_game(self):
        while True:
            bet = self.betting.place_bet()
            if bet is None:
                print("Insufficient balance or invalid bet.")
                break

            self.deck.shuffle()
            self.player.receive_card(self.deck.draw())
            self.player.receive_card(self.deck.draw())
            self.dealer.receive_card(self.deck.draw())
            self.dealer.receive_card(self.deck.draw())

            print(f"Your cards: {self.player.cards} Total: {self.player.calculate_hand()}")
            print(f"Dealer's face-up card: {self.dealer.cards[0]}")

            while self.player.calculate_hand() < 21:
                action = input("Do you want to [h]it or [s]tand? ")
                if action == 'h':
                    self.player.receive_card(self.deck.draw())
                    print(f"Your cards: {self.player.cards} Total: {self.player.calculate_hand()}")
                elif action == 's':
                    break

            while self.dealer.calculate_hand() < 17:
                self.dealer.receive_card(self.deck.draw())
            
            print(f"Dealer's cards: {self.dealer.cards} Total: {self.dealer.calculate_hand()}")
            
            if self.player.calculate_hand() > 21:
                print("You busted! Dealer wins.")
                self.player.lose_bet(bet)
            elif self.dealer.calculate_hand() > 21:
                print("Dealer busted! You win.")
                self.player.win_bet(bet)
            elif self.player.calculate_hand() > self.dealer.calculate_hand():
                print("You win!")
                self.player.win_bet(bet)
            elif self.player.calculate_hand() < self.dealer.calculate_hand():
                print("Dealer wins.")
                self.player.lose_bet(bet)
            else:
                print("It's a tie.")

            print(f"Your balance: {self.player.balance}")
            if self.player.balance <= 0:
                print("Game over! You've run out of money.")
                break

