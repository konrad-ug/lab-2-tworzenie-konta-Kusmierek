from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.Konto import Konto

app = Flask(__name__)


@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    konto = Konto(dane["imie"], dane["nazwisko"], dane["pesel"])
    RejestrKont.AddAccounts(konto)
    return jsonify("Konto stworzone"), 201


@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    ile = RejestrKont.NumbersOfAccounts()
    print("Ilość kont: "+str(ile))
    return jsonify("Ilość kont: "+str(ile)), 200


@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    konto = RejestrKont.SearchByPesel(pesel)
    print(f"Request o szukanie konta z peselem: {pesel}")
    return jsonify(imie=konto.imie, nazwisko=konto.nazwisko, pesel=konto.pesel, saldo=konto.saldo), 200