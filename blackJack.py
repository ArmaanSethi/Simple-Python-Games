import random

class Player(object):
    """ A player for a game. """
    def __init__(self, name, money = 200):
        self.name = name
        self.money = money
        self.bet = 10
        self.hand = BJ_Hand()
        self.is_playing = True

    def change_bet(self, question):
        response = None
        while response not in range (0,int(self.money+1)):
            response = int(raw_input(self.name + ", " + question).lower())
        self.bet = response

    def not_playing(self):
        self.is_playing = False
        
    def win(self):
        print "Congradulations " + self.name + ", " + "YOU WIN"
        self.money = self.money + 2*(self.bet)
        
    def tie(self):
        print "Nice " + self.name + ", " + "YOU TIE"
        self.money = self.money + (self.bet)
        
    def BJ_win(self):
        print "Congradulations " + self.name + ", " + "YOU HAVE NATURAL BLACK JACK"
        self.is_playing = False
        self.money = int(self.money + (5.0/2)*(self.bet))

    def __str__(self):
        rep = self.name + "\t" + str(self.hand) + "Total: " + str(self.hand.total) + "\t" + "Money: " + str(self.money) + "\t" + "Bet: " + str(self.bet)
        return rep
    
class Dealer(Player):
    def __init__(self):
        self.name = "Dealer"
        self.hand = BJ_Hand()

    def __str__(self):
        rep = self.name + ":\t" + str(self.hand) + "Total: " + str(self.hand.total)
        return rep

    
def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = raw_input(question).lower()
    return response

def ask(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("split","hit","double down","stand"):
        response = raw_input(question).lower()
    return response


def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high+1):
        response = int(raw_input(question))
    return response

class Card(object):
    """ A playing card. """
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
    SUITS = ["C", "D", "H", "S"]

    def __init__(self, rank, suit, face_up = True):
        self.rank = rank 
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = self.rank + self.suit
        else:
            rep = "XX"
        return rep
    
    def get_value(self):
        if self.is_face_up:
            value = BJ_Card.RANKS.index(self.rank) + 1
            if value > 10:
                value = 10
        else:
            value = None
        return value

    value = property(get_value)    

    def flip(self):
        self.is_face_up = not self.is_face_up

class Hand(object):
    """ A hand of playing cards. """
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
           rep = ""
           for card in self.cards:
               rep += str(card) + "\t"
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    """ A deck of playing cards. """
    def __init__(self):
        super(Deck,self).__init__()
        self.cardCount = 0
    def rig_deck(self):
        self.add(Card("5","D"))
        self.add(Card("Q","D"))
        self.add(Card("Q","D"))
        self.add(Card("Q","D"))
        self.add(Card("J","D"))
        self.add(Card("5","D"))
        self.add(Card("J","D"))
        self.add(Card("J","D"))
        self.add(Card("J","D"))
        self.add(Card("J","D"))
        self.add(Card("A","D"))
        self.add(Card("J","D"))
        self.add(Card("J","D"))
        self.add(Card("J","D"))
        self.add(Card("A","D"))
        self.add(Card("J","D"))
        self.add(Card("J","D"))
        self.add(Card("J","D"))
        self.add(Card("J","D"))
        self.add(Card("J","D"))
        self.add(Card("J","D"))
        self.add(Card("A","D"))
        self.add(Card("J","D"))
        self.add(Card("J","D"))
    
            
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS: 
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)
                
    def deal(self, players, per_hand = 2):
        for rounds in range(per_hand):
            for p in players:
                if self.cards:
                    top_card = self.cards[0]
                    if top_card.get_value() < 5:
                        self.cardCount = self.cardCount + 1
                        print "CardCount+: " + str(self.cardCount)
                    elif top_card.get_value() > 9:
                        self.cardCount = self.cardCount - 1
                        print "CardCount-: " + str(self.cardCount)
                    self.give(top_card, p.hand)
                else:
                    print "Can't continue deal. Out of cards!"

class BJ_Card(Card):
    """ A Blackjack Card. """
    def get_value(self):
        if self.is_face_up:
            value = BJ_Card.RANKS.index(self.rank) + 1
            if value > 10:
                value = 10
        else:
            value = None
        return value

    value = property(get_value)    

class BJ_Hand(Hand):
    """ A Blackjack Hand. """
    def __str__(self):
        if self.cards:
            rep = "<"
            for card in self.cards:
                rep += str(card) + ","
            rep = rep[:len(rep)-1]
        else:
            rep = "<empty"
        return rep + ">" + "   \t"
     
    def get_total(self):
        total = 0
        contains_ace = 0
        # if a card in the hand has value of None, then total is None
        for card in self.cards:
            if not card.value:
                return None
        
        # add up card values, treat each Ace as 1
        for card in self.cards:
            total += card.get_value()
                
        # determine if hand contains an Ace
        for card in self.cards:
            if card.get_value() == 1:
                contains_ace = 1
                                 
        # if hand contains Ace and total is low enough, treat Ace as 11
        if contains_ace and total <= 11:
            # add only 10 since we've already added 1 for the Ace
            total += 10   
                
        return total

    total = property(get_total)

    def flip_card(self):
        self.cards[1].flip()

    def is_busted(self):
        return self.total > 21



"""class for BJ_Player and BJ_Dealer and all the win/loss situations
	make sure flip a card is included with dealer"""



class BJ_Game(object):
    """ A Blackjack Game. """
    def __init__(self):
        self.cardCount = 0
        self.players = []
        self.deck = Deck()
        self.deck.populate()
        self.deck.shuffle()
        #self.deck.rig_deck()
        num = ask_number(question = "How many players? (1 - 5): ",
                                   low = 1, high = 5)
        for i in range(num):
            name = raw_input("Player name: ")
            player = Player(name)
            self.players.append(player)
        self.players.append(Dealer())
        #self.print_players()

    def flip_dealer(self):
        self.players[len(self.players)-1].hand.flip_card()

    def print_players(self):
        print "\nHere are the players:"
        for player in self.players:
            print player

    def get_still_playing(self):
        playing = []
        for i in range(len(self.players)-1):
            if self.players[i].hand.total <= 21:
                if(self.players[i].is_playing):
                    playing.append(self.players[i])
        return playing
    #list of players still playing (not busted) this round
    still_playing = property(get_still_playing)

    def __additional_cards(self, player):
        #print "Check money, Split, Hit, Stand, DoubleDown"
        print player
        print player.name+",",
        idek = []
        idek.append(player)
        response = ""
        if(player.money >= player.bet):
            response = ask("Would you like to 'Double Down', 'Hit', or Stand'?")
        else:
            response = ask("Would you like to 'Hit', or Stand'?")
            
        if response == "double down":
            print "DOUBLED DOWN!!!"
            player.money = player.money - player.bet
            player.bet = player.bet*2
            self.deck.deal(idek,1)
            print player
        if response == "hit":

            self.deck.deal(idek,1)
            if(player.hand.total < 22):
                self.__additional_cards(player)
            else:
                print player
                print "BUST!!!"
                raw_input("Press the enter key to continue.")


                    
    def bet_amount(self, player):
        player.change_bet("How much would you like to bet?")
        player.money = player.money - player.bet
        

    def play(self):
        self.print_players()
        #bets
        print "Card Count: " +  str(self.deck.cardCount)
        for i in range(len(self.players)-1):
            self.bet_amount(self.players[i])
            
        print self.deck
        # deal initial 2 cards to everyone
        self.deck.deal(self.players)
        self.flip_dealer()
        self.print_players()
        print self.deck
        #self.flip_dealer()
        #self.print_players()
        """CHECK DEALER"""
        self.flip_dealer()
        print "VALUE OF DEALER CARD:   " + str(self.players[len(self.players)-1].hand.cards[0].get_value())
        
        if(self.players[len(self.players)-1].hand.cards[0].get_value() == 1):
            for p in self.still_playing:
                if p.hand.total == 21:
                    response = ask_yes_no(p.name + "," + "would you like even money?")
                    if response == "y":
                        p.win()
                        p.not_playing()
                else:
                    response = ask_yes_no(p.name + ", " + "would you like insurance?")
                    if response == "y":
                        if(self.players[len(self.players)-1].hand.total == 21):
                            p.money = p.money + (.5)*p.bet
                        else:
                            p.money = p.money - (.5)*p.bet

        if(self.players[len(self.players)-1].hand.total == 21):
            for p in self.still_playing:
                if p.hand.total == 21:
                    p.tie()
                p.not_playing()
            print "DEALER BLACK JACK!!! NOBODY WINS"
            
            
        if(self.players[len(self.players)-1].hand.cards[0].get_value() == 10):
            print "DEALER 10!!!!!"+"\n"
            if(self.players[len(self.players)-1].hand.total == 21):
                print "DEALER BLACK JACK!! NOBODY WINS"
                for p in self.still_playing:
                    if p.hand.total == 21:
                        p.tie()
                    p.not_playing()
            
        self.flip_dealer()
        """CHECK PLAYER"""
        for p in self.still_playing:
            if(p.hand.total == 21):
                p.BJ_win()
                
        """Normal Play"""
        # deal additional cards to players
        
        for p in self.still_playing:
            self.__additional_cards(p)

        #print "Players Still Playing :" + str(self.still_playing)
        
        if len(self.still_playing)== 0:
            print "There are no winners"
            self.flip_dealer()
            print self.players[len(self.players)-1]
        else:
            self.flip_dealer()
            idek = []
            idek.append(self.players[len(self.players)-1])
            while(self.players[len(self.players)-1].hand.total < 16):
                self.deck.deal(idek,1)

        """Show Dealer"""
        print "\n" + str(self.players[len(self.players)-1]) + "\n"
        
        if self.players[len(self.players)-1].hand.total > 21:
            print "DEALER BUSTS!!!!!!!"
            for player in self.still_playing:
                player.win()
                print player
        else:
            for player in self.still_playing:
                if(player.hand.total > self.players[len(self.players)-1].hand.total):
                    player.win()
                    print player
                if(player.hand.total == self.players[len(self.players)-1].hand.total):
                    player.tie()
                    print player
                

                # compare each player still playing to dealer
                
        # remove everyone's cards
        print "ROUND OVER" + "\n" + "\n"
        for p in self.players:
            p.hand.clear()
        self.print_players()

# main
def main():
    again = None
    game = BJ_Game()
    while again != "n":
        game.play()
        again = ask_yes_no("\nDo you want to play again? (y/n): ")

main()
raw_input("\n\nPress the enter key to exit.")

