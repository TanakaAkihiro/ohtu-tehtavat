from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu


class KiviPaperiSakset:
    def __init__(self, io):
        self.io = io
    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            self.io.tulosta(tuomari)

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

        self.io.tulosta("Kiitos!")
        self.io.tulosta(tuomari)
    
    def _ensimmaisen_siirto(self):
        return self.io.lue("Ensimmäisen pelaajan siirto: ")
    
    def _toisen_siirto(self, ensimmaisen_siirto):
        return "k"

    def _onko_ok_siirto(self, siirto):
        if siirto in "kps":
            return True
        return False
