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

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

DEALER_WIN = 0
PLAYER_WIN = 0

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
        
# define hand class
class Hand:
    def __init__(self):
        self.card_list = []

    def __str__(self):
        ans = ""
        for i in range(len(self.card_list)):
            ans += str(self.card_list[i]) + ' '
        return ans

    def add_card(self, card):
        self.card_list.append(card)

    def get_value(self):
        val = 0
        ace = 0
        for i in self.card_list:
            val += VALUES[i.get_rank()]
            
            if i.get_rank() == 'A':
                ace += 1
            
        if ace == 0:
            return val
        elif val +10 <= 21:
            return val+10
        else:
            return val
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        for i in self.card_list:
            i.draw(canvas, pos)
            pos[0] += 73
    # draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.shuffle_list = []
        for i in SUITS:
            for r in RANKS:
                self.shuffle_list.append(Card(i,r))
        # create a Deck object

    def shuffle(self):
        return random.shuffle(self.shuffle_list)
        # shuffle the deck 

    def deal_card(self):
        return self.shuffle_list.pop()
        # deal a card object from the deck
    
    def __str__(self):
        ans = ""
        for i in range(len(self.shuffle_list)):
            ans += str(self.shuffle_list[i]) + ' '
        return ans
        # return a string representing the deck


#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, deal_hand, test_deck

    # your code goes here
    
    in_play = True
    test_deck = Deck()
    test_deck.shuffle()
    
    print 'start'
    
    player_hand = Hand()
    player_hand.add_card(test_deck.deal_card())
    player_hand.add_card(test_deck.deal_card())
    print 'player - ', player_hand, player_hand.get_value()
    
    
    deal_hand = Hand()
    deal_hand.add_card(test_deck.deal_card())
    deal_hand.add_card(test_deck.deal_card())
    print 'dealer - ',deal_hand, deal_hand.get_value()

    
def hit():
    global in_play, player_hand, deal_hand, DEALER_WIN
    
    in_play = True
    
    if in_play and player_hand.get_value() <= 21:
        player_hand.add_card(test_deck.deal_card())

        print 'dealer', deal_hand, deal_hand.get_value()
        print 'player', player_hand, player_hand.get_value()
        if player_hand.get_value() > 21:
            DEALER_WIN += 1
            in_play = False
            print 'player -- You have busted'
    
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score

def stand():

    global in_play, player_hand, deal_hand, DEALER_WIN, PLAYER_WIN

    while deal_hand.get_value() < 17:
        deal_hand.add_card(test_deck.deal_card())
    print 'deal lost player win'

    if deal_hand.get_value() > 21:
        print 'dealer busted'
        PLAYER_WIN += 1

    if player_hand.get_value() <= deal_hand.get_value():
        print 'dealer win'
        DEALER_WIN += 1
    else:
        PLAYER_WIN += 1
        print 'player win'

   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    global DEALER_WIN, PLAYER_WIN
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text('Blackjack', [240,50], 40, 'Red')
    canvas.draw_text('Dealer ' + str(DEALER_WIN), [500, 50], 20 ,"Black")
    canvas.draw_text('Player ' + str(PLAYER_WIN), [500, 90], 20 ,"Black")
    
    player_hand.draw(canvas, [150,400])
    deal_hand.draw(canvas, [150,100])
    


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