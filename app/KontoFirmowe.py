from .Konto import Konto

class KontoFirmowe(Konto):
    def __init__(self,nazwa,nip):
        self.nazwa = nazwa
        self.saldo = 0
        self.NipValidation(nip)

    def NipValidation(self,nip):
        if(len(nip)==10):
            self.nip = nip;
        else:
            self.nip = "Niepoprawny NIP!"

    def ExpressTransfer(self,kwota):
        price = 5;
        if(self.saldo>=kwota):
            self.saldo-=kwota+price


