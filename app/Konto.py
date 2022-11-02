from pkgutil import extend_path


class Konto:
    def __init__(self, imie, nazwisko,pesel,promo=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.PeselValidation(pesel)
        self.PromoChecker(promo)

    def PeselValidation(self,pesel):
        if(len(pesel)!=11 or not pesel.isnumeric()):
            self.pesel = "Niepoprawny pesel"
        else:
            self.pesel=pesel

    def PromoChecker(self,promo):
        if(promo != None and promo.startswith('PROM_') and len(promo)==8 and( int(self.pesel[0:2])>60 or ((int(self.pesel[2:4])>20) and int(self.pesel[2:4])<33))):
            self.saldo += 50

    def TransferMoney(self,kwota):
        if(self.saldo>=kwota):
            self.saldo-=kwota
    
    def ReceiveMoney(self,kwota):
        self.saldo += kwota;

    def ExpressTransfer(self,kwota):
        price = 1;
        if(self.saldo>=kwota):
            self.saldo-=kwota+price
