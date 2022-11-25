from pkgutil import extend_path


class Konto:
    def __init__(self, imie, nazwisko,pesel,promo=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.PeselValidation(pesel)
        self.PromoChecker(promo)
        self.historia = []

    def PeselValidation(self,pesel):
        if(len(pesel)!=11 or not pesel.isnumeric()):
            self.pesel = "Niepoprawny pesel"
        else:
            self.pesel=pesel

    def PromoChecker(self,promo):
        if(promo != None and promo.startswith('PROM_') and len(promo)==8 and( int(self.pesel[0:2])>60 or ((int(self.pesel[2:4])>20) and int(self.pesel[2:4])<33))):
            self.saldo += 50

    def TransferMoney(self,kwota):
        if(kwota>0):
            if(self.saldo>=kwota):
                self.saldo-=kwota
                self.historia.insert(0, -kwota)
    
    def ReceiveMoney(self,kwota):
        if(kwota>0):
            self.saldo += kwota;
            self.historia.insert(0, kwota)

    def ExpressTransfer(self,kwota):
        if(kwota>0):
            price = 1;
            if(self.saldo>=kwota):
                self.saldo-=kwota+price
                self.historia.insert(0, -kwota)
                self.historia.insert(0,-price)
