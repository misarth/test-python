#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""date.py: récupération de la date à partir du fichier TestFileJenkins.log et tester le résultat """

__author__ = "Sarah Gharbi"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Sarah Gharbi"
__email__ = "gharbisarah186@gmail.com"
__status__ = "Production"

####################################################################################################################


def date():                                    #fonction pour récupérer la date   
    fichier = open("TestFileJenkins.log",'r')  #ouverture du fichier
    texte = fichier.readlines()                #récupération des lignes de fichier dans la liste texte
    d=texte[-1]
    l= d[d.index(':')+1:]                      #récupération de la date
    date=l.split()
    fichier.close()                            #fermeture du fichier
    return date   

def test():                                    #fonction test pour tester la format de la date
    d=date()
    assert (d[0] in ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])                      
    assert (d[1] in ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
    assert (0<int(d[2])<32)  
