import xlrd, xlwt
from xlutils.copy import copy
import math
from src import parser
from src import structures
from src import generacjaObiektow
from jinja2 import Environment, PackageLoader
import webbrowser


szerokosc_ekranu = math.floor(1366*0.9) #na 768


parser.przeniesDaneZNewDaydoAllDayData()
wczytywanyArkusz = parser.zwrocSheet("everydaysData/AllDayData.xls")
ilosc_dni = parser.iloscDniAllDayData(wczytywanyArkusz)
szerokosc_slupka = math.floor(szerokosc_ekranu/ilosc_dni)

obiektySnu = generacjaObiektow.wygenerujObiektyOpisuSnu(parser.wczytajDaneDlaSnu(wczytywanyArkusz))
obiektyZakupuSlodyczy = generacjaObiektow.wygenerujObiektyOpisuKupnaSlodyczy(parser.wczytajDaneDlaSlodyczyNapojow(wczytywanyArkusz))
obiektyRozrywki = generacjaObiektow.wygenerujObiektyOpisuRozrywki(parser.wczytajRozrywke(wczytywanyArkusz))
obiektyNaukiPracyZaangazowania = generacjaObiektow.wygenerujObiektyOpisuPracyNauki(parser.wczytajNaukaPracaModlitwa(wczytywanyArkusz))
obiektyOpisuSytuacjiOdczuc = generacjaObiektow.wygenerujObiektyOpisuSytuacjiOdczuc(parser.wczytajOpisySytuacji(wczytywanyArkusz))

len(obiektySnu)
env = Environment(loader=PackageLoader('yourapplication'))

template = env.get_template('slodyczeTemplate.html')
output_from_parsed_template = template.render(szerokoscEkranu=szerokosc_ekranu,
                                              szerokoscSlupka=szerokosc_slupka,
                                              iloscDni=ilosc_dni,
                                              obiektyZakupuSlodyczy=obiektyZakupuSlodyczy,
                                              iloscObiektyZakupuSlodyczy=len(obiektyZakupuSlodyczy))

with open("wynikSlodycze.html", "w") as fh:
    fh.write(output_from_parsed_template)


template = env.get_template('rozrywkaTemplate.html')
output_from_parsed_template = template.render(szerokoscEkranu=szerokosc_ekranu,
                                              szerokoscSlupka=szerokosc_slupka,
                                              iloscDni=ilosc_dni,
                                              obiektyRozrywki=obiektyRozrywki,
                                              iloscObiektowRozrywki=len(obiektyRozrywki))

with open("wynikRozrywka.html", "w") as fh:
    fh.write(output_from_parsed_template)

template = env.get_template('naukaPracaModlitwaTemplate.html')
output_from_parsed_template = template.render(szerokoscEkranu=szerokosc_ekranu,
                                              szerokoscSlupka=szerokosc_slupka,
                                              iloscDni=ilosc_dni,
                                              obiektyNaukiPracyZaangazowania=obiektyNaukiPracyZaangazowania,
                                              iloscObiektowNauki=len(obiektyNaukiPracyZaangazowania),
                                                wysokoscDiagram=30)

with open("wynikNaukaPracaModlitwa.html", "w") as fh:
    fh.write(output_from_parsed_template)


template = env.get_template('senTemplate.html')
output_from_parsed_template = template.render(szerokoscEkranu=szerokosc_ekranu,
                                              szerokoscSlupka=szerokosc_slupka,
                                              iloscDni=ilosc_dni,
                                              obiektySnu=obiektySnu,
                                              iloscObiektowSnu=len(obiektySnu),
                                              wysokoscDiagram=15,
                                              stalaWyrownaniaSlupkowSnu=-73)

with open("wynikSen.html", "w") as fh:
    fh.write(output_from_parsed_template)


#uruchamiamy wykresy
"""
webbrowser.get('firefox').open_new_tab('wynikNaukaPracaModlitwa.html')
webbrowser.get('firefox').open_new_tab('wynikSen.html')
webbrowser.get('firefox').open_new_tab('wynikRozrywka.html')
webbrowser.get('firefox').open_new_tab('wynikSlodycze.html')
"""