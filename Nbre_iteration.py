def nbre_iteration():
    fichier = open("TestFileJenkins.log",'r')
    texte = fichier.readlines()
    n=0
    for i in texte:
        if "Iteration" in i:
            n = n + 1
    return(int(n/2))

nbre_iteration()

def verification():
    assert nbre_iteration() <= 3
            
