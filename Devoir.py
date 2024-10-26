import math

source = []
probalblities = []
inp = 0;
calcInput = 0;

while(inp != "#"):
    inp = input("Entrez Les nombres de la source et pour arreter tapez #: ")
    if(inp == '#'):
      break
    while True:
       try:
            prob = float(input("Entrez la probabilite de cet element (entre 0 et 1): "))
            if 0 <= prob <= 1:
                break
            else:
                print("La probabilite doit être entre 0 et 1. Veuillez réessayer.")
       except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")
    source.append(inp)
    probalblities.append(float(prob))
    if(sum(probalblities) == 1):
        break


        

print("La source est: ", source)
print("Les probabilites sont: ", probalblities)

while True:
    calcInput = input("Entrez 1 pour calculer la quantite, 2 pour cacluler l'entropie ou bien arreter avec #: ")
    if(calcInput == '#'):
        break
    if(calcInput == '2'):
        quantite = 0
        for i in range(len(probalblities)):
            quantite += probalblities[i] * math.log2(1/probalblities[i])
        print("L'entropie est: ", quantite)
    else:
        if(calcInput == '1'):
            while True:
                quantElement = input("Entrez l'element dont vous voulez calculer la quantite: ")
                if(quantElement in source):
                    index = source.index(quantElement)
                    print("La quantite de ", quantElement, " est: ", math.log2(1/probalblities[index]))
                    break
                else:
                    print("L'element n'existe pas dans la source. Veuillez réessayer.")
