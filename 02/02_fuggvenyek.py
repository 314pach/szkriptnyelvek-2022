def fgv():
    print("A szkriptnyelvek a legjobb tantargy")

fgv()


def fgv(kedvenc):
    print("A(z)", kedvenc, "a legjobb tantargy")

fgv("koszi")


def fgv(kedvenc="szkriptnyelvek"):
    print("A(z)", kedvenc, "a legjobb tantargy")

fgv()
fgv("koszi")


def fagyi(iz, gombocok=None, edestolcser=None):
    szoveg = "Ez "
    if gombocok is not None:        # ha adtunk meg gombocok parametert
        szoveg += str(gombocok) + " gomboc "
    szoveg += iz + " izu fagylalt "
    if edestolcser is not None:     # ha adtunk meg edestolcser parametert
        if edestolcser:
            szoveg += "edestolcserben"
        else:
            szoveg += "sima tolcserben"
    print(szoveg)

fagyi("csoki", 2, True)
fagyi("csoki", edestolcser=False)
