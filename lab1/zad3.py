print("jaka operacje chcesz wykonac? \n 1) dodawanie \n 2) odejmowanie \n 3) mnozenie \n 4) dzielenie \n 5) potegowanie")
operacja = int(input("wpisz numer operacji: "))
x = float(input("podaj argument 1: "))
y = float(input("podaj argument 2: "))
if operacja == 1:
    dodawanie = x + y
    print("dodawanie: ", dodawanie)
elif operacja == 2:
    odejmowanie = x - y
    print("odejmowanie: ", odejmowanie)
elif operacja == 3:
    mnozenie = x * y
    print("mnozenie: ", mnozenie)
elif operacja == 4:
    dzielenie = x / y
    print("dzielenie: ", dzielenie)
elif operacja == 5:
    potegowanie = x ** y
    print("potegowanie: ", potegowanie)
