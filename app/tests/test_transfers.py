import unittest

from ..KontoFirmowe import KontoFirmowe
from ..Konto import Konto

class TestTransfer(unittest.TestCase):

    def test_transfer(self):
        pierwszy_transfer = Konto("Jacek", "Parówiak","80090298994")
        pierwszy_transfer.ReceiveMoney(10000)
        self.assertEqual(pierwszy_transfer.saldo,10000,"Saldo się nie zgadza")
        pierwszy_transfer.TransferMoney(500)
        self.assertEqual(pierwszy_transfer.saldo,9500,"Saldo się nie zgadza")
        pierwszy_transfer.TransferMoney(-200)
        self.assertEqual(pierwszy_transfer.saldo,9500,"Saldo się nie zgadza")
        pierwszy_transfer.TransferMoney(10000)
        self.assertEqual(pierwszy_transfer.saldo,9500,"Saldo się nie zgadza")

    def test_receive(self):
        konto_receive= Konto("Paweł", "Barman","80090298972")
        konto_receive.ReceiveMoney(300)
        self.assertEqual(konto_receive.saldo,300,"Saldo się nie zgadza")
        konto_receive.ReceiveMoney(500)
        self.assertEqual(konto_receive.saldo,800,"Saldo się nie zgadza")
        konto_receive.ReceiveMoney(-100)
        self.assertEqual(konto_receive.saldo,800,"Saldo się nie zgadza")

    def test_transfers(self):
         konto_transfer= Konto("Krzysztof", "Wypiek","80090298962")
         konto_transfer.ReceiveMoney(1000)
         konto_transfer.TransferMoney(200)
         konto_transfer.ReceiveMoney(500)
         konto_transfer.TransferMoney(300)
         self.assertEqual(konto_transfer.saldo,1000,"Saldo się nie zgadza")




    def test_exp_transfer_os(self):
        konto_os = Konto("Maciej", "Grzegorczyk","80090298974","PROM_ABC")
        konto_os.ReceiveMoney(450)
        
        self.assertEqual(konto_os.saldo,500,"Saldo się nie zgadza")
        konto_os.ExpressTransfer(99)
        self.assertEqual(konto_os.saldo,400,"Saldo się nie zgadza")
        konto_os.ExpressTransfer(400)
        self.assertEqual(konto_os.saldo,-1,"Saldo się nie zgadza")
        konto_os.ExpressTransfer(400)
        self.assertEqual(konto_os.saldo,-1,"Saldo się nie zgadza")

    #tutaj proszę dodawać nowe testy