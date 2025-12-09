# foction est pair 

def est_pair(n):
    return n % 2 == 0
nombre = int(input("Entrez un nombre : "))
if est_pair(nombre):
    print("Le nombre est pair.")
else:
    print("Le nombre est impair.")
