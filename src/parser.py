import xlrd, xlwt
from xlutils.copy import copy
import math

ilosc_parametrow_jednego_dnia = 30
pierwsza_kolumna_danych = 1
waga_litra = 1000 #1000g
ilosc_minut_w_godzinie = 60



class wierszeZnaczenie:
    senGlowny = 0
    ileNieMoglemZasnac = 1
    opoznieniePojsciaSpac = 2
    wylaczenieMonitora = 3
    ostatniPosilek = 4
    kosztSlodyczy = 8
    ileCukruMasyWJedzeniu = 9
    pojemnoscNapojowSlodzonych = 10
    czasNaGraniu = 11
    czasNaOgladaniu = 12
    czasDark = 13
    naukaNaStudiaZaangazowanie = 14
    naukaDodatkowaZaangazowanie = 15
    czytanieZaangazowanie = 16
    sumaPozostalychWaznychZajec = 17
    modlitwa = 18
    opisPodczucPejoratywnych = 19
    opisOdczucGloriatywnych = 20



def iloscDniAllDayData(sheet):
    return sheet.cell(0, 0).value


def wczytajWiersz(wiersz, poczatekWczytywania,sheet):
    wczytanyWiersz = []
    for i in range(poczatekWczytywania, sheet.row_len(wiersz)):
        if(sheet.cell(wiersz, i).value == ""):
            return wczytanyWiersz
        wczytanyWiersz.append(sheet.cell(wiersz, i).value)
    return wczytanyWiersz

def wczytajJednaWartoscWiersza(wiersz, kolumna, sheet):
    return sheet.cell(wiersz, kolumna).value


def sumaElementowProcentowych(elementy):
    suma = 0.0
    masaElementu = 0.0
    for i in range(0,len(elementy)):
        if(i % 2 == 0):
            masaElementu = elementy[i]
        else:
            procent = elementy[i]
            suma = suma + ((float(masaElementu)*float(procent))/100.0)
    return round(suma, 2)


def sumaElementow(elementy):
    suma = 0
    for i in range(0, len(elementy)):
        suma = suma + float(elementy[i])
    return suma

def sumaPierwszegoICoDrugiegoElementu(elementy):
    suma = 0
    for i in range(0, len(elementy), 2):
        suma += float(elementy[i])
    return suma

def parujElementy(elementy):
    pary = []
    for i in range(0, len(elementy), 2):
        pary.append((elementy[i], elementy[i+1]))
    return pary



def sredniaWazona(tablicaParCzasZaangazowanie):
    mianownik = sumaPierwszegoICoDrugiegoElementu(tablicaParCzasZaangazowanie)
    licznik = 0.0
    for i in range(0, len(tablicaParCzasZaangazowanie), 2):
        licznik += float(tablicaParCzasZaangazowanie[i])*float(tablicaParCzasZaangazowanie[i+1])
    wynik = licznik / mianownik
    return round(wynik, 2)


def wczytajDaneDlaSnu(sheet):
    iloscDni = iloscDniAllDayData(sheet)
    dane = []
    for i in range(0, math.floor(iloscDni)):
        wiersz = math.floor(1 + i*ilosc_parametrow_jednego_dnia)
        przedzialySnu = wczytajWiersz(wiersz + wierszeZnaczenie.senGlowny, 0, sheet)
        ileNieMoglemZasnac = wczytajJednaWartoscWiersza(wiersz + wierszeZnaczenie.ileNieMoglemZasnac, 0, sheet)
        jakBardzoChcialemOpoznicSen = wczytajJednaWartoscWiersza(wiersz + wierszeZnaczenie.opoznieniePojsciaSpac, 0, sheet)
        godzinaZgaszeniaMonitora = wczytajJednaWartoscWiersza(wiersz + wierszeZnaczenie.wylaczenieMonitora, 0, sheet)
        godzinaOstatniegoPosilku = wczytajJednaWartoscWiersza(wiersz + wierszeZnaczenie.ostatniPosilek, 0, sheet)
        dane.append((przedzialySnu, ileNieMoglemZasnac, jakBardzoChcialemOpoznicSen, godzinaZgaszeniaMonitora, godzinaOstatniegoPosilku))
    return dane



def wczytajDaneDlaSlodyczyNapojow(sheet):
    iloscDni = iloscDniAllDayData(sheet)
    dane = []
    for i in range(0, math.floor(iloscDni)):
        wiersz = 1 + i*ilosc_parametrow_jednego_dnia
        wydanaKwotaNaSlodycze = sumaElementow(wczytajWiersz(wiersz + wierszeZnaczenie.kosztSlodyczy, 0, sheet))
        masaJedzeniaSmieciowego = sumaPierwszegoICoDrugiegoElementu(wczytajWiersz(wiersz + wierszeZnaczenie.ileCukruMasyWJedzeniu, 0, sheet))
        pojemnoscNapojowSlodzonych = sumaPierwszegoICoDrugiegoElementu(wczytajWiersz(wiersz + wierszeZnaczenie.pojemnoscNapojowSlodzonych, 0, sheet))
        iloscCukruWJedzeniu = sumaElementowProcentowych(wczytajWiersz(wiersz + wierszeZnaczenie.ileCukruMasyWJedzeniu, 0, sheet))
        iloscCukruWPiciu = waga_litra*sumaElementowProcentowych(wczytajWiersz(wiersz + wierszeZnaczenie.pojemnoscNapojowSlodzonych, 0, sheet))
        dane.append((round(wydanaKwotaNaSlodycze, 2), iloscCukruWJedzeniu+iloscCukruWPiciu, masaJedzeniaSmieciowego, pojemnoscNapojowSlodzonych))
    return dane



def wczytajRozrywke(sheet):
    iloscDni = iloscDniAllDayData(sheet)
    dane = []
    for i in range(0, math.floor(iloscDni)):
        wiersz = 1 + i*ilosc_parametrow_jednego_dnia
        lacznyCzasGry = float(wczytajJednaWartoscWiersza(wiersz + wierszeZnaczenie.czasNaGraniu, 0, sheet))*ilosc_minut_w_godzinie
        lacznyCzasOgladania = float(wczytajJednaWartoscWiersza(wiersz + wierszeZnaczenie.czasNaOgladaniu, 0, sheet))*ilosc_minut_w_godzinie
        lacznyCzasDark = float(wczytajJednaWartoscWiersza(wiersz + wierszeZnaczenie.czasDark, 0, sheet))*ilosc_minut_w_godzinie
        dane.append((lacznyCzasGry, lacznyCzasOgladania, lacznyCzasDark))
    return dane


def wczytajNaukaPracaModlitwa(sheet):
    iloscDni = iloscDniAllDayData(sheet)
    dane = []
    for i in range(0, math.floor(iloscDni)):
        wiersz = 1 + i * ilosc_parametrow_jednego_dnia
        naukaNaStudia = sumaPierwszegoICoDrugiegoElementu(wczytajWiersz(wiersz + wierszeZnaczenie.naukaNaStudiaZaangazowanie, 0, sheet))
        zaangazowanieNaukiNaStudia = sredniaWazona(wczytajWiersz(wiersz + wierszeZnaczenie.naukaNaStudiaZaangazowanie, 0, sheet))
        naukaDodatkowa = sumaPierwszegoICoDrugiegoElementu(wczytajWiersz(wiersz + wierszeZnaczenie.naukaDodatkowaZaangazowanie, 0, sheet))
        zaangazowanieNaukiDodatkowej = sredniaWazona(wczytajWiersz(wiersz + wierszeZnaczenie.naukaDodatkowaZaangazowanie, 0, sheet))
        czytanie = sumaPierwszegoICoDrugiegoElementu(wczytajWiersz(wiersz + wierszeZnaczenie.czytanieZaangazowanie, 0, sheet))
        zaangazowanieCzytanie = sredniaWazona(wczytajWiersz(wiersz + wierszeZnaczenie.czytanieZaangazowanie, 0, sheet))
        modlitwaRano = wczytajJednaWartoscWiersza(wiersz + wierszeZnaczenie.modlitwa, 0, sheet)
        modlitwaWieczorem = wczytajJednaWartoscWiersza(wiersz + wierszeZnaczenie.modlitwa, 1, sheet)
        sumaPozostalychZajec = wczytajJednaWartoscWiersza(wiersz + wierszeZnaczenie.sumaPozostalychWaznychZajec, 0, sheet)
        dane.append((naukaNaStudia, zaangazowanieNaukiNaStudia, naukaDodatkowa, zaangazowanieNaukiDodatkowej, czytanie, \
                zaangazowanieCzytanie, sumaPozostalychZajec, (modlitwaRano, modlitwaWieczorem)))
    return dane




def wczytajOpisySytuacji(sheet):
    iloscDni = iloscDniAllDayData(sheet)
    dane = []
    for i in range(0, math.floor(iloscDni)):
        wiersz = 1 + i*ilosc_parametrow_jednego_dnia
        opisSytuacjiPejoratywnych = parujElementy(wczytajWiersz(wiersz + wierszeZnaczenie.opisPodczucPejoratywnych, 0, sheet))
        opisSytuacjiGloriatywnych = parujElementy(wczytajWiersz(wiersz + wierszeZnaczenie.opisOdczucGloriatywnych, 0, sheet))
        dane.append((opisSytuacjiPejoratywnych, opisSytuacjiGloriatywnych))
    return dane



def przeniesDaneZNewDaydoAllDayData():
    bookAllDayData = xlrd.open_workbook("everydaysData/AllDayData.xls")
    sheetAllDayData = bookAllDayData.sheet_by_index(0)
    bookNewDay = xlrd.open_workbook("everydaysData/newDay.xls")
    sheetNewDay = bookNewDay.sheet_by_index(0)
    iloscDni = iloscDniAllDayData(sheetAllDayData)
    rb = xlrd.open_workbook("everydaysData/AllDayData.xls", formatting_info=True)
    r_sheet = rb.sheet_by_index(0)  # read only copy to introspect the file
    wb = copy(rb)  # a writable copy (I can't read values out of this, only write to it)
    wb.save("everydaysData/AllDayDataDayBefore.xls")

    w_sheet = wb.get_sheet(0)  # the sheet to write to within the writable copy
    miejsceNaNoweDane = 1 + ilosc_parametrow_jednego_dnia*iloscDni

    w_sheet.write(0,0,math.floor(iloscDni+1))
    for i in range(0,ilosc_parametrow_jednego_dnia):
        for j in range(pierwsza_kolumna_danych, sheetNewDay.row_len(i)):
            w_sheet.write(math.floor(i+miejsceNaNoweDane), j-1, sheetNewDay.cell(i, j).value)
    wb.save("everydaysData/AllDayData.xls")


def zwrocSheet(path):
    book = xlrd.open_workbook(path)
    sheet = book.sheet_by_index(0)
    return sheet