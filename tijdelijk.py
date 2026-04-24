# Stap 1: Toevoegen van een nieuw bestand aan de map IJssalon-start met de naam tijdelijk.py
# Stap 2: maak de dictionary
prijzen_dictionary = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade": 5
}
# Stap 3: bereken de aanbieding (20% korting op aardbei)
aanbieding = prijzen_dictionary ["aardbei"] * 0.8
# Stap 4: maak de formatted string
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"
# Stap 5: print de tekst
reclame_tekst2 = reclame_tekst[:62]
# Stap 6: Spandoek sportvliegtuigje
reclame_tekst3 = reclame_tekst[:62].upper()
# Stap 7: Reclametekst als een list van woorden
reclame_tekst4 = reclame_tekst3.split()
# Stap 8: Woorden onder elkaar afgedrukt voor een flyer - for-loop
for el in reclame_tekst4:
# Stap 9: Geen hoofdletters - string-method.lower - print(el.lower())
# Stap 10: if-statement
    if len(el) >=5:
        print(el.upper())
    else:
        print(el.lower())
# Stap 11: Nieuwe lokale versie met tekst "bestand tijdelijk.py gecodeerd" tweede commando via Terminal
# Stap 12: Updaten van de remote repo op GitHub
# Stap 13: De URL van mijn remote repo op GitHub via Plaza mailen