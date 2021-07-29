def nbre_ligne():
    fichier = open("TestFileJenkins.log",'r')
    texte = fichier.readlines()
    fichier.close()
    return len(texte)

def test():
    assert nbre_ligne()<= 100
   
        
                
                
        
