wiek = int(input("podaj wiek klienta: "))
if wiek < 4:
    cena = "bezplatnie"
elif 4 < wiek < 18:
    cena = 10
else:
    cena = 20
print("Cena biletu: ", cena)