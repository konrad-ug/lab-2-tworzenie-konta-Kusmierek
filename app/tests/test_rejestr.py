import unittest

from ..Konto import Konto
from ..RejestrKont import RejestrKont

class TestAccounts(unittest.TestCase):
    imie="Oskar"
    nazwisko="Kusmierek"
    pesel="12345678999"

    @classmethod
    def setUpClass(cls):
        konto1=Konto(cls.imie, cls.nazwisko, cls.pesel)
        RejestrKont.AddAccounts(konto1)

    def test_1_adding_first_account(self):
        konto1=Konto(self.imie, self.nazwisko, self.pesel)
        konto2=Konto(self.imie, self.nazwisko, self.pesel)
        RejestrKont.AddAccounts(konto1)
        RejestrKont.AddAccounts(konto2)
        self.assertEqual(RejestrKont.NumbersOfAccounts(),3, "Powinny byc 3 konta")
    
    def test_2_adding_second_account(self):
        konto1=Konto(self.imie, self.nazwisko, self.pesel)
        RejestrKont.AddAccounts(konto1)
        self.assertEqual(RejestrKont.NumbersOfAccounts(),4, "Powinny byc 4 konta")
    

    def test_3_find_account(self):
        konto1=Konto(self.imie, self.nazwisko, self.pesel)
        konto2=Konto("Mariusz", "Pudzianowski", "12345678911")
        RejestrKont.AddAccounts(konto1)
        RejestrKont.AddAccounts(konto2)
        self.assertEqual(RejestrKont.SearchByPesel("12345678911"),konto2, "Uzytkownik to nie Mariusz Pudzianowski")

    def test_4_znajdz_konto(self):
        konto1=Konto(self.imie, self.nazwisko, self.pesel)
        konto2=Konto("Andrzej", "Duda", "12345668900")
        konto3=Konto("Karol", "Marcepan", "12345668800")
        RejestrKont.AddAccounts(konto1)
        RejestrKont.AddAccounts(konto2)
        RejestrKont.AddAccounts(konto3)
        self.assertEqual(RejestrKont.SearchByPesel("12345668900"),konto2, "Użytkownik to nie Andrzej Duda")
    
    def test_5_znajdz_konto_nie_ma(self):
        self.assertEqual(RejestrKont.SearchByPesel("12444678000"),None, "None powinno byc zwrocone")
    
    @classmethod
    def tearDownClass(cls):
        RejestrKont.usersAccounts=[]