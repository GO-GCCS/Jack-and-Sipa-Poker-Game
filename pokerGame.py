# The Poker Game

import random

"""Important Visualisation Functions"""


def value(c):
    if c > 39:
        c -= 39
    elif c > 26:
        c -= 26
    elif c > 13:
        c -= 13
    else:
        c = c
    return c


def suit(c):
    if c > 39:
        c = 4
    elif c > 26:
        c = 3
    elif c > 13:
        c = 2
    else:
        c = 1
    return c


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
# money
player1_funds = 1000
player2_funds = 1000
player1_bet = 0
player2_bet = 0
pot = 0

"""Player Cards shown"""


def shown_card(c):
    if value(c) == 1:
        return 'A'
    elif value(c) == 11:
        return 'J'
    elif value(c) == 12:
        return 'Q'
    elif value(c) == 13:
        return 'K'
    else:
        return str(value(c))


def shown_suit(c):
    if suit(c) == 1:
        return "\U00002665"
    elif suit(c) == 2:
        return "\U00002664"
    elif suit(c) == 3:
        return "\U00002666"
    else:
        return "\U00002667"


"""Start of Actual Game"""

while True:
    if input("Please press enter to start") == '':
        break

"""Betting"""


def betting(a, b, c, d, e):
    t = 0
    while True:

        if t == 0:
            p1b = input("Player 1, enter a number to bet or 'q' to quit")

            if p1b == 'q':
                print("Player 1 quits, Player 2 wins this hand")
                break

            try:
                int(p1b) == 0
            except ValueError:
                print("Please read the instructions")
                continue

            if int(p1b) in range(0, a + 1):
                if int(p1b) >= 50 or c >= 50:
                    if int(p1b) + c < d:
                        print("Please bet as much as or more than Player 2")
                    else:
                        c += int(p1b)
                        a -= int(p1b)
                        t += 1
                        print("Player 1's bet amounts to " + str(c))
                else:
                    print("Please bet at least 50")
                    continue
            elif int(p1b) not in range(0, a + 1):
                print("Please enter an amount within your fund limit")
                continue

        if t == 1:

            p2b = input("Player 2, enter a number to bet or 'q' to quit")

            if p2b == 'q':
                print("Player 2 quits, Player 1 wins this hand")
                break

            try:
                int(p2b) == 0
            except ValueError:
                print("Please read the instructions")
                continue

            if int(p2b) in range(0, b + 1):
                if int(p2b) >= 50 or d >= 50:
                    if int(p2b) + d < c:
                        print("Please enter as much as or more than Player 1")
                    else:
                        d += int(p2b)
                        b -= int(p2b)
                        t -= 1
                        print("Player 2's bet amounts to " + str(d))
                else:
                    print("Please bet at least 50")
                    continue
            elif int(p2b) not in range(0, b + 1):
                print("Please enter an amount within your fund limit")
                continue
        if c == d:
            break
        else:
            continue

    e += c + d

    print("The pot is " + str(e))


betting(a, b, c, d, e)

# TURN 1
# your turn

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
    shown_cards1 += shown_card(player1Cards[i]) + shown_suit(player1Cards[i]) + ' '
shown_cards1 += shown_card(player1Cards[4]) + shown_suit(player1Cards[4])

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

betting(a, b, c, d, e)

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

betting(a, b, c, d, e)

"""Determining the Winner"""

# straight flush


def straight_flush():
    if value(card1) == value(card2) - 1 == value(card3) - 2 == value(card4) - 3 == value(card5) - 4 or value(card1)\
            == value(card2) - 1 == value(card3) - 2 == value(card4) - 3 == value(card5) + 9:
        if flush() == card1 and value(card1) not in (11, 12, 13):
            return True
        else:
            return False
    else:
        return False

# straight


def straight():
    if value(card1) == value(card2) - 1 == value(card3) - 2 == value(card4) - 3 == value(card5) - 4 or value(card1)\
            == value(card2) - 1 == value(card3) - 2 == value(card4) - 3 == value(card5) + 9:
        if not flush() and value(card1) not in (11, 12, 13):
            return True
        else:
            return False
    else:
        return False

# flush


def flush():
    if suit(card1) == suit(card2) == suit(card3) == suit(card4) == suit(card5):
        return True
    else:
        return False

# 4 of a kind


def four_of_a_kind():
    if value(card1) == value(card2) == value(card3) == value(card4) or value(card2) == value(card3)\
            == value(card4) == value(card5):
        return True
    else:
        return False

# full house


def full_house():
    if value(card1) == value(card2) == value(card3) and value(card4) == value(card5):
        return True
    elif value(card1) == value(card2) and value(card3) == value(card4) == value(card5):
        return True
    else:
        return False

# 3 of a kind


def three_of_a_kind():
    if not four_of_a_kind():
        if value(card1) == value(card2) == value(card3) or value(card2) == value(card3) == value(card4)\
                or value(card3) == value(card4) == value(card5):
            return True
        else:
            return False
    else:
        return False

# 2 pairs


def two_pairs():
    if not four_of_a_kind() and not three_of_a_kind():
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
def pair():
    if four_of_a_kind() is True or three_of_a_kind() is True or two_pairs() is True:
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

if straight_flush():
    player1score = 9
elif four_of_a_kind():
    player1score = 8
elif full_house():
    player1score = 7
elif flush():
    player1score = 6
elif straight():
    player1score = 5
elif three_of_a_kind():
    player1score = 4
elif two_pairs():
    player1score = 3
elif pair():
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

if straight_flush():
    player2score = 9
elif four_of_a_kind():
    player2score = 8
elif full_house():
    player2score = 7
elif flush():
    player2score = 6
elif straight():
    player2score = 5
elif three_of_a_kind():
    player2score = 4
elif two_pairs():
    player2score = 3
elif pair():
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
        print("It's a ducking draw. A draw. How in the the name of GCCS did you manage that?")
