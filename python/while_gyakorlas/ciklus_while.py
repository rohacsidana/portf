import math
def f1():
    i = 0
    while i <= 150:
        print(i)
        i += 2
# Addig kérjünk be szám(ok)at, amíg 10-zel osztható nem lesz!


def fl3():
    i = 1
    while i % 10 != 0:
        i = int(input("kérek egy számot: "))
    print("köszönöm")
# Addig kérjünk be számokat, amíg pozitív páratlan számot nem kapunk.


def fl5():
    i = int(input("kérek egy számot: "))
    while not ((i % 2 != 0) and (i > 0)):
        i = int(input("!kérek egy másik számot: "))
    print("köszönöm")

#Addig kérjünk be számokat, amíg 3-mal osztható vagy négyzetszám nem lesz.
def fl6():
    i = float(input("kérek egy számot: "))
    while not(i % 3 == 0 or math.sqrt(i) % 1 == 0):
        i = float(input("kérek egy másik számot: "))
    print("köszy")
#Kérj be 3 számot, amíg szerkeszthető háromszög oldalait nem kapjuk (valós szám is lehet)!
def fl7():
    #a + c > b, b + a > c, c + b > a
    a = int(input("kérem a háromszog 'a' oldalát: "))
    b = int(input("kérem a háromszog 'b' oldalát: "))
    c = int(input("kérem a háromszog 'c' oldalát: "))
    while not(a + c > b and b + a > c and c + a > b):
        a = int(input("újra kérem a háromszog 'a' oldalát: "))
        b = int(input("újra kérem a háromszog 'b' oldalát: "))
        c = int(input("újra kérem a háromszog 'c' oldalát: "))

#Addig kérjünk be szöveget, amíg legalább 3 karakterest nem írnak be. Majd írjuk ki a szót csupa nagy betűvel!
def fl8():
    szo = input("kérek egy 3 karakteres szót: ")
    while not(len(szo) == 3):
        szo = input("újra kérek egy 3 karakteres szót: ")
    print("A szó nagybetűsen:", szo.upper())
#Addig kérjünk be szöveget, amíg csupa kis betűs és 4 karakteres szót nem adnak meg!

def fl9():
    szo = input("kérek egy 4 karakteres, kisbetűs szót: ")
    while not(len(szo) == 4 and szo.islower()):
        szo = input("újra kérek egy 4 karakteres, kiisbetűs szót: ")
    print("köszii")
