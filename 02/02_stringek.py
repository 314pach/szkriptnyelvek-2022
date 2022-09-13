hosszu_szoveg = """Never gonna give you up
Never gonna let you down
Never gonna run around and desert you"""

# összefűzés
szoveg = "cica" + "mica"
print(szoveg)

szoveg = str(101) + " kiskutya"     # csak stringeket lehet összefűzni
print(szoveg)

# szövegek hossza
print(len("alma"))

# indexelés
szoveg = "Hókuszpók"
print("A 0. indexű karakter:", szoveg[0])   # az indexelés 0-tól kezdődik
print("A 2. indexű karakter:", szoveg[2])
print("Az utolso karakter:", szoveg[-1])

print("4-10. karakter, 2-es lépésközzel:", szoveg[4:8:2])
print("2-5. karakter:", szoveg[2:5])
print("Elejétől a 6. karakterig:", szoveg[:6])
print("6. karaktertől a string végéig:", szoveg[6:])
print("A teljes szöveg:", szoveg[:])
print("Minden második karakter:", szoveg[::2])

print(szoveg[::-1])     # a szöveg megfordítása

# immutable (nem módositható)
# szoveg[0] = 'K'   # nem szabad!

# rész-string előfordulása - in kulcsszó
if "Never gonna" in hosszu_szoveg:
    print("Rick roll")

# stringkezelő függvények
szoveg = "   Az összes lekvár közül a baracklekvár a kedvencem                "
szoveg = szoveg.strip()   # helyközök eltávolítása a szöveg elejéről és végéről

print(szoveg.lower())               # kisbetűsítés
print(szoveg.upper())               # nagybetűsítés
print(szoveg.endswith("kedvenc"))   # a "szerint" stringre végződik-e a szöveg
print(szoveg.count("a"))            # hány darab 'a' betű van a szövegben
print(szoveg.replace("lekvár", "fa"))  # lecserélés
print(szoveg.split(" "))            # feldarabolás szóközök mentén

# formázott kiíratás
PI = 3.14159265359
print("A pí értéke: {}".format(PI))                   # format() metódus

nev = "Béla"
eletkor = 21
print("Hello, %s vagyok, %d éves." % (nev, eletkor))  # %-formatting

elet_ertelme = 42
print(f"Az élet értelme: {elet_ertelme}")             # f-string

