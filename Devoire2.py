import math

s1 = []
s2 = []
p1 = []
p2 = []

sinput = 0

def get_input(s, p,i):
    while True:
        sinput = input("Entrez Les nombres de la source "+ str(i) +  " et pour arreter tapez #: ")
        if(sinput == '#'):
            break
        while True:
                try:
                    prob = float(input("Entrez la probabilite de cet element (entre 0 et 1): "))
                    print(sum(p) + prob)
                    if (prob + sum(p) <= 1 and 0 <= prob <= 1):
                        break
                    else:
                        print("La probabilite doit être entre 0 et 1. Veuillez réessayer et la somme des probabilites doivent être == 1.")
                except ValueError:
                    print("Entrée invalide. Veuillez entrer un nombre.")
        s.append(sinput)
        p.append(float(prob))
        if(sum(p) == 1):
            return True
    return False

get_input(s1, p1, 1)
get_input(s2, p2, 2)

print("La source 1 est: ", s1)
print("Les probabilites sont: ", p1)
print("La source 2 est: ", s2)
print("Les probabilites sont: ", p2)