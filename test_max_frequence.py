def max_freq():
    fichier = open("TestFileJenkins.log",'r')
    texte = fichier.readlines()
    for i in texte:
        if "Maximum Frequency" in i:
            j= i.index(':')
            s=i[j+3:j+8]
    fichier.close()        
    return s

def test():
    assert (float(max_freq())<= 10.00)
            
