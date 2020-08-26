#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}


playing = True


# In[ ]:


class Card:
    
    def _init_(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def _str_(self):
        return self.rank+ 'of'+self.suit


# In[ ]:


class Deck:
    
    def _init_(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(card(suit,rank))
                
    def _str_(self):
        deck_comp = ''
        for card  in self.deck:
            deck_comp += '\n'+ card _str_()
        return 'the deck has:'+deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card
       


# In[ ]:


class Hand:
    def _init_(self):
        self.cards = []
        self.values = 0
        self.aces = 0
        
    def add_card(self,card):
        self.cards.append(card)
        self.values += values[card.rank]
        
        #track aces
        if card.rank == 'Ace'
        self.aces += 1
        
    def adjust_for_ace(self):
        #
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# In[ ]:


class Chips:
    def _init_(self,total=100):
        self.total = 100
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet
        
        


# In[ ]:


def take_bet(chips):
    
    while True:
        
        try:
            chips.bet = int(input('how many chips would you like to bet?'))
        except:
            print('sorry please give an integer')
        else:
            if chips.bet > chips.total:
                print('sorry, dont have enough chips! you have: {}'.format(chips.total))
            else:
                break


# In[ ]:


def hit(deck,hand):
    
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


# In[ ]:


def hit_or_stand(deck,hand):
    global playing
    
    while True:
        x = input('Hit or stand? Enter H or S ')
        
        if x[0].lower() == 'h':
            hit(deck,hand)
        
        elif x[0].lower() == 's':
            print('player stand dealers turn')
            playing = False
            
        else:
            print('sorry, i did not understand that, please enter h or s!')
            continue
            
        break


# In[ ]:


def show_some(payer,dealer):
    
    print('dealers hand:')
    print('one card hidden')
    print(dealer.cards[1])
    print('\n')
    print('players hand:')
    for card in player.cards:
        print(card)
        
def show_all(player,dealer):
    
    print('dealers hand:')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('players hand:')
    for card in player.cards:
        print(card)


# In[ ]:


def player_busts(player,dealer,chips):
    print('Bust players')
    chip.lose_bet()
    
def player_wins(player,dealer,chips):
    print('player wins')
    chips.win_bet()
    
def dealer_busts(player,dealer,chips):
    print('player wins dealer busted')
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print('dealer wins')
    chips.lose_bet()
    
def push(player,dealer):
    print('dealer and player tie')


# In[ ]:


while True:
    print('welcome to balck jack game')
    
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    player_chips = chips()
    
    take_bet(player_chips)
    
    show_some(player_hand,dealer-hand)
    while playing:
        
        hit_or_stand(deck,player_hand)
        
        
        show_some(player-hand,dealer-hand)
        
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            
            break
            
    if player_hand.value <= 21:
        
        while dealer_hand.value < player_hand.value:
            hit(deck,dealer_hand)
            
            
        show_all(player_hand,dealer_hand)
        
        
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            
        else:
            push(player_hand,dealer_hand)
            
            
    print('\n player total chips are at: {}'.format(player_chips.total))
    
    new_game = input('would u like to play another hand? y or n')
    
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('thankyou for playing')
        break
            
            
    
    
    

