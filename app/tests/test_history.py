import unittest

from ..KontoFirmowe import KontoFirmowe
from ..Konto import Konto


class TestHistory(unittest.TestCase):

    def test_combined_transfer(self):
        konto_os = Konto("Marcin", "Chrzaszcz","80090298974","PROM_ABC")
        konto_os.ReceiveMoney(450)
        konto_os.ExpressTransfer(80)
        konto_os.ExpressTransfer(70)
        konto_os.TransferMoney(200)
        self.assertEqual(konto_os.historia, [-200,-1, -70,-1, -80, 450], "Niepoprawna historia przelewów!")

    def test_combined_transfer_company(self):
        konto_firmowe = KontoFirmowe("Karolex","1234567890")

        konto_firmowe.ReceiveMoney(500)
        konto_firmowe.ReceiveMoney(200)
        konto_firmowe.ExpressTransfer(50)
        konto_firmowe.TransferMoney(100)
        self.assertEqual(konto_firmowe.historia, [-100,-5, -50, 200, 500], "Niepoprawna historia przelewów!")