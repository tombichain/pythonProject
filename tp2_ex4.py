BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400
nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue : "))

fromage *= nbConvives / BASE
eau *= nbConvives / BASE
ail *= nbConvives / BASE
pain *= nbConvives / BASE

print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut :")
print(f"- {fromage} gr de fromage")
print(f"- {eau} dl d'eau")
print(f"- {ail} gousse(s) d'ail")
print(f"- {pain} gr de pain")