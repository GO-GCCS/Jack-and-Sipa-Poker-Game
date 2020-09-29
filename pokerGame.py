# The Poker Game

import random
import sys

"""Important Visualisation Functions"""


def value(card):
    if card > 39:
        card = card - 39
    elif card > 26:
        card = card - 26
    elif card > 13:
        card = card - 13
    else:
        card = card
    return card


def suit(card):
    if card > 39:
        card = 4
    elif card > 26:
        card = 3
    elif card > 13:
        card = 2
    else:
        card = 1
    return card


"""Variables"""
# possibleCards
card = 0
# player variables
player1Cards = []
player2Cards = []
# player variables shown
# playerCard check
passedCards = []
cardValue = ''
# discarded cards
discarded = []
#money
pot = 0
player1funds = 1000
player2funds = 1000
player1bet = 0
player2bet = 0
total_player1bet = 0
total_player2bet = 0


"""Player Cards shown"""


def shown_card(card):
    if value(card) == 1:
        return 'A'
    elif value(card) == 11:
        return 'J'
    elif value(card) == 12:
        return 'Q'
    elif value(card) == 13:
        return 'K'
    else:
        return str(value(card))


def shown_suit(card):
    if suit(card) == 1:
        return "\U00002665"
    elif suit(card) == 2:
        return "\U00002664"
    elif suit(card) == 3:
        return "\U00002666"
    else:
        return "\U00002667"


"""Start of Actual Fucking Game"""


while True:
    if input("Please press enter to start") == '':
        break


"""Betting"""
player2bet = 0
p = 0

player1bet = int(input("Please enter the amount you want to bet player1"))
print("Player1's bet amounts to " + str(player1bet))

while True:
    if p == 0:
        player2bet += int(input("Please enter the amount you want to bet player2"))
        print("Player2's bet amounts to " + str(player2bet))
        p += 1
        if player1bet == player2bet:
            break
    elif p == 1:
        player1bet += int(input("Please enter the amount you want to bet player1"))
        print("Player1's bet amounts to " + str(player1bet))
        p -= 1
        if player1bet == player2bet:
            break

player1funds -= player1bet
player2funds -= player2bet

total_player1bet += player1bet
total_player2bet += player2bet

pot += player1bet + player2bet
print('')
print("The pot is now at " + str(pot) + " chips")
print('')
print("Player1's current balance is " + str(player1funds) + "chips")
print("Player2's current balance is " + str(player2funds) + "chips")
print('')
print('')
print('')


# TURN 1
# your turn
"""If you know the the number of times you want your loop to run, then use for loop  as its cleaner"""
n = 0
for i in range(5):
    card = random.randint(1, 52)
    # Checking whether the card is already in game
    if cardValue in passedCards:
        i -= 1
        continue
    else:
        passedCards.append(card)
        player1Cards.append(card)


# computer turn
n = 0
for i in range(5):
    card = random.randint(1, 52)
    # Checking whether the card is already in game
    if cardValue in passedCards:
        i -= 1
        continue
    else:
        passedCards.append(card)
        player2Cards.append(card)

# print(str(player1Cards))
shown_cards1 = ''
for i in range(4):
    shown_cards1 = shown_cards1 + \
        shown_card(player1Cards[i]) + shown_suit(player1Cards[i]) + ' '
    if i == 3:
        shown_cards1 = shown_cards1 + \
            shown_card(player1Cards[4]) + shown_suit(player1Cards[4])

print("Player 1's cards are " + shown_cards1)
print('')
# print(player1Cards)
shown_cards2 = ''
for i in range(4):
    shown_cards2 = shown_cards2 + \
        shown_card(player2Cards[i]) + shown_suit(player2Cards[i]) + ' '
    if i == 3:
        shown_cards2 = shown_cards2 + \
            shown_card(player2Cards[4]) + shown_suit(player2Cards[4])
print("Player 2's cards are " + shown_cards2)
print('')


"""TURN 2"""

"""Betting"""
player2bet = 0
p = 0

player1bet = int(input("Please enter the amount you want to bet player1"))
print("Player1's bet amounts to " + str(player1bet))

while True:
    if p == 0:
        player2bet += int(input("Please enter the amount you want to bet player2"))
        print("Player2's bet amounts to " + str(player2bet))
        p += 1
        if player1bet == player2bet:
            break
    elif p == 1:
        player1bet += int(input("Please enter the amount you want to bet player1"))
        print("Player1's bet amounts to " + str(player1bet))
        p -= 1
        if player1bet == player2bet:
            break

player1funds -= player1bet
player2funds -= player2bet

total_player1bet += player1bet
total_player2bet += player2bet

pot += player1bet + player2bet
print('')
print("The pot is now at " + str(pot) + " chips")
print('')
print("Player1's current balance is " + str(player1funds) + "chips")
print("Player2's current balance is " + str(player2funds) + "chips")
print('')
print('')
print('')

# player 1
print('Player 1, if you want to change one or more cards, write the numbers and then press enter')

discarded1 = input()
numOfDiscarded = 0

if '5' in discarded1:
    del player1Cards[4]
    numOfDiscarded = numOfDiscarded + 1

if '4' in discarded1:
    del player1Cards[3]
    numOfDiscarded = numOfDiscarded + 1

if '3' in discarded1:
    del player1Cards[2]
    numOfDiscarded = numOfDiscarded + 1

if '2' in discarded1:
    del player1Cards[1]
    numOfDiscarded = numOfDiscarded + 1

if '1' in discarded1:
    del player1Cards[0]
    numOfDiscarded = numOfDiscarded + 1

i = 0
while i <= numOfDiscarded:
    card = random.randint(1, 52)
    if card in passedCards:
        continue
    else:
        passedCards.append(card)
        player1Cards.append(card)
        i = i + 1

shown_cards1 = ''
for i in range(4):
    shown_cards1 = shown_cards1 + \
        shown_card(player1Cards[i]) + shown_suit(player1Cards[i]) + ' '
    if i == 3:
        shown_cards1 = shown_cards1 + \
            shown_card(player1Cards[4]) + shown_suit(player1Cards[4])

print("Player1, your new cards are: " + shown_cards1)

# player 2
print('Player 2, if you want to change one or more cards, write the numbers and then press enter')
discarded2 = input()
numOfDiscarded = 0

if '5' in discarded2:
    del player2Cards[4]
    numOfDiscarded = numOfDiscarded + 1

if '4' in discarded2:
    del player2Cards[3]
    numOfDiscarded = numOfDiscarded + 1

if '3' in discarded2:
    del player2Cards[2]
    numOfDiscarded = numOfDiscarded + 1

if '2' in discarded2:
    del player2Cards[1]
    numOfDiscarded = numOfDiscarded + 1

if '1' in discarded2:
    del player2Cards[0]
    numOfDiscarded = numOfDiscarded + 1

i = 0
while i <= numOfDiscarded:
    card = random.randint(1, 52)
    if card in passedCards:
        continue
    else:
        passedCards.append(card)
        player2Cards.append(card)
        i = i + 1

shown_cards2 = ''
for i in range(4):
    shown_cards2 = shown_cards2 + \
        shown_card(player2Cards[i]) + shown_suit(player2Cards[i]) + ' '
    if i == 3:
        shown_cards2 = shown_cards2 + \
            shown_card(player2Cards[4]) + shown_suit(player2Cards[4])

print("Player2, your new cards are: " + shown_cards2)


"""Betting"""
player2bet = 0
p = 0

player1bet = int(input("Please enter the amount you want to bet player1"))
print("Player1's bet amounts to " + str(player1bet))

while True:
    if p == 0:
        player2bet += int(input("Please enter the amount you want to bet player2"))
        print("Player2's bet amounts to " + str(player2bet))
        p += 1
        if player1bet == player2bet:
            break
    elif p == 1:
        player1bet += int(input("Please enter the amount you want to bet player1"))
        print("Player1's bet amounts to " + str(player1bet))
        p -= 1
        if player1bet == player2bet:
            break


"""Determining the Winner"""


# straight flush
def straight_flush(card1, card2, card3, card4, card5):
    if value(card1) == value(card2) - 1 == value(card3) - 2 == value(card4) - 3 == value(card5) - 4 or value(card1)\
            == value(card2) - 1 == value(card3) - 2 == value(card4) - 3 == value(card5) + 13:
        if flush(card1, card2, card3, card4, card5) == card1 and value(card1) not in (11, 12, 13):
            return True
        else:
            return False
    else:
        return False


# straight
def straight(card1, card2, card3, card4, card5):
    if value(card1) == value(card2) - 1 == value(card3) - 2 == value(card4) - 3 == value(card5) - 4 or value(card1)\
            == value(card2) - 1 == value(card3) - 2 == value(card4) - 3 == value(card5) + 13:
        if not flush(card1, card2, card3, card4, card5) and value(card1) not in (11, 12, 13):
            return True
        else:
            return False
    else:
        return False


# flush
def flush(card1, card2, card3, card4, card5):
    if suit(card1) == suit(card2) == suit(card3) == suit(card4) == suit(card5):
        return True
    else:
        return False


# 4 of a kind
def four_of_a_kind(card1, card2, card3, card4, card5):
    if value(card1) == value(card2) == value(card3) == value(card4) or value(card2) == value(card3)\
            == value(card4) == value(card5):
        return True
    else:
        return False


# full house
def full_house(card1, card2, card3, card4, card5):
    if value(card1) == value(card2) == value(card3) and value(card4) == value(card5):
        return True
    elif value(card1) == value(card2) and value(card3) == value(card4) == value(card5):
        return True
    else:
        return False


# 3 of a kind
def three_of_a_kind(card1, card2, card3, card4, card5):
    if not four_of_a_kind:
        if value(card1) == value(card2) == value(card3) or value(card2) == value(card3) == value(card4)\
                or value(card3) == value(card4) == value(card5):
            return True
        else:
            return False
    else:
        return False


# 2 pairs
def two_pairs(card1, card2, card3, card4, card5):
    if not four_of_a_kind and not three_of_a_kind:
        if value(card1) == value(card2):
            if value(card3) == value(card4):
                return True
            elif value(card4) == value(card5):
                return True
            else:
                return False
        elif value(card2) == value(card3) and value(card4) == value(card5):
            return True
        else:
            return False
    else:
        return False


# pair
def pair(card1, card2, card3, card4, card5):
    if four_of_a_kind(card1, card2, card3, card4, card5) is True or three_of_a_kind(card1, card2, card3, card4, card5)\
            is True or two_pairs(card1, card2, card3, card4, card5) is True:
        return False
    else:
        if value(card1) == value(card2):
            return True
        elif value(card2) == value(card3):
            return True
        elif value(card3) == value(card4):
            return True
        elif value(card4) == value(card5):
            return True

# Player 1 Score


player1Cards.sort()
card1 = player1Cards[0]
card2 = player1Cards[1]
card3 = player1Cards[2]
card4 = player1Cards[3]
card5 = player1Cards[4]

if straight_flush(card1, card2, card3, card4, card5):
    player1score = 9
elif four_of_a_kind(card1, card2, card3, card4, card5):
    player1score = 8
elif full_house(card1, card2, card3, card4, card5):
    player1score = 7
elif flush(card1, card2, card3, card4, card5):
    player1score = 6
elif straight(card1, card2, card3, card4, card5):
    player1score = 5
elif three_of_a_kind(card1, card2, card3, card4, card5):
    player1score = 4
elif two_pairs(card1, card2, card3, card4, card5):
    player1score = 3
elif pair(card1, card2, card3, card4, card5):
    player1score = 2
else:
    if value(player1Cards[0]) == 1:
        player1score = 1
    else:
        player1score = 0


# Player 2 Score
player2Cards.sort()
card1 = player2Cards[0]
card2 = player2Cards[1]
card3 = player2Cards[2]
card4 = player2Cards[3]
card5 = player2Cards[4]

if straight_flush(card1, card2, card3, card4, card5):
    player2score = 9
elif four_of_a_kind(card1, card2, card3, card4, card5):
    player2score = 8
elif full_house(card1, card2, card3, card4, card5):
    player2score = 7
elif flush(card1, card2, card3, card4, card5):
    player2score = 6
elif straight(card1, card2, card3, card4, card5):
    player2score = 5
elif three_of_a_kind(card1, card2, card3, card4, card5):
    player2score = 4
elif two_pairs(card1, card2, card3, card4, card5):
    player2score = 3
elif pair(card1, card2, card3, card4, card5):
    player2score = 2
else:
    if value(player2Cards[0]) == 1:
        player2score = 1
    else:
        player2score = 0

if player1score > player2score:
    print('Player 1 is Awesome, He wins')
    print('')
    print("Player 2 is a f***ing loser, he's the worst cock-sucking penguin molester who has ever given me the "
          "displeasure of playing this game")
elif player1score < player2score:
    print('Player 2 is Awesome, He wins')
    print('')
    print("Player 1 is a f***ing loser, he's the worst cock-sucking penguin molester who has ever given me the "
          "displeasure of playing this game")
else:
    player1score = value(player1Cards[4])
    player2score = value(player2Cards[4])
    if player1score > player2score:
        print('Player 1 is Awesome, He wins')
        print('')
        print("Player 2 is a f***ing loser, he's the worst cock-sucking penguin molester who has ever given me the "
              "displeasure of playing this game")
    elif player1score < player2score:
        print('Player 2 is Awesome, He wins')
        print('')
        print("Player 1 is a f***ing loser, he's the worst cock-sucking penguin molester who has ever given me the "
              "displeasure of playing this game")
    else:
        print("It's a f***ing draw. A draw. How in the the name of GCCS did you manage that?")
