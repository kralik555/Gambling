import random


class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value



class Player:
    def __init__(self, name, money):
        self.name = name
        self.hand = []
        self.money = money

    def display_hand(self):
        print(self.hand)

    def receive_cards(cards):
        self.hand = cards

    def receive_money(money):
        self.money += money

    def bet_money(money):
        self.money -= money


class Deck:
    def __init__(self):
        colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = range(2, 15)
        self.deck = [Card(color, value) for color in colors for value in values]

    def shuffle(self):
        self.deck = random.shuffle(self.deck)
        return self.deck

    def deal_cards(self, num_cards):
        cards = []
        for i in range(num_cards):
            card = self.deck.pop()
            cards.append(card)
        return cards


class Game:
    def __init__(self, players):
        self.num_players = len(players)
        self.cards = Deck().shuffle()
        self.table = []
        self.bets = {}
        self.is_first_round = True

    def add_player(player):
        self.players.append(player)
        self.num_players = len(players)

    def remove_player(player):
        if player in self.players:
            self.players.remove(player)
        self.num_players = len(self.players)

    def deal_cards_to_players(self):
        for player in self.players:
            cards = []
            for i in range(2):
                card = self.cards.pop()
                cards.append(card)
            player.receive_cards(cards)

    def deal_card_on_table(self):
        self.table.append(self.cards.pop())

    def turn(self):
        if self.is_first_round:
            pass
        self.is_first_round = False
    
    def player_turn(self, player):
        # if bets are higher than has can fold or 
        # match the bets or raise - max increase = all in
        # if no hgher bets can check or raise
        # theoretically also fold
        # also special shit for first round
        pass

    def determine_winner(self):
        winner []
        for player in players:
            pass
        # determine how good their cards are
        # if better than current winner -> new winner
        # if the same -> two winners

    def return_table(self):
        return self.table

    def self.reward_winners(self, winners):
        total_bets = sum(self.bets.values())
        reward = total_bets / len(winners)
        for player in winners:
            player.receive_money(reward)

    def play_game(self):
        self.deal_cards_to_players()
        for i in range(3):
            self.deal_card_on_table()
        for i in range(3):
            # play turn
        winners = self.determine_winner()
        self.reward_winners(winners)
        return
        
    
def one_game(Game, players)
