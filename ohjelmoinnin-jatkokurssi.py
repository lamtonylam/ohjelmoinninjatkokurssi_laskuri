print("ohjelmoinnin jatkokurssin arvosanalaskuri \n")

tehtavapistemaara = 0

osa1 = int(input("anna osan 8 pisteet: "))
osa2 = int(input("anna osan 9 pisteet: "))
osa3 = int(input("anna osan 10 pisteet: "))
osa4 = int(input("anna osan 11 pisteet: "))
osa5 = int(input("anna osan 12 pisteet: "))
osa6 = int(input("anna osan 13 pisteet: "))
osa7 = int(input("anna osan 14 pisteet: "))
if osa7 == 0:
    print("Oho! Huomaathan, että tenttiin osallistuaksesi pitää saada kaikki osan 14 tehtävät hyväksytysti.")

tehtavapistemaara += (osa1+ osa2 + osa3 + osa4 + osa5 + osa6 + osa7)

prosenttimaaratehtava = tehtavapistemaara / 160 * 100

while True:
    koe_valinta = input("haluatko ottaa mukaan myös koepisteet?   Y/N")
    if koe_valinta == "Y" or koe_valinta == "y":
        koe_valinta = True
        break
    if koe_valinta == "N" or koe_valinta == "n":
        koe_valinta = False
        break
    else:
        print("Väärä syöte  \n Y, kyllä. N, ei.")

if koe_valinta == True:
    koe_prosentti = int(input("\n kuinka monta prosenttia koepisteistä sait?"))
    kokonaisprosenttimaara = (koe_prosentti + prosenttimaaratehtava) / 2
else:
    kokonaisprosenttimaara = prosenttimaaratehtava

if kokonaisprosenttimaara > 90:
    print("Arvosana on 5")
elif kokonaisprosenttimaara > 80:
    print("Arvosana on 4")
elif kokonaisprosenttimaara > 70:
    print("Arvosana on 3")
elif kokonaisprosenttimaara > 60:
    print("Arvosana on 2")
elif kokonaisprosenttimaara > 50:
    print("Arvosana on 1")
else:
    print("Arvosana on 0, et päässyt läpi")