class Konto:
    def __init__(self, imie, nazwisko,pesel,promo=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.PeselValidation(pesel)
        self.PromoChecker(promo)
    def PeselValidation(self,pesel):
        if(len(pesel)!=11):
            self.pesel = "Niepoprawny pesel"
        else:
            self.pesel=pesel
    def PromoChecker(self,promo):
        if(promo != None and promo.startswith('PROM_') and len(promo)==8):
            self.saldo += 50