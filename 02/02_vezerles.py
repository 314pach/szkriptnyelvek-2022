# blokkszerkezet
val = "Ajjajj"
 # print(val, "ebből baj lesz")


# szelekciós vezérlés
szam = int(input("Irj be egy szamot! "))
if szam < 50:
    print("A szam kisebb, mint 50")
elif 50 <= szam < 100:
    print("A szam 50 es 100 koze esik")
else:
    print("A szam nagyobb, mint 100")

print("-------------------------------")

# ismétléses utasítások / ciklusok
szam = int(input("Adj meg egy szamot! "))
i = 1
while szam > 1:
    i *= szam
    szam -= 1      # no --
print("A megadott szam faktorialisa:", i)

print("-------------------------------")
for betu in "szoveg":
    print(betu)

print("-------------------------------")
tantargyak = ["szkript", "webterv", "progalap", "kalkulus"]
for elem in tantargyak:
    if elem != "kalkulus":
        print("A", elem, "konnyu targynak szamit")

print("-------------------------------")
for i in range(5):
    print("Ez eskü egy kalsszikus for ciklus")

print("-------------------------------")
for i in range(10, -10, -2):  # start : stop : step, stop már nincs benne
    print(i)
