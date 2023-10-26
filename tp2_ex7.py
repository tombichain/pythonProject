import random

nombre_aleatoire = random.randint(1, 3)

if nombre_aleatoire in [1, 2]:
    print("\tPile !")
else:
    print("\tFace !")