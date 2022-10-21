class Konto:
    def __init__(self, imie, nazwisko,pesel,rabat):
        self.imie = imie
        self.nazwisko = nazwisko
        if(len(pesel)!=11):
            self.pesel="Niepoprawny pesel"
        else:
            self.pesel = peselgiu
        
        self.saldo = 0
        self.rabat = rabat
