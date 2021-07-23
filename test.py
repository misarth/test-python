def Extract_data():
    fichier = open("TestFileJenkins.log",'r')
    texte = fichier.readlines()
    for i in texte:
        if "Number of LUTs" in i:
            j=i.index('%')
            s=i[j-5:j+1]
    fichier.close()
    return s

def test_function():
    assert f() == "80.00%"
