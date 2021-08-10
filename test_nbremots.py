#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""nbre_de_mots.py: calculer le nombre des mots du fichier TestFileJenkins.log et tester le résultat """

__author__ = "Sarah Gharbi"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Sarah Gharbi"
__email__ = "gharbisarah186@gmail.com"
__status__ = "Production"

####################################################################################################################


def nbre():                                  #fonction pour calculer le nombre des mots   
    fichier = open("TestFileJenkins.log",'r')#ouverture du fichier
    texte = fichier.read()                   #récupération du contenu du fichier
    L=texte.split()                          #diviser le contenu du fichier en des mots séparés
    fichier.close()                          #fermeture du fichier
    return len(L)   

def test():                                  #fonction test pour tester le nombre des mots
    assert (nbre()<1001)
      
