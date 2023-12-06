import pythoncards as pc

def titlebar(): print("{:<20}".format('='*20))
print("{}{:^18}{}".format("|","Simple Card Game","|"))
print("{:<20}".format('='*20))
print()

titlebar()

player1 = input("Enter player 1: ") 
player2 = input("Enter player 2: ") 
print()

while True:

   deck = pc.SCardDeck()

   hand1 = pc.SHand(player1) 
   hand2 = pc.SHand(player2)

   for i in range(5): 
      hand1.add_card(deck.deal_card()) 
      hand2.add_card(deck.deal_card())

   print("{:<15} {} :value: {}".format(hand1.owner, hand1, hand1.get_value())) 
   print("{:<15} {} :value: {}".format(hand2.owner, hand2, hand2.get_value())) 
   print()
   if hand1.get_value() > hand2.get_value(): 
      print("*** {} is the winner! ***".format(hand1.owner)) 
   elif hand1.get_value() < hand2.get_value(): 
      print("*** {} is the winner! ***".format(hand2.owner)) 
   else: 
      print("*** It is a tie game! ***")
   print() 
   choice = input('Would you like to play again (y or n): ')
   if choice != 'y': 
      break