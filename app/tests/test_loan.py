
import unittest

from ..Konto import Konto
from parameterized import parameterized

class TestLoan(unittest.TestCase):
    def setUp(self):
        self.konto_os=Konto("Marek", "Pawlacz", "12345678111")

    @parameterized.expand([
        ([100,200,300,700,600], 600, True, 600),
        ([100,100], 300, False, 0),
        ([-100,-200,300,400,100],100, False, 0),
        ([100,200,300,-100,-100], 200, True, 200),
        ([200,200,200,-100,100,-300], 200, True, 200),
    ])

    def test_loan(self, historia, kwota, result, oczek_saldo):
        self.konto_os.historia=historia
        self.assertEqual(self.konto_os.take_loan(kwota), result, "Nie udało się zaciągnąć kredytu!")
        self.assertEqual(self.konto_os.saldo,oczek_saldo, "Niepoprawna kwota!")

