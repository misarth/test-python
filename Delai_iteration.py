def delai_iteration():
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
    for i in delai_iteration():
        assert int(i)<=20
                
                
        
