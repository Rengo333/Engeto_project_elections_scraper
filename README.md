# Elections Scraper Projekt
---
Třetí projekt pro akademii engeto.
### Popis Projektu
---
Tento projekt slouží pro extrahování výsledků z parlamentních voleb v roce 2017.Odkaz k prohlédnutí [zde](https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103).
### Instalace knihoven
---
Knihovny, které jsou použity v kódu jsou uložené v souboru requirements.txt.Pro instalaci doporučuji použít nové virtuální prostředí a s nainstalovaným manažerem spustit následovně:

###### pip --version  #ověření verze manažeru
###### pip install -r requirements.txt #instalace knihoven
### Spuštění projektu
---
Spuštění souboru elections_scraper.py v rámci příkaz. řádku požaduje dva povinné argumenty.
###### python elections_scraper.py "odkaz-uzemniho-celku" "nazev-vysledneho-souboru"
Následně se vám stáhnou výsledku jako soubor s připonou .csv.
### Ukázka projektu
---
Výsledky hlasování pro okres Prostějov:
1. argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
2. argument: vysledky_prostejov.csv

Spuštění programu:
###### python elections_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" "vysledky_prostejov.csv"
Průběh stahování:
###### Downloading data from your url: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
###### Saving data in file: vysledky_prostejov.csv
###### Your file vysledky_prostejov.csv was created.Enjoy.Exiting program elections_scraper.py.
Částečný výstup:
###### Town Code, Town Name, Registered, Envelopes, Valid votes,
###### 506761,Alojzov,205,145,144,29,0,0,9,0,5,17,4,1,1,0,0,18,0,5,32,0,0,6,0,0,1,1,15,0
###### 589268,Bediho��,834,527,524,51,0,0,28,1,13,123,2,2,14,1,0,34,0,6,140,0,0,26,0,0,0,0,82,1
