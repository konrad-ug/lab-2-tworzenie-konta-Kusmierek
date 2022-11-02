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
        konto_firmowe.ReceiveMoney(200)
        self.assertEqual(konto_firmowe.saldo,700,"Saldo się nie zgadza")

    def test_firmowe_NIP(self):
        konto_firmowe_corr = KontoFirmowe("CD_Projekt","1234567892")
        konto_firmowe_incorr = KontoFirmowe("Psia Karma","123456789")

        self.assertEqual(konto_firmowe_corr.nip,"1234567892","Wartość NIP się nie zgadza")
        self.assertEqual(konto_firmowe_incorr.nip,"Niepoprawny NIP!", "Wartość NIP się nie zgadza")

    def test_exp_transfer_firm(self):
        konto_firmowe_exp = KontoFirmowe("Kakaowex","1234567898")
        konto_firmowe_exp.ReceiveMoney(1000)
        self.assertEqual(konto_firmowe_exp.saldo,1000,"Saldo się nie zgadza")
        konto_firmowe_exp.ExpressTransfer(195)
        self.assertEqual(konto_firmowe_exp.saldo,800,"Saldo się nie zgadza")
        konto_firmowe_exp.ExpressTransfer(800)
        self.assertEqual(konto_firmowe_exp.saldo,-5,"Saldo się nie zgadza")

        konto_os = Konto("Maciej", "Grzegorczyk","80090298974","PROM_ABC")
        konto_os.ReceiveMoney(450)
        self.assertEqual(konto_os.saldo,500,"Saldo się nie zgadza")
        konto_os.ExpressTransfer(99)
        self.assertEqual(konto_os.saldo,400,"Saldo się nie zgadza")
        konto_os.ExpressTransfer(400)
        self.assertEqual(konto_os.saldo,-1,"Saldo się nie zgadza")

    #tutaj proszę dodawać nowe testy