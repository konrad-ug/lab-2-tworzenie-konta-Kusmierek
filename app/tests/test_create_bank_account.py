import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski","80090298994")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel,"80090298994","Pesel nie został zapisany")

        
        
    def test_niepoprawny_pesel(self):
        drugie_konto = Konto("Kacper", "Kacperczyk","800902984")
        self.assertEqual(drugie_konto.imie, "Kacper", "Imie nie zostało zapisane!")
        self.assertEqual(drugie_konto.nazwisko, "Kacperczyk", "Nazwisko nie zostało zapisane!")
        self.assertEqual(drugie_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(drugie_konto.pesel,"Niepoprawny pesel","Pesel nie został zapisany")

    def test_bonus(self):
        trzecie_konto = Konto("Marcin", "Markowski","59092593383","PROM_ABC")
        self.assertEqual(trzecie_konto.imie, "Marcin", "Imie nie zostało zapisane!")
        self.assertEqual(trzecie_konto.nazwisko, "Markowski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(trzecie_konto.saldo, 50, "Saldo się nie zgadza!")
        self.assertEqual(trzecie_konto.pesel,"59092593383","Pesel nie został zapisany")
    
    #tutaj proszę dodawać nowe testy