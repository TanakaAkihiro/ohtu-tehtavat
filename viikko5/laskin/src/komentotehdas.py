class Komentotehdas:
    def __init__(self, sovellus):
        self.sovellus = sovellus
        self.komennot = {
            1: Summa(self.sovellus),
            2: Erotus(self.sovellus),
            3: Nollaus(self.sovellus),
            4: Kumoa(self.sovellus)
        }
    
    def hae(self, komento):
        return self.komennot[komento]

class Summa:
    def __init__(self, sovellus) -> None:
        self.sovellus = sovellus
    
    def suorita(self, arvo):
        self.sovellus.plus(arvo)

class Erotus:
    def __init__(self, sovellus) -> None:
        self.sovellus = sovellus
    
    def suorita(self, arvo):
        self.sovellus.miinus(arvo)

class Nollaus:
    def __init__(self, sovellus) -> None:
        self.sovellus = sovellus
    
    def suorita(self, arvo):
        self.sovellus.nollaa()
    
class Kumoa:
    def __init__(self, sovellus) -> None:
        self.sovellus = sovellus
    
    def suorita(self, arvo):
        pass
