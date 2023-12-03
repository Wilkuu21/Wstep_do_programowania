import math
boka = float(input("podaj dlugosc boku a: "))
bokb = float(input("podaj dlugosc boku b: "))
bokc = float(input("podaj dlugosc boku c: "))
p = (boka + bokb + bokc) / 2
pole = math.sqrt(p*((p - boka)*(p - bokb)*(p - bokc)))
print("pole trojkata wynosi: ", pole)
