def délai_itération():
    fichier = open("TestFileJenkins.log",'r')
    texte = fichier.readlines()
    L=[]
    for i in texte:
        if "Iteration" in texte:
            if "ended" in i:
                j= i.index('(')
                L.append(i[j+1:j+3])
    print(L)
    return L

def verification():
    for i in délai_itération():
        assert i<=20
                
        
