from math import pi

def is_even(x):
    result = x % 2
    if result == 0:
        return True
    else:
        return False


def is_oneven(x):
    result = is_even(x)
    if result == False:
        return True
    else:
        return False


def volume_bol(r):
    result = 4/3 * pi * r **3
    return result


def oppervlakte_cirkel(r):
    result = r**2 * pi 
    # Deze functie kan je gebruiken om het volume van de donut te berekenen.
    return result


def omtrek_cirkel(r):
    result = 2 * r * pi
    # Deze functie kan je gebruiken om het volume van de donut te berekenen.
    return result


def volume_donut(r, R):
    if r <= 0:
        return -1
    if R <= 0:
        return -1
    if r == R:
        return -1 
    result = 2 * pi**2 * r**2 * R
    return result


def stats(punten):
    gemiddelde = sum(punten) / len(punten)
    maximum = max(punten)
    minimum = min(punten)
    nr = len(punten) 
    return gemiddelde, maximum, minimum, nr


class Cirkel:
    def __init__(self, r):
        self.straal = r

    def omtrek(self):
        omtrek = self.straal * 2 * pi
        return omtrek

    def oppervlakte(self):
        oppervlakte = self.straal **2 * pi
        return oppervlakte

    def __str__(self):
        x = Cirkel(r)
        return f"Een cirkel met straal {self.straal}"


def pythagoras(a, b):
    """Return de lengte van de schuine zijde als de lengtes
    van de rechthoekszijden gegeven zijn door a en b"""
    return 0


def is_palindroom(woord):
    """Return True als het omgekeerde van het woord gelijk
    is aan het woord zelf. Return anders False."""
    return True
