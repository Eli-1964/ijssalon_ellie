# Imports
from algemene_functies import mijn_functie_2
# Functie 1: aanbieding
def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs:.2f} euro."
print(aanbieding_1("aardbei", 4, 0.1))
# Functie 2: totaal inkomsten + btw
def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag:.2f} euro btw betaald dient te worden."
week =  [220, 430, 125, 160, 205, 90, 345]
print(inkomsten_totaal(week, 0.09))
# Functie 3: hoogste en laagste waarden
def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return (hoogste, laagste)
week = [220, 430, 125, 160, 205, 90, 345]
print(laag_en_hoog(week))
# Functie 4: gemiddelde
def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    gem = totaal / aantal
    return f"De gemiddelde inkomsten van deze week zijn {gem} euro."
week = [220, 430, 125, 160, 205, 90, 345]
print(gemiddelde(week))
# Functie 5: hergebruik van laag en hoog
def meervoudig(invoer_lijst):    
    return laag_en_hoog(invoer_lijst)
invoer_lijst = [10, 5, 3, 2, 1, 2, 9]
print(meervoudig(invoer_lijst))
# Functie 6: combinatie met externe functie
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(*korte_lijst)
print(combinatie(week))