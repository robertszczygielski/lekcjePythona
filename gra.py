import random

gracz1 = "x"
gracz2 = "o"
plansza = []
plansza.append(["i", "i", "i"])
plansza.append(["i", "i", "i"])
plansza.append(["i", "i", "i"])


def przypisanie_pola_do_gracza(x, y, gracz):
    plansza[x][y] = gracz


def narysowanie_planszy_na_ekranie():
    for index in plansza:
        print index
    print ""


def zmiana_aktywnego_gracza(aktywny_gracz):
    if aktywny_gracz == gracz1:
        return gracz2
    else:
        return gracz1


def losowanie_pola():
    while True:
        a = random.randint(0, 2)
        b = random.randint(0, 2)
        if plansza[b][a] == "i":
            return [b, a]


def zakonczenie_gry():
    gracz = gracz1
    for x in range(0, 9):
        narysowanie_planszy_na_ekranie()
        [indexa, indexb] = losowanie_pola()
        przypisanie_pola_do_gracza(indexa, indexb, gracz)
        gracz = zmiana_aktywnego_gracza(gracz)
    narysowanie_planszy_na_ekranie()


zakonczenie_gry()
