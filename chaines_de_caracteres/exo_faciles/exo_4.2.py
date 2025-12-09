# compteur de voyelles 

chaine = input("entrez une chaine : ")

voyelles = "aeiouyAEUOIY"
compteur = 0

for lettre in chaine:
    if lettre in voyelles:
        compteur += 1

        print(f"nombre de voyelles :", {compteur})