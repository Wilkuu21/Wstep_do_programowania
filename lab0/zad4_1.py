import random
droga = random.randint(1, 100000)
srednie_spalanie = float(input("podaj srednie spalanie samochodu(w l/100km): "))
cena_paliwa = 6.5
zuzycie = (droga * srednie_spalanie) / 100
koszt = zuzycie * cena_paliwa
print("przejechales: ", droga, "zuzyles: ", zuzycie, " litrow paliwa, a koszt przejechania tej trasy wyniesie: ", koszt)
