# egysoros komment

# több
# soros
# komment

# kiíratás
print("hello python")
print("itt", 1, "csomó", "paraméter")

## adattípusok
# az itt felsoroltakon kívül is vannak még
# bool - case sensitive!
val = True
# val = False

# számok: int, float
val = 5
print(type(val))

val = 3.14
print(type(val))

# stringek
print('Így is ' + "lehet")
print("Python goes b" + 5 * "rrr")
print(10* "NA" + " BATMAN")

## extrásabb operátorok
print(7/2)      # lebegőpontos (valós) osztás
print(7//2)     # egész osztás
print(7**2)     # hatványozás
# logikai operátorok: and, or, not

## inkrementálás, dekrementálás
val = 10
# val++ # ez hibás!!!
val += 1

## típuskonverzió
# szöveg -> szám
int("420")      # 420
float("1.5")    # 1.5

# szám -> szöveg
print(str(1) + ", egy almafa") # csak stringeket lehet összefűzni!!!

## beolvasás a konzolról
val = input("Írj be valamit! ")
print(val)

# Feladat
# Kérjük be a felhasználó születési évét, és írjuk ki az életkorát a konzolra

szul_ev = input("Mikor szulettel? ")
val= 2022 - int(szul_ev)
print(str(val) + " eves vagy!")
