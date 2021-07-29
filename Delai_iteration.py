def delai():
    fichier = open("TestFileJenkins.log",'r')
    texte = fichier.readlines()
    L=[]
    for i in texte:
        if "Iteration" in i:
            if "ended" in i:
                j= i.index('(')
                L.append(i[j+1:j+3])
    print(L)
    return L

def verification():
    i=delai()
    assert 4 == 4
   
        
                
                
        
