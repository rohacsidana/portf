import math
print("Üdvözlöm, bemutatom a BMI kalkulátorunkat. A BMI, avagy a Body Mass Index mutatja a testsúly és a magasság arányát. A BMI kiszámolása alapján megtudhatja, hogy ideális-e az aktuális testsúlya vagy jobb lenne változtatni rajta. Csak meg kell adnia néhány adatot, és besorolom az 5 súlykategória egyikébe. Amennyiben a BMI szerint pl. soványság vagy túlsúly jön ki, mindenképpen jó, ha megbeszéli a háziorvosoddal. Ő majd elmagyarázza, hogyan tud helyesen változtatni a testsúlyán.")
nem = input("Kérem a nemét (F = férfi, N = nő): ")
kor = int(input("Kérem az életkorát: "))
kg = int(input("Kérem a testtömegét kg-ban kifejezve: "))
cm = int(input("Kérem a tesmagasságát cm-ben kifejezve: "))
m = float(cm / 100)
bmi = kg / (m**2)
sovanyno = "Ön egy sovány testalkatú nő. BMI kalkulátor szerint a testsúlya a magasságához képest nagyon alacsony. A szervezetéből fontos tápanyagok hiányozhatnak."
sovanyffi = "Ön egy sovány testalkatú férfi. BMI kalkulátor szerint a testsúlya a magasságához képest nagyon alacsony. A szervezetéből fontos tápanyagok hiányozhatnak."
normalno = "Ön egy ideális testsúlyú nő. Nagyszerű! A BMI kalkulátor szerint ideális a testsúlya a magasságához képest. Valószínűleg ez nem is fog változni, ha (továbbra is) egészségesen étkezik és tornázik. Gratulálunk!"
normalffi = "Ön egy ideális testsúlyú férfi. Nagyszerű! A BMI kalkulátor szerint ideális a testsúlya a magasságához képest. Valószínűleg ez nem is fog változni, ha (továbbra is) egészségesen étkezik és tornázik. Gratulálunk!"
tulsuly1no = "Ön egy túlsúlyos alkatú nő. A testsúlya magasabb a kelleténél. Kezdjen el többet mozogni, étkezzen egészségesebben és pár héten belül formába lendül. Az ideális súlya karnyújtásnyira van!"
tulsuly1ffi = "Ön egy túlsúlyos alkatú férfi. A testsúlya magasabb a kelleténél. Kezdjen el többet mozogni, étkezzen egészségesebben és pár héten belül formába lendül. Az ideális súlya karnyújtásnyira van!"
tulsuly2no = "Ön egy elhízott testalkatú nő. A BMI kalkulátor a testsúlya alapján az elhízás kategóriába sorolta. A kilogrammok csökkentése érdekében keresse fel a háziorvosát."
tulsuly2ffi = "Ön egy elhízott testalkatú férfi. A BMI kalkulátor a testsúlya alapján az elhízás kategóriába sorolta. A kilogrammok csökkentése érdekében keresse fel a háziorvosát."
tulsuly3no = "Ön egy súlyosan elhízott testalkatú nő. A BMI kalkulátor szerint súlyos elhízástól szenved. Ez egy táplálkozási és anyagcsere-betegség, amely kezeléséhez mindenképpen orvosi segítségre van szüksége."
tulsuly3ffi = "Ön egy súlyosan elhízott testalkatú férfi. A BMI kalkulátor szerint súlyos elhízástól szenved. Ez egy táplálkozási és anyagcsere-betegség, amely kezeléséhez mindenképpen orvosi segítségre van szüksége."
hasovany = bmi < 20
haideal = (18 <= kor <= 24 and 20 <= bmi < 24) or (25 <= kor <= 34 and 20 <= bmi < 25) or (35 <= kor <= 44 and 20 <= bmi < 26) or (45 <= kor <= 54 and 20 <= bmi < 27 ) or (55 <= kor <= 64 and 20 <= bmi < 28) or (kor >= 65 and 20 <= bmi < 29)
hatulsuly1 = (18 <= kor <= 24 and 24 <= bmi < 30) or (25 <= kor <= 34 and 25 <= bmi < 31) or (35 <= kor <= 44 and 26 <= bmi < 32) or (45 <= kor <= 54 and 27 <= bmi < 33) or (55 <= kor <= 64 and 28 <= bmi < 34) or (kor >= 65 and 29 <= bmi < 35)
hatulsuly2 = (18 <= kor <= 24 and 30 <= bmi < 40) or (25 <= kor <= 34 and 31 <= bmi < 41) or (35 <= kor <= 44 and 32 <= bmi < 42) or (45 <= kor <= 54 and 33 <= bmi < 43) or (55 <= kor <= 64 and 34 <= bmi < 44) or (kor >= 65 and 35 <= bmi < 45)
hatulsuly3 = (18 <= kor <= 24 and 39 < bmi) or (25 <= kor <= 34 and 40 < bmi) or (35 <= kor <= 44 and 41 < bmi) or (45 <= kor <= 54 and 42 < bmi) or (55 <= kor <= 64 and 43 < bmi) or (kor >= 65 and 44 < bmi)
if hasovany:
    print("Az ön BMI-je:", round(bmi, 1))
    if nem == "N":
        print("\033[1m" + sovanyno + "\033[0m")
    else:
        print(sovanyffi)
if haideal:
    print("Az ön BMI-je:", round(bmi, 1))
    if nem == "N":
        print("\033[1m" + normalno + "\033[0m")
    else:
        print("\033[1m" + normalffi + "\033[0m")
if hatulsuly1:
    print("Az ön BMI-je:", round(bmi, 1))
    if nem == "N":
        print("\033[1m" + tulsuly1no + "\033[0m")
    else:
        print("\033[1m" + tulsuly1ffi + "\033[0m")
if hatulsuly2:
    print("Az ön BMI-je:", round(bmi, 1))
    if nem == "N":
        print("\033[1m" + tulsuly2no + "\033[0m")
    else:
        print("\033[1m" + tulsuly2ffi + "\033[0m")
if hatulsuly3:
    print("Az ön BMI-je:", round(bmi, 1))
    if nem == "N":
        print("\033[1m" + tulsuly3no + "\033[0m")
    else:
        print("\033[1m" + tulsuly3ffi + "\033[0m")
szamolo = 0
if hatulsuly1 or hatulsuly2 or hatulsuly3:    
    while not haideal:
        kg -= 1
        bmi = kg / (m**2)
        haideal = (18 <= kor <= 24 and 20 <= bmi < 24) or (25 <= kor <= 34 and 20 <= bmi < 25) or (35 <= kor <= 44 and 20 <= bmi < 26) or (45 <= kor <= 54 and 20 <= bmi < 27 ) or (55 <= kor <= 64 and 20 <= bmi < 28) or (kor >= 65 and 20 <= bmi < 29)
        szamolo += 1
    print(szamolo, "kilogrammot kell fogynia az ideális testúly eléréséhez.")
if hasovany:    
    while not haideal:
        kg += 1
        bmi = kg / (m**2)
        haideal = (18 <= kor <= 24 and 20 <= bmi < 24) or (25 <= kor <= 34 and 20 <= bmi < 25) or (35 <= kor <= 44 and 20 <= bmi < 26) or (45 <= kor <= 54 and 20 <= bmi < 27 ) or (55 <= kor <= 64 and 20 <= bmi < 28) or (kor >= 65 and 20 <= bmi < 29)
        szamolo += 1
    print(szamolo, "kilogrammot kell híznia az ideális testúly eléréséhez.")

    
