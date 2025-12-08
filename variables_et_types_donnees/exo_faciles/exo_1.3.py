#calcul de moyenne 
n = 3 
somme = 0
for a in range (1, n + 1):
    note = float(input(f"note {i} : "))
    somme += note

 moyenne = somme / n

print(f"la moyenne est : {moyenne:.2f}")    