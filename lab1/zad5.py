def sortuj_bez_funkcji(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c

a = int(input("Podaj pierwszą zmienną: "))
b = int(input("Podaj drugą zmienną: "))
c = int(input("Podaj trzecią zmienną: "))

print("Posortowane zmienne to:", sortuj_bez_funkcji(a, b, c))