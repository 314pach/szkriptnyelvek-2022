# sajat kivetel osztály:

class Bor:
    def __init__(self, fajta, evjarat, alkoholtartalom=12.5):
        self._fajta = fajta
        self._evjarat = evjarat
        self.alkoholtartalom = alkoholtartalom

    @property
    def fajta(self):
        return self._fajta

    @fajta.setter
    def fajta(self, ertek):
        self._fajta = ertek

    @property
    def evjarat(self):
        return self._evjarat

    @evjarat.setter
    def evjarat(self, ertek):
        self._evjarat = ertek

    @property
    def alkoholtartalom(self):
        return self._alkoholtartalom

    @alkoholtartalom.setter
    def alkoholtartalom(self, ertek):
        if 0 < ertek < 100:
            self._alkoholtartalom = ertek
        else:
            print("Nem megfelelo alkoholtartalom!")

    def __str__(self):
        return f"{self.fajta} (evjarat: {self.evjarat}), melynek alkoholtartalma: {self.alkoholtartalom}%"

    def __eq__(self, other):
        if isinstance(other, Bor):
            return self.fajta.lower() == other.fajta.lower() and self.evjarat==other.evjarat and self.alkoholtartalom == other.alkoholtartalom
        else:
            return False

class Szekreny:
    def __init__(self):
        self.borok = []

    def get_bor(self, n):
        if n >len(self.borok) or n < 0:
            print("Nem letezo index!")
        else:
            return self.borok[n]

    def __iadd__(self, other):
        if isinstance(other, Bor):
            self.borok.append(other)
        else:
            print("Nem bor!")

    def __add__(self, other):
        if isinstance(other, Szekreny):
            uj_szekreny = Szekreny()
            uj_szekreny.borok = self.borok + other.borok
            return uj_szekreny
        else:
            print("Nem szekreny!")