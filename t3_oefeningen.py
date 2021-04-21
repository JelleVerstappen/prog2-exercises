from math import pi


def bmi(gewicht, lengte):
    if lengte <= 0:
        return -1
    if gewicht <=0:
        return -1
    if lengte == 0:
        return -1
    resultaat = gewicht / lengte **2
    return resultaat

def omtrek_cirkel(r):
    resultaat = 2 * r * pi
    return resultaat

def oppervlakte_cirkel(r):
    resultaat = (r **2) * pi
    return resultaat

def oppervlakte_vierkant(zijde):
    resultaat = zijde **2
    return resultaat

def volume_cilinder(r, h):
    resultaat = oppervlakte_cirkel(r) * h
    return resultaat

def volume_kubus(zijde):
    if zijde < 0:
        resultaat = 0
        return resultaat
    resultaat = zijde **3
    return resultaat

