from kivipaperisakset import KiviPaperiSakset as KPS


class KPSPelaajaVsPelaaja(KPS):
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.io.lue("Toisen pelaajan siirto: ")

        return tokan_siirto
