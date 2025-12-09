# invertion de chaine 

chaine = input("entre une chaine :")
chaine_inversee = ""
for i in range (len(chaine) -1, -1, -1):
    chaine_inversee += chaine[i]
    
    print(f"chaine originale : {chaine} ")
    print(f"chaine inversee : {chaine_inversee}")