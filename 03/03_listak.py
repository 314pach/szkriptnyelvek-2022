# dinamikus méretű tömb, több -nem feltétlenül azonos típusú elem- tárolására alkalmas
# lista létrehozása
lista1 = list()     # üres
lista2 = []         # üres

fagyik = ["vanília", "csoki", "sztracsatella", "puncs", "citrom"]   # ebben stringek vannak

# listák hossza
print(len(fagyik))

print("--------------")
# indexelés
print(fagyik[0])        # a legelső listaelem
print(fagyik[-1])       # az utolsó listaelem
print(fagyik[1:3])      # az 1-3. indexű elemek (a 3. indexű elem már nincs benne)
print(fagyik[2:])       # az elemek a 2. indextől a lista végéig
print(fagyik[:])        # a teljes lista
print(fagyik[::2])      # minden második listaelem

# megfordítás
print(fagyik[::-1])

print("--------------")
# értékadás
fagyik[2] = "eper"
print(fagyik)

# bejárás 2 módon is
for iz in fagyik:
    print(iz)

print("--------------")

for i in range(len(fagyik)):
    print(fagyik[i])            # index alapján

print("--------------")
# referencia szerinti működés
def duplaz(szamok):
    for l in range(len(szamok)):        # a számok kétszeresét vesszük
        szamok[l] = szamok[l]*2
    return szamok

szamok = [5, 7, 10, 2, 3]
duplaz(szamok)
print(szamok)

# másolat átadása
dupla = duplaz(szamok[:])
print(szamok)
print(dupla)

print("--------------")
# adott indexű listaelem törlése
del fagyik[1]
print(fagyik)

# listaelem előfordulása
if "csoki" not in fagyik:
    print("A csoki elfogyott")
if "pisztacia" not in fagyik:
    print("Pisztacia nem is volt")
if "citrom" in fagyik:
    print("Citrom meg van")

print("--------------")
# listák összafűzése
szamsor1 = [1, 2, 3, 4, 5]
szamsor2 = [6, 7, 8, 9, 10]

szamsor = szamsor1 + szamsor2
print(szamsor)

# hosszáfűzés
szamsor1.extend(szamsor2)
print(szamsor1)

print("--------------")
# listakezelő füvgények
print(fagyik)
fagyik.append("eper")        # hozzáfűzés a lista végéhez
print(fagyik)
fagyik.insert(0, "csoki")    # beszúrás a lista elejére
print(fagyik)

fagyik.remove("eper")          # a legelső "Thor"-t törli
fagyik.sort()                  # rendezés (itt: ábécé-sorrend)
print(fagyik)
rendezett_fagyik = sorted(fagyik)
print(rendezett_fagyik)

fagyik.clear()                 # lista kiürítése
print(fagyik)

print("--------------")
# szöveg-lista konverzió
szoveg = "Ez itt egy nagon kreatív szöveg"
lista = szoveg.split()
print(lista)
megint_szoveg = " ".join(lista)     # stringkezelő függvény, nem listakezelő!
print(megint_szoveg)

print("--------------")
# list comprehension példa
gyumolcsok = ["alma", "banán", "cseresznye", "kiwi", "mangó"]
ujlista = [x for x in gyumolcsok if "a" in x]
print(ujlista)
