import blackjack2
import random


my_hand = []
pc_hand = []
my_score = 0
pc_score = 0


def kiiras():
    print(f"\033[94mAz én lapjaim: {my_hand}")
    print(f"\033[94mAz én pontjaim: {my_score}")
    print(f"\033[93mA gép lapjai: {pc_hand}")
    print(f"\033[93mA gép pontjai: {pc_score}")


blackjack2.first2(2, my_hand)
blackjack2.first2(2, pc_hand)
my_points = blackjack2.score(my_score, my_hand)
pc_points = blackjack2.score(pc_score, pc_hand)
my_score += my_points
pc_score += pc_points

while not(my_score > 20 or pc_score > 20):
    kiiras()
    play_or_not = input('\x1b[0;30;45m' + "Szeretnél lapot kérni?(y/n) " + '\x1b[0m').upper()
    if play_or_not == "Y":
        blackjack2.first2(1, my_hand)
        my_score += blackjack2.score_after_start(my_score, my_hand)
    elif play_or_not == "N":
        rnd = random.randint(1, 2)
        if rnd == 1:
            blackjack2.first2(1, pc_hand)
            pc_score += blackjack2.score_after_start(pc_score, pc_hand)


kiiras()
if my_score == 21:
    print("\033[94mBLACKJACK-ed van")
if pc_score == 21:
    print("\033[93mA gépnek BLACKJACK-je van.")
elif my_score > 21:
    print("\033[94mVesztettél.")
elif pc_score > 21:
    print("\033[93mA gép vesztett.")
