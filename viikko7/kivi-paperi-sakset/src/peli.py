from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


class Peli:
    @staticmethod
    def luo_kaksinpeli(io):
        return KPSPelaajaVsPelaaja(io)
    
    @staticmethod
    def luo_tekoaly_peli(io):
        return KPSTekoaly(io)
    
    @staticmethod
    def luo_parempi_tekoaly_peli(io):
        return KPSParempiTekoaly(io)
