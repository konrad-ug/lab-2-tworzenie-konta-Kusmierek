import unittest

from ..KontoFirmowe import KontoFirmowe
from parameterized import parameterized

class TestLoanCp(unittest.TestCase):
    def setUp(self):
        self.konto_cp=KontoFirmowe("Zubrowkex", "123456789")

    @parameterized.expand([
        ([100,200,300,400,500, -1775], 200, True, 200),
        ([100,200,300,400,100, -1775], 200, True, 200),
        ([100,200], 500, False, 0),
        ([100,200, 1775], 500, False, 0),
        ([-1775,2000,3000,400,100, -1775], 100, True, 100),
    ])

    def test_loan_cp(self, historia, kwota, result, oczek_saldo):
        self.konto_cp.historia=historia
        self.assertEqual(self.konto_cp.take_loan(kwota), result, "Nie udało się zaciágnąć kredytu!")
        self.assertEqual(self.konto_cp.saldo, oczek_saldo, "Niepoprawna kwota!")
    