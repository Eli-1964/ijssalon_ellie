import csv
from presentatie import *
from helper import *
inkomsten = mijn_dict
totaal_inkomsten = som(inkomsten)
presenteer(inkomsten, totaal_inkomsten)
with open('boekhouding.csv', 'w', newline='') as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=';')
    writer.writerow([key, value])