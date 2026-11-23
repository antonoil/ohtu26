import unittest
from unittest.mock import Mock
from kauppa import Kauppa
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()
        self.varastossa = {1: 10}
        self.tuotteet = {1: Tuote(1, "maito", 5)}
        self.varasto_mock.saldo.side_effect = lambda tuote_id: self.varastossa.get(tuote_id)
        self.varasto_mock.hae_tuote.side_effect = lambda tuote_id: self.tuotteet.get(tuote_id)

        self.kauppa = Kauppa(
            self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock
        )

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):
        kauppa = self.kauppa

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan_oikein(self):
        kauppa = self.kauppa

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikein
        self.pankki_mock.tilisiirto.assert_called_once_with("pekka", 42, "12345", "33333-44455", 5)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_maksettaessa_samat_ostokset_pankin_metodia_tilisiirto_kutsutaan_oikein(self):
        kauppa = self.kauppa

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikein
        self.pankki_mock.tilisiirto.assert_called_once_with("pekka", 42, "12345", "33333-44455", 10)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_maksettaessa_eri_ostokset_pankin_metodia_tilisiirto_kutsutaan_oikein(self):
        self.varastossa[2] = 10
        self.tuotteet[2] = Tuote(2, "kaali", 3)
        kauppa = self.kauppa

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikein
        self.pankki_mock.tilisiirto.assert_called_once_with("pekka", 42, "12345", "33333-44455", 8)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_maksettaessa_eri_ostoksista_loppunut_tuote_ei_mene_maksuun(self):
        self.varastossa[2] = 0
        self.tuotteet[2] = Tuote(2, "kaali", 3)
        kauppa = self.kauppa

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_once_with(
            "pekka", 42, "12345", "33333-44455", 5
        )
        self.varasto_mock.hae_tuote.assert_called_once_with(1)
    
