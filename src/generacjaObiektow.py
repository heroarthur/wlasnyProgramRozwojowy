import xlrd, xlwt
from xlutils.copy import copy
import math
from src import parser
from src import structures


def wygenerujObiektyOpisuSnu(dane):
    obiekty = []
    for opis in dane:
        obiekt = structures.Sen(opis[0], opis[1], opis[2], opis[3], opis[4])
        #wypiszObiekty(opis)
        obiekty.append(obiekt)
    return obiekty


def wygenerujObiektyOpisuKupnaSlodyczy(dane):
    obiekty = []
    for opis in dane:
        obiekt = structures.PieniadzeSlodyczeSmiecioweJedzenie(opis[0], opis[1], opis[2], opis[3])
        #wypiszObiekty(opis)
        obiekty.append(obiekt)
    return obiekty


def wygenerujObiektyOpisuRozrywki(dane):
    obiekty = []
    for opis in dane:
        obiekt = structures.Rozrywka(opis[0], opis[1], opis[2])
        #wypiszObiekty(opis)
        obiekty.append(obiekt)
    return obiekty


def wygenerujObiektyOpisuPracyNauki(dane):
    obiekty = []
    for opis in dane:
        #wypiszObiekty(opis)
        obiekt = structures.NaukaPracaModlitwa(opis[0], opis[1], opis[2], opis[3], opis[4], opis[5], opis[6], opis[7])
        obiekty.append(obiekt)
    return obiekty


def wygenerujObiektyOpisuSytuacjiOdczuc(dane):
    obiekty = []
    for opis in dane:
        obiekt = structures.OpisSytuacji(opis[0], opis[1])
        #wypiszObiekty(opis)
        obiekty.append(obiekt)
    return obiekty

def wypiszObiekty(elementy):
    wynik = ""
    for e in elementy:
        wynik = wynik + str(e) + " | "
    #print(wynik)