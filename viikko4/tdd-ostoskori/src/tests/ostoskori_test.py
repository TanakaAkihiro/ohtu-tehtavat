import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
    
    def test_palauttaa_oikean_maaran_tavaroita(self):
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

        maito = Tuote("maito", 5)
        suklaa = Tuote("maito", 7)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(suklaa)

        self.assertEqual(self.kori.tavaroita_korissa(), 3)
 