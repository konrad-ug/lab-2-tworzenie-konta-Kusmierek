import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski","80090298994")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.pesel, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel,"80090298994","Pesel nie został zapisany")
        self.assertEqual(len(pierwsze_konto.pesel),11,"Niepoprawny")
    def test_tworzenie_konta(self):
        pierwsze_konto = Konto("Kacper", "Kacperczyk","800902984")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.pesel, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel,"80090298994","Pesel nie został zapisany")
        self.assertEqual(len(pierwsze_konto.pesel),,"Niepoprawny")


    #tutaj proszę dodawać nowe testy