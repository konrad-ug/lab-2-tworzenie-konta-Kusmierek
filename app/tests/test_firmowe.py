import unittest

from ..KontoFirmowe import KontoFirmowe
from ..Konto import Konto


class TestFirmowe(unittest.TestCase):
      def test_firmowe_rec(self):
        konto_firmowe = KontoFirmowe("Płotex","1234567890")

        konto_firmowe.ReceiveMoney(500)
        self.assertEqual(konto_firmowe.saldo,500,"Saldo się nie zgadza")
        konto_firmowe.ReceiveMoney(200)
        self.assertEqual(konto_firmowe.saldo,700,"Saldo się nie zgadza")
        konto_firmowe.ReceiveMoney(-200)
      
      def test_firmowe_tran(self):
          konto_firmowe = KontoFirmowe("Marcepany","1234567892")

          konto_firmowe.ReceiveMoney(700)
          konto_firmowe.TransferMoney(300)
          self.assertEqual(konto_firmowe.saldo,400,"Saldo się nie zgadza")
          konto_firmowe.TransferMoney(500)
          self.assertEqual(konto_firmowe.saldo,400,"Saldo się nie zgadza")
          konto_firmowe.TransferMoney(400)
          self.assertEqual(konto_firmowe.saldo,0,"Saldo się nie zgadza")

      def test_firmowe_NIP(self):
        konto_firmowe_corr = KontoFirmowe("CD_Projekt","1234567892")
        konto_firmowe_incorr = KontoFirmowe("Psia Karma","123456789")
        konto_firmowe_alph=KontoFirmowe("Karmex","123456789AB")

        self.assertEqual(konto_firmowe_alph.nip,"Niepoprawny NIP!", "Wartość NIP się nie zgadza")
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
        konto_firmowe_exp.ExpressTransfer(800)
        self.assertEqual(konto_firmowe_exp.saldo,-5,"Saldo się nie zgadza")