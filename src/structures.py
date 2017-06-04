from math import *


class Przedzial:
    def __init__(self, X):
        self.left = X[0]
        self.right = X[1]

def przeliczSen(start, koniec, ileNieMoglemZasnac): #zalozenie: sen glowny nie zaczyna sie przed 22, drzemka jest po polnocy
    if(start > koniec):
        return [start-22 + round(float(ileNieMoglemZasnac)/60, 2), koniec + 24 -22]
    else:
        return [start + 24 - 22 + round(float(ileNieMoglemZasnac)/60, 2), koniec + 24 - 22]






class Sen:
    def __init__(self, przedzialySnu, ileNieMoglemZasnac, jakBardzoChcialemOpóźnićPójścieSpać, godzinaZgaszeniaEkranu, godzinaOstatniegoPosilku):
        self.senGlowny = przeliczSen(przedzialySnu[0], przedzialySnu[1], ileNieMoglemZasnac)
        self.ileNieMoglemZasnac = round(float(ileNieMoglemZasnac)/60, 2)
        self.jakBardzoChcialemOpóźnićPójścieSpać = jakBardzoChcialemOpóźnićPójścieSpać
        self.godzinaZgaszeniaEkranu = godzinaZgaszeniaEkranu
        self.godzinaOstatniegoPosilku = godzinaOstatniegoPosilku


class PieniadzeSlodyczeSmiecioweJedzenie:
    def __init__(self, lacznaWydanaKwota, lacznaIloscCukru, lacznaMasaJedzenia, lacznaIloscNapojow):
        self.lacznaWydanaKwota = lacznaWydanaKwota
        self.lacznaIloscCukru = lacznaIloscCukru
        self.lacznaMasaJedzenia = lacznaMasaJedzenia
        self.lacznaIloscNapojow = lacznaIloscNapojow


class Rozrywka:
    def __init__(self, lacznyCzasGrania, lacznyCzasFilmikowStron, lacznyCzasDark):
        self.lacznyCzasGrania = lacznyCzasGrania
        self.lacznyCzasFilmikowStron = lacznyCzasFilmikowStron
        self.lacznyCzasDark = lacznyCzasDark


class NaukaPracaModlitwa:
    def __init__(self, naukaNaStudia, srednieZaangazowanieStudia, naukaDodatkowa, srednieZaangazowanieDodatkowa, czytanieKsiazek, srednieZaangazowanieCzytanie, wartoscPozostalychZajec, modlitwa):
        self.lacznyCzasNaukiNaStudia = naukaNaStudia
        self.lacznyCzasNaukiDodatkowej = naukaDodatkowa
        self.czytanieKsiazek = czytanieKsiazek
        self.srednieZaangazowanieStudia = srednieZaangazowanieStudia
        self.srednieZaangazowanieDodatkowa = srednieZaangazowanieDodatkowa
        self.srednieZaangazowanieCzytanie = srednieZaangazowanieCzytanie
        self.wartoscPozostalychZajec = wartoscPozostalychZajec
        self.modlitwaRano = modlitwa[0]
        self.modlitwaWieczorem = modlitwa[1]


class OpisSytuacji:
    def __init__(self, opisySytuacjiPejoratywnych, opisySytuacjiGlioriatywnych):
        self.opisySytuacjiPejoratywnych = opisySytuacjiPejoratywnych
        self.opisySytuacjiGlioriatywnych = opisySytuacjiGlioriatywnych

