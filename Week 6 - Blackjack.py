# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
state = ""
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        if pos[0] == 50 and pos[1] == 200 and in_play == True:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        elif pos[0] == 50 and pos[1] == 200 and in_play == False:
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
# define hand class
class Hand:
    def __init__(self):
        self.cardlist = []

    def __str__(self):
        list = ""
        for i in range(len(self.cardlist)):
            list += " " + str(self.cardlist[i])
        return "Hand contains" + list

    def add_card(self, card):
        self.cardlist.append(card)

    def get_value(self):
        value = 0
        walue = 0
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        for i in range(len(self.cardlist)):
             value += VALUES.get(self.cardlist[i].get_rank())
             walue += VALUES.get(self.cardlist[i].get_rank())
             if self.cardlist[i].get_rank() == 'A':
                value += 10
             if self.cardlist[i].get_rank() == 'A' and value > 21:
                value = value - 10
        if value < 21:
            return value
        else:
            return walue
   
    def draw(self, canvas, pos):
        for i in range(len(self.cardlist)):
            self.cardlist[i].draw(canvas, pos)
            pos[0] += 100
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suits in SUITS:
            for ranks in RANKS:
                self.deck.append(Card(suits, ranks))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()
    
    def __str__(self):
        cardlist = ""
        for i in range(len(self.deck)):
            cardlist += str(self.deck[i]) + " "   
        return "Deck contains " + cardlist

#define event handlers for buttons
def deal():
    global outcome, in_play, player, dealer, deck, score, state
    outcome = "Hit or stand?"
    state = ""
    # your code goes here
    if in_play == True:
        in_play = False
        score -= 1
        outcome = "New deal?"
        state = "You lose!"
        #print "Score: " + str(score)
    else:
        in_play = True
    deck=Deck()
    deck.shuffle()
    player = Hand()
    dealer = Hand()
    player.add_card(deck.deal_card()), player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card()), dealer.add_card(deck.deal_card())
    #print "Player cards: " + str(player)
    #print "Dealer cards: " + str(dealer)

def hit():
    global in_play, score, state, outcome
    if player.get_value() <= 21 and in_play == True:
        player.add_card(deck.deal_card())
        #print "Player cards: " + str(player) + " Player value: " + str(player.get_value())
        if player.get_value() > 21:
            if in_play == True:
                state = "You lose!"
                outcome = "New deal?"
                in_play = False
                score -= 1
                #print "Score: " + str(score)
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global in_play, score, state, outcome
    if player.get_value() > 21 and in_play == True:
          state = "You lose!"
          outcome = "New deal?"
          in_play = False
    elif in_play == True: 
        while (dealer.get_value() <= 17):
            dealer.add_card(deck.deal_card())
        #print "Dealer cards: " + str(dealer) + " Dealer value: " + str(dealer.get_value())
        if dealer.get_value() > 21 and in_play == True:
              state = "You win!"
              outcome = "New deal?"
              score += 1
              #print "Score: " + str(score)
              in_play = False
        elif player.get_value() <= dealer.get_value() and in_play == True:
              state = "You lose!"
              outcome = "New deal?"
              score -= 1
              #print "Score: " + str(score)
              in_play = False
        elif in_play == True:
              state = "You win!"
              outcome = "New deal?"
              score += 1
              #print "Score: " + str(score)
              in_play = False
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text('Blackjack', (20, 60), 60, 'Black')
    canvas.draw_text("Score: " + str(score), (400, 60), 40, 'Black')
    canvas.draw_text(state, (300,180), 40, 'Black')
    canvas.draw_text(outcome, (300,380), 40, 'Black')
    canvas.draw_text("Player", (50,380), 40, 'Blue')
    canvas.draw_text("Dealer", (50,180), 40, 'Red')  
    dealer.draw(canvas, [50, 200])
    player.draw(canvas, [50, 400])
    #dealer.draw(canvas, [50, 200])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()


# remember to review the gradic rubric