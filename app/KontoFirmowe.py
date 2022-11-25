from .Konto import Konto

class KontoFirmowe(Konto):
    def __init__(self,nazwa,nip):
        self.nazwa = nazwa
        self.saldo = 0
        self.NipValidation(nip)
        self.historia = []
        

    def NipValidation(self,nip):
        if(len(nip)==10 and nip.isnumeric()):
            self.nip = nip;
        else:
            self.nip = "Niepoprawny NIP!"

    def ExpressTransfer(self,kwota):
        if(kwota>0):
            price = 5;
            if(self.saldo>=kwota):
                self.saldo-=kwota+price
                self.historia.insert(0, -kwota)
                self.historia.insert(0, -price)


