# fonction puissance
def puissance(a, b):
    resultat = 1
    for _ in range(b):
        resultat *= a
    return resultat

base = int(input("Entrez la base : "))
exposant = int(input("Entrez l'exposant : "))
print(f"{base}^{exposant} = {puissance(base, exposant)}")
