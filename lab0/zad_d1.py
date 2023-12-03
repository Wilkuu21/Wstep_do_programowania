a = float(input("podaj wartosc a: "))
b = float(input("podaj wartosc b: "))
if a == 0:
    if b == 0:
        print("rownanie tozsamosciowe")
    else:
        print("rownanie sprzeczne")
else:
    x = -b / a
    print("x = ", x)
