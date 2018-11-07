import cards
import time

class Player:
    def __init__(self):
        self.hand = []
        self.handVal = 0
    def draw(self, deck, num = 1):
        pCards = deck.draw(num)
        for i in pCards:
            self.hand.append(i)
        self.handVal = self._calcHandValue()
    def _calcHandValue(self):
        value = 0
        aces = 0
        for c in self.hand:
            if c.rank_id == 1 or c.rank_id == 14:
                aces+=1
            else:
                value += c.rank_id if c.rank_id<10 else 10
        for i in range(aces):
            if value+11 > 21:
                value+=1
            else:
                value+=11
        return value
        
        

money = 500

run = True

print("Welcome to Blackjack! Type \"exit\" at any time to close Blackjack.")
time.sleep(1.5)
while run == True:
    # set up variables and deck
    possibleBlackjack = True
    dealerPossibleBlackjack = True
    blackjack = False
    dealerBlackjack = False
    bust = False
    deck = cards.Deck()
    deck.shuffle()
    
    # get and validate the bet
    while True:
        bet = input("\nYou have ${}.  How much would you like to bet? ".format(money))
        if bet == "exit":
            exit()
        try:
            bet = int(bet)
            if bet!=0 and bet<=money:
                break
            else:
                print("That bet is not valid.")
        except:
            print("That bet is not valid.")

    # create the players and deal them hands
    p = Player()
    d = Player()
    p.draw(deck, 2)
    d.draw(deck, 2)
    time.sleep(1)
    print("\nThe dealer has a {} showing.".format(d.hand[0]))
    time.sleep(1)
    
    # make the player do his/her turn
    while True:
        print("\nYour cards are:")
        for i in p.hand:
            time.sleep(0.25)
            print("  {}".format(i))
        time.sleep(0.5)
        if possibleBlackjack and p.handVal == 21:
            print("\nYou got a Blackjack!  You got ${}.".format(bet*2))
            blackjack = True
            money+=bet*2
            break
        elif p.handVal > 21:
            print("\nYou busted. You lost ${}.".format(bet))
            money-=bet
            bust = True
            break
        else:
            possibleBlackjack = False
            hit = input("Do you want to hit? (y/n) ")
            if hit == "y":
                p.draw(deck)
            elif hit == "exit":
                exit()
            else:
                # make the dealer do its turn if needed
                while True:
                    if dealerPossibleBlackjack and d.handVal == 21:
                        dealerBlackjack = True
                        break
                    elif d.handVal < 17:
                        d.draw(deck)
                        dealerPossibleBlackjack = False
                    else:
                        break
                break
    time.sleep(2)

    # output what the dealer got
    print()
    if not bust and not blackjack:
        if dealerBlackjack == True:
            print("The dealer got a Blackjack.  You lost ${}.".format(bet))
            money-=bet
        elif d.handVal > 21:
            print("The dealer busted!  You got ${}.".format(bet))
            money += bet
        elif p.handVal > d.handVal:
            print("The dealer got {}.  You won! You got ${}.".format(d.handVal, bet))
            money+=bet
        elif p.handVal < d.handVal:
            print("The dealer got {}.  You lost ${}.".format(d.handVal, bet))
            money-=bet
        elif p.handVal == d.handVal:
            print("The dealer got {}.  You tied.  You didn't get any money.".format(d.handVal))
        time.sleep(2)

    # ask the player if he/she wants to play again if they have money
    q = input("\nDo you want to play again? (y/n) ".format(money))
    if q != "y" or not money:
        run = False

if not money and q == "y":
    print("\nYou don't have any money.")
    time.sleep(2)
