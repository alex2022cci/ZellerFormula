from typing import List

import main


class Date:
    # Liste des jours
    jours: list[str] = ["samedi", "dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi"]

    def __init__(self, day1, month1, year1):
        self.day1 = day1
        self.month1 = month1
        self.year1 = year1

    def get_day(self):
        return self.day1

    def get_month(self):
        return self.month1

    def get_year(self):
        return self.year1


day1 = int(input("jour= ?"))
month1 = int(input("mois= ?"))
year1 = int(input("année= ?"))

# Tester la date du jour
print("Date =", day1, month1, year1)

# Zeller Formula
# J et K sont les moitiés de l'année exemple 1789 J = 17 et K = 89
# d est le numéro du jour
# m est le numéro du mois sauf janvier et février qui sont 13 et 14

# h = d + int((13(m+1))/5) + K + int(K/4) + int(J/4) - 2J%7

# h est un résultat entre 0 et 6 => samedi = 0, dimanche = 1,  ... vendredi = 6


def get_zeller_day():
    q = main.day1
    print("q= ", q)
    return q


# get_zeller_day()


def get_zeller_month():
    m = 0
    if main.month1 >= 3:
        m = main.month1
    elif main.month1 == 1:
        m = 13
    elif main.month1 == 2:
        m = 14
    print("m= ", m)
    return m


# get_zeller_month()


def get_zeller_year():
    y = 0
    j = 0
    k = 0
    if main.get_zeller_month() > 12:
        y = main.year1 - 1
    else:
        y = main.year1
    print("year Zeller= ", y)
    k = y % 100
    j = y // 100
    print(" j = ", j, " et k = ", k)
    return y

# get_zeller_year()


def zeller_formula():
    q = main.get_zeller_day()
    m = main.get_zeller_month()
    k = main.get_zeller_year() % 100
    j = main.get_zeller_year() // 100
    # h = (q + int(13*(m+1)) + k + k//4 + 5*j + j//4 - 2*j) % 7

    h = (q + (13*(m+1))//5 + k + k//4 + 5*j + j//4) % 7

    print("q= ", q, "m=", m, "j=", j, "k=", k,  "h=", h)
    return h


# zeller_formula()

def annonce_jour():
    h = zeller_formula()
    print(
        Date.jours[h]
    )


annonce_jour()

