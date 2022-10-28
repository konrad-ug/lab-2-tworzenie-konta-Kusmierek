import unittest

from ..KontoFirmowe import KontoFirmowe
from ..Konto import Konto

class TestTransfer(unittest.TestCase):

    def test_payment(self):
        pierwszy_transfer = Konto("Jacek", "Parówiak","80090298994")
        pierwszy_transfer.ReceiveMoney(10000)
        
        self.assertEqual(pierwszy_transfer.saldo,10000,"Saldo się nie zgadza")
        pierwszy_transfer.TransferMoney(500)
        self.assertEqual(pierwszy_transfer.saldo,9500,"Saldo się nie zgadza")

    def test_firmowe(self):
        konto_firmowe = KontoFirmowe("Płotex","1234567890")

        konto_firmowe.ReceiveMoney(500)
        self.assertEqual(konto_firmowe.saldo,500,"Saldo się nie zgadza")
    #tutaj proszę dodawać nowe testy