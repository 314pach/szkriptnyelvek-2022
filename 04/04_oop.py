# osztály létrehozása
class IrinyiKabinetesOperator:
    def __init__(self, nev, pizzaSzeletekSzama, fizetes=500000):
        self.nev = nev
        self._pizzaSzeletekSzama = pizzaSzeletekSzama
        self._fizetes = fizetes

    def twitchStreametNez(self):
        self.pizzaSzeletekSzama -= 1

    #################################

    def get_pizzaSzeletekSzama(self):  # getter metódus
        return self._pizzaSzeletekSzama

    def set_pizzaSzeletekSzama(self, szam):  # setter metódus
        self._pizzaSzeletekSzama = szam

    #################################
    # a fetniek helyett propertyk:
    @property
    def fizetes(self):
        return self._fizetes

    @fizetes.setter
    def fizetes(self, ertek):
        self._fizetes = ertek

    #################################
    # szöveggé alakítás

    def __str__(self):
        return f"A nevem {self.nev}, {self.get_pizzaSzeletekSzama()} szelet pizzám van, és {self.fizetes} Ft-ot keresek"

    #################################
    # operator overloading

    def __gt__(self, other):
        if self.get_pizzaSzeletekSzama() > other.get_pizzaSzeletekSzama():
            return True
        else:
            return False

    def __lt__(self, other):
        if self.get_pizzaSzeletekSzama() < other.get_pizzaSzeletekSzama():
            return True
        else:
            return False

    def __add__(self, other):
        if isinstance(other, IrinyiKabinetesOperator):      # típusellenőrzés
            uj_operator = IrinyiKabinetesOperator(
                "László",
                self.get_pizzaSzeletekSzama() + other.get_pizzaSzeletekSzama(),
                (self.fizetes + other.fizetes)//2
            )
            return uj_operator
        else:
            print(f"Operátort csak másik operátorral adhatsz össze, {type(other)}-rel nem")


# Példányosítás #
#################

op1 = IrinyiKabinetesOperator("Sanyi", 3, 476000)
op2 = IrinyiKabinetesOperator("Joci", 5)
print(op1)
print(op2)

if op1 < op2:
    print(f"{op2.nev}-nak több pizzája van, mint {op1.nev}-nak")

op3 = op1 + op2
print(op3)

op4 = op3 + "szeretek videójátékozni"
