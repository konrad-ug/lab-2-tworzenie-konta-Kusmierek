class RejestrKont():
    konta = []
    @classmethod
    def AddAccounts(cls,konto):
        cls.konta.append(konto)

    @classmethod
    def SearchByPesel(cls,pesel):
        return next((x for x in cls.konta if x.pesel == pesel), None)

    @classmethod
    def NumbersOfAccounts(cls):
        return len(cls.konta)
    