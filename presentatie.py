def presenteer(mijn_dict, totaal):
    for soort, bedrag in mijn_dict.items():
        print(f"{soort} : {bedrag} euro")
    print("=" * 26)
    print(f"totaal : {totaal} euro")
mijn_dict = {
    'Aardbeien-ijs-totaal' : 1000,
    'Vanille-ijs-totaal' : 2000, 
    'Chocolade-ijs-totaal' : 1500, 
    'Waterijsjes-totaal' : 750
}
totaal = 5250