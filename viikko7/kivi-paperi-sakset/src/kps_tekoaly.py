from kivipaperisakset import KiviPaperiSakset as KPS
from tekoaly import Tekoaly


class KPSTekoaly(KPS):
    def __init__(self, io):
        self.io = io
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()

        self.io.tulosta(f"Tietokone valitsi: {tokan_siirto}")

        return tokan_siirto
