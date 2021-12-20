from kivipaperisakset import KiviPaperiSakset as KPS
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KPS):
    def __init__(self, io) -> None:
        self.io = io
        self.tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmainen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()

        self.io.tulosta(f"Tietokone valitsi: {tokan_siirto}")
        self.tekoaly.aseta_siirto(ensimmainen_siirto)

        return tokan_siirto
