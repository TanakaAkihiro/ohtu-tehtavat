from unittest import result
from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoslista = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        if self.ostoslista == []:
            return 0

        summa = 0
        for ostos in self.ostoslista:
            summa += ostos.lukumaara()
        
        return summa
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        if self.ostoslista == []:
            return 0
        
        summa = 0
        for ostos in self.ostoslista:
            summa += ostos.hinta()
        
        return summa
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        boolean = False
        for ostos in self.ostoslista:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                boolean = True

        if not boolean:
            self.ostoslista.append(Ostos(lisattava))
        

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for ostos in self.ostoslista:
            if ostos.tuotteen_nimi() == poistettava.nimi() and ostos.hinta()/ostos.lukumaara() == poistettava.hinta():
                ostos.muuta_lukumaaraa(-1)
                if ostos.lukumaara() == 0:
                    self.ostoslista.remove(ostos)

    def tyhjenna(self):
        self.ostoslista = []
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.ostoslista
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
