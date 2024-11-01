import math

def Entropie_Conjointe(p):
    calc = 0
    for i in range(len(p)):
        calc += p[i] * math.log2(p[i])
    return -calc

def Entroie_Marginel(p):
    calc = 0
    for i in range(len(p)):
        calc += p[i] * math.log2(p[i])
    return -calc

def Read_Source(i):
    s = []
    p = []
    while True:
        try:
            userInput = input(f"Entrer le caractere pour la source numero {i} ou arreter avec #: ")
            if(userInput == '#'):
                break
            s.append(userInput)
            userInput = input(f"Entrer la probabilité de ce caractere {i}: ")
            p.append(float(userInput))
            if(sum(p) == 1):
                break
            if(sum(p) > 1):
                print("La somme des probabilités ne doit pas dépasser 1")
                s.pop()
                p.pop()
        except:
            print("Erreur de saisie 2")
    return s, p

def Calcule_Proba_conjoint_Independant(p1,p2):
    p = []
    for i in range(len(p1)):
        for j in range(len(p2)):
            p.append(p1[i] * p2[j])
    return p


def Entrer_Proba_Dependant_Conditionelle(n,m):
    p = []
    for i in range(n):
        tmp = []
        for j in range(m):
            while True:
                userInput = input(f"Entrer la Probabilite de P(s{i}|s{j}): ")
                if( userInput == '#'):
                    break
                if( float(userInput) < 1):
                    tmp.append(float(userInput))
                    break
                print("entrer une proba > 1")
          
        p.append(tmp)
        print(p)

    return p  

def Calcule_Proba_Dependant_Conditionelle(p1,p2):
    p = []
    colums = list(zip(*p2))
    print(colums)
    for col_index, colum in enumerate(colums):
        for i in colum:
            p.append(p1[col_index] * i)
    return p    

def main():
    s1 = []
    s2 = []
    p1 = []
    p2 = []
    ps1s2 = []
    ps1Sachs2 = []
    ps2Sachs1 = []
    s1, p1 = Read_Source(1)
    s2, p2 = Read_Source(2)
    print(s1, p1)
    print(s2, p2)
    while True:
        try:
            userInput = input("Entrer 1 si les dexu sources sont independantes, 2 si non ou bien # pur sortire: ")
            if(userInput == '#'):
                break
            if(userInput == '1'):
                ps1s2 = Calcule_Proba_conjoint_Independant(p1,p2)
                print(ps1s2)
                break
            if(userInput == '2'):
               ps2Sachs1 = Entrer_Proba_Dependant_Conditionelle(len(p2), len(p1))
               print(ps2Sachs1)
               ps1s2 = Calcule_Proba_Dependant_Conditionelle(p1, ps2Sachs1 )
               print(ps1s2)
               break
        except Exception as e:
            print("Erreur de saisie 1", e)

    while True:
        try:
            userInput = input("Entrer 1 pour calculer l'entropie conjointe, 2 pour l'entropie conditionnelle ou bien # pour sortir: ")
            if(userInput == '#'):
                break
            if(userInput == '1'):
                print(Entropie_Conjointe(ps1s2))
                continue
            if( userInput == '2'):
                print(-Entroie_Marginel(p1) + Entropie_Conjointe(ps1s2))
            
        except:
            print("Erreur de saisie 3")           
         


if __name__ == "__main__":
    main()