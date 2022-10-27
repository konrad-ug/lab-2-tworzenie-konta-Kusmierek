import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski","80090298994")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel,"80090298994","Pesel nie został zapisany")

        
        
    def test_pesel_incorrect(self):
        niepoprawny_pesel = Konto("Kacper", "Kacperczyk","800902984")
        self.assertEqual(niepoprawny_pesel.pesel,"Niepoprawny pesel","Pesel nie został zapisany")

    def test_bonus_correct(self):
        poprawny_bonus = Konto("Marcin", "Markowski","78092593383","PROM_ABC")
        pesel_over_00 = Konto("Kuba","Kubczak","19311233811","PROM_KIL")

        self.assertEqual(poprawny_bonus.saldo, 50, "Saldo się nie zgadza!")
        self.assertEqual(pesel_over_00.saldo,50,"Saldo się nie zgadza!")

    def test_bonus_incorrect(self):
        niepoprawny_bonus = Konto("Jan", "Jankowski","67094593381","ASDWER")
        niepoprawny_bonus_keyword = Konto("Paweł","Pawłowski","67094593381","OPROM_XYZ")
        pesel_under_65 = Konto("Ola","Aleksandrowska","59094593381","PROM_WER")
        
        self.assertEqual(niepoprawny_bonus.saldo,0,"Saldo się nie zgadza!")
        self.assertEqual(niepoprawny_bonus_keyword.saldo,0,"Saldo się nie zgadza!")
        self.assertEqual(pesel_under_65.saldo,0,"Saldo się nie zgadza!")


    #tutaj proszę dodawać nowe testy