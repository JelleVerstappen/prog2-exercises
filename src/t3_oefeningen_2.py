from math import pi

def is_even(x):
    result = x % 2
    if result == 0:
        return True
    else:
        return False


def is_oneven(x):
    resultaat = is_even(x)
    if resultaat == False:
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
    return 0


def volume_donut(r, R):
    """Return volume donut met straal r en R
    waarbij r de dikte van de donut is, en R
    de grootte van de donut.
    """
    return 0


def stats(punten):
    """Return het gemiddelde, het maximum, het minimum en het aantal getallen
    als een lijst met punten gegeven werd."""
    return 0


class Cirkel:
    def __init__(self, r):
        self.straal = r

    def omtrek(self):
        """Return de omtrek van de cirkel met straal r"""
        return 0

    def oppervlakte(self):
        """Return de oppervlakte van de cirkel met straal r"""
        return 0

    def __str__(self):
        """Return een string zoals aangegeven in de testen"""
        return ""


def pythagoras(a, b):
    """Return de lengte van de schuine zijde als de lengtes
    van de rechthoekszijden gegeven zijn door a en b"""
    return 0


def is_palindroom(woord):
    """Return True als het omgekeerde van het woord gelijk
    is aan het woord zelf. Return anders False."""
    return True
