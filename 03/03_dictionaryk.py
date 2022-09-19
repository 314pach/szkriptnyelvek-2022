# szótár: kulcs-érték párokat tartalmaz
# dictionary létrehozása
szotar1 = dict()    # üres
szotar2 = {}        # üres

hallgato = {"neptun": "ty2d4", "szak": "pti", "eletkor": 20}
print(hallgato)
print("--------------")

# dictionaryk hossza
print(len(hallgato))
print("--------------")

# elemek elérése
print(hallgato["szak"])             # indexeles
# print(hallgato["csuszik_e"])      # ez nem lesz jo!

print(hallgato.get("szak"))         # get() függvény
print(hallgato.get("csuszik_e"))
print("--------------")

# elem módosítása
hallgato["eletkor"] = 21
print(hallgato)

# új elem hozzáadása
hallgato["nev"] = "Kis Béla"
print(hallgato)

# elem törlése
del hallgato["szak"]
print(hallgato)
print("--------------")

# kulcs előfordulásának ellenőrzése
# hallgato["szak"] = "pti"
if "szak" in hallgato:
    print(f"{hallgato.get('nev')} {hallgato.get('szak')}-ra jar")
else:
    print("Fene tudja, bárhova járhat")

print("--------------")

# dictionaryk bejárása
for kulcs in hallgato:              # kulcsok bejárása
    print(kulcs)

print("--------------")

for ertek in hallgato.values():     # értékek bejárása
    print(ertek)

print("--------------")

for kulcs, ertek in hallgato.items():   # kulcs-érték párok bejárása
    print(str(kulcs) + ": " + str(ertek))
