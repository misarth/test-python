def nbre_iteration():
    fichier = open("TestFileJenkins.log",'r')
    texte = fichier.readlines()
    n=0
    for i in texte:
        if "Iteration" in i:
            n = n + 1
    fichier.close()
    return(n/2)

def test():
    assert (nbre_iteration()<4.0)
            
