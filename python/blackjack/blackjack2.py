import random
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4


# first 2 cards
def first2(db, hand):
    for i in range(db):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:
            card = "J"
        if card == 12:
            card = "Q"
        if card == 13:
            card = "K"
        if card == 14:
            card = "A"
        hand.append(card)
        if card == "J":
            card = 11
        if card == "Q":
            card = 12
        if card == "K":
            card = 13
        if card == "A":
            card = 14


def score(score, hand):
    point = 0
    for i in range(len(hand)):
        if hand[i] == "J" or hand[i] == "Q" or hand[i] == "K":
            point += 10
        elif hand[i] == "A":
            if score <= 10:
                point += 11
            else:
                point += 1
        else:
            point += hand[i]
    return point


def score_after_start(score, hand):
    point = 0
    if hand[-1] == "J" or hand[-1] == "Q" or hand[-1] == "K":
        point += 10
    elif hand[-1] == "A":
        if score <= 10:
            point += 11
        else:
            point += 1
    else:
        point += hand[-1]
    return point
