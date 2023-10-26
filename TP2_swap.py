a=int(input("Entrez la premiere  valeur : "))
b=int(input("Entrez la deuxieme  valeur : "))
c=int(input("Entrez la troisieme valeur : "))

print("Les valeurs entrees sont : a = " , a , ", b = " , b , " et c = " , c)
print("Permutation: a ==> b, b ==> c, c ==> a")
"""      *******************************************
         * Completez le programme a partir d'ici.
         *******************************************
"""
a = a + c
c = a - c
a = a - c
b = b + c
c = b - c
b = b - c


"""     *******************************************
         * Ne rien modifier apres cette ligne.
         *******************************************
"""

print("Les valeurs permutees sont : a = " , a , ", b = " , b , " et c = " , c)