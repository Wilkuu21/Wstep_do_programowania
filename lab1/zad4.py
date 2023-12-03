import math
a = float(input("podaj wartosc wspolczynnika a:"))
b = float(input("podaj wartosc wspolczynnika b:"))
c = float(input("podaj wartosc wspolczynnika c:"))
delta = (b * b) - 4 * a * c
if delta == 0:
    x0 = -b / 2 * a
    print("x0 = ", x0)
elif delta > 0:
    x1 = (-b - math.sqrt(delta) / 2 * a)
    x2 = (-b + math.sqrt(delta) / 2 * a)
    print("x1 = ", x1, " x2 = ", x2)
elif delta < 0:
    print("Nie ma pierwiastkow.")
