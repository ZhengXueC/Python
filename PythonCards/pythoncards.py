import random

# define a card class
class Card:
    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank
        
    def __str__(self):
        # concatenation works because both are strings in the lists above
        return self._suit + self._rank

    def get_suit(self):
        return self._suit

    def get_rank(self):
        return self._rank

    
        
#Define French Standard Card inherit from Card
class SCard(Card):
    
    # Defining values for cards (Class Attributes) 
    SUITS = ('S', 'C', 'H', 'D')
    RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
    CARDPIC ={'S':'\u2660', 'C':'\u2663', 'H':'\u2665', 'D':'\u2666'}
        
    def __init__(self,suit, rank):
        
        if (suit in SCard.SUITS) and (rank in SCard.RANKS):
            # assign
            super().__init__(suit, rank)
        else:
            # None is a special default value in Python
            raise ValueError("Invalid suit or rank ({}{}".format(suit,rank))
        
    def __str__(self):
            # concatenation works because both are strings in the lists above
            return SCard.CARDPIC[self._suit] + self._rank        
        
    
        
# define deck class

class CardDeck:
    def __init__(self, deck):
        
        self._deck = deck 
        
    # add cards back to deck and shuffle
    def deckshuffle(self):
        # modifies list deck, so no assignment needed
        random.shuffle(self._deck)

    def deal_card(self):
        ''' pick the last one from the deck. Remove it and return.'''
        return self._deck.pop()
    
    def __str__(self):
        s = ', '.join([str(crd) for crd in self._deck])
        return s
    
class SCardDeck(CardDeck):
    def __init__(self):
        
        SUITS = SCard.SUITS
        RANKS = SCard.RANKS
        
        deck = [SCard(suit, rank) for suit in SUITS for rank in RANKS]
        
        super().__init__(deck)
        
        self.deckshuffle()
        
# define hand class
class Hand:
    
    def __init__(self, owner):
        # hand is a list of cards. Start empty.
        self.cards = []
        self.owner = owner
        
    def __str__(self):
        s = ', '.join([str(crd) for crd in self.cards])
        return s
      
    def add_card(self, card):
        ''' add this card to the hand list '''
        self.cards.append(card)
        
    def get_card(self, pos):
        ''' retrieve rank and suit of a card given its position in the hand '''
        return self.cards[pos]

    def number_cards(self):
        #count how many cards are now in the hand.
        return len(self.cards)
          
    
    
class SHand(Hand):
    
    VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}
    
    def __init__(self, owner):
            super().__init__(owner)
     
    
    def get_value(self):
        ''' calculate simple total value of the hand '''
        value = 0 
        
        for card in self.cards:
            value += SHand.VALUES[card.get_rank()]
         
        return value
         
    def count_aces(self):
        ''' go through the hand and count aces '''
        #print("Hand count Aces")
        aces = 0
        for crd in self.cards:
            if crd.get_rank() == 'A':
                aces += 1
        #print("Aces: ", aces)
        return aces    
                
       
    
    
