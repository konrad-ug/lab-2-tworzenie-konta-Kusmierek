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

    def check_sum_loan_cp(self, kwota):
        return super().check_sum_loan(2*kwota)

    
    def check_ZUS(self):
        if(-1775 in self.historia):
            return True
        else:
            return False

    def take_loan(self, kwota):
        if (self.check_ZUS() and self.check_sum_loan_cp(kwota)):
            self.saldo += kwota
            return True
        else:
            return False
