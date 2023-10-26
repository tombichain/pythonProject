nombre = int(input("Entrez un nombre entier: "))

if nombre > 0:
    status = "positif"
elif nombre < 0:
    status = "négatif"
else:
    status = "zéro"

if nombre % 2 == 0:
    parite = "pair"
else:
    parite = "impair"

if nombre == 0:
    print(f"Le nombre est {status} (et il est {parite})")
else:
    print(f"Le nombre est {status}\t et {parite}")