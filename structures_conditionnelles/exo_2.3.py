# maximun de deux nombres 

a = int(input("entrez le premier nombre : "))
b = int(input("entrez le deuxieme nombre : "))

if a > b:
    print(f"le plus grand est : {a}")
elif b > a:
    print(f"le plus grand est : {b}")
else:
    print ("les deux nombres sont egaux.")