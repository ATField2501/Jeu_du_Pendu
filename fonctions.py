#!/usr/bin/python2
# -*- coding: utf8 
# auteur: <atfield2501@gmail.com>

import random
import pickle
 

joueur="olaf"



# Chargement des scores sous forme d'un dictionnaire 
def Load():
    """
    Fonction de chargement des scores sous forme d'un dictionnaire


    """
    with open( 'scores', 'rb') as fichier:
        nirvana = pickle.Unpickler(fichier)
        dictio = nirvana.load()
    return dictio



# Verification de l'existence du joueur dans la base de données
def Verif(joueur):
    with open( 'scores', 'rb') as fichier:
        nirvana = pickle.Unpickler(fichier)
        dictio = nirvana.load()
    if joueur not in dictio.keys():
        createD(joueur, dictio)
    else:
        Affiche(joueur)
        return joueur
    return joueur
  

            
# Afficher score joueur 
def Affiche(joueur):
    with open( 'scores', 'rb') as fichier:
        nirvana = pickle.Unpickler(fichier)
        dictio = nirvana.load() 
        banshee = str(dictio[joueur])
        print "\n  * :: (;,,;) :: * \n"
        print  "\n  " + joueur + " possede un score de: " + banshee + " Pts\n"
    return joueur  



# Afficher tous les scores   
def AfficheS():
    with open( 'scores', 'rb') as fichier:
        nirvana = pickle.Unpickler(fichier)
        dictio = nirvana.load() 
        print "\n * Scores Du Pendu * \n"
        print"  ---------------- "                                  
        for keys in dictio.keys():
            banshee = str(dictio[keys])
            print " " +keys + " possede : " + banshee + " Pts"

    print"  ---------------- "  
    print "\n"                                
    return 



# Creation du joueur sous forme de dictionnaire
def createD(joueur, dictio):
    dictio[joueur]= 0
    with open('scores', 'wb') as fich:
        mon_pickler = pickle.Pickler(fich)
        mon_pickler.dump(dictio)
    Affiche(joueur)
    return joueur



# Fonction Sortie du Jeu
def Choix():
    try:
        suite = raw_input(" Sortir du jeu [Q] \n \n Afficher les Scores [A] \n \n Continuer le Jeu [C] \n \n  Votre choix :  ")
        suite = suite.upper()
    except:
        print"\n * Mauvaise entrée... Veillez recommencez * \n"

    if suite == "A":
        AfficheS()
        Choix()

    if suite == "C":
        Tentative()

    if suite == "Q":
        print"\n * A Bientôt * \n"      
        exit()
    else:
       Choix()
    return joueur  




# Identification du joueur
def Identif():
    try:
        joueur0 = raw_input("  Votre Nom : ")
        global joueur
        joueur = joueur0
    except:
        print"\n * Mauvaise entrée... Veillez recommencez * \n"
    Verif(joueur) 
    return joueur



# Recup lettre
def recupL(chaine):
    global essai
    essai = raw_input(chaine) 
    essai = essai.lower()
    if len(essai)>1 or not essai.isalpha():
        recupL(chaine)  
    else:
        return essai
  
# Récup mot
def recupM():
    with open( 'liste_mots.txt', 'r') as fichier:
        NumberOfLine = -1
        for line in fichier:
            NumberOfLine += 1 
    from random import randrange
    numero = random.randint(0,NumberOfLine)
    with open( 'liste_mots.txt', 'r') as fichier:
        global mot_mystere
        mot_mystere= fichier.readlines()[numero]
    return mot_mystere   


# Test Lettre
def testL(essai):
    try:
        if essai in mot_mystere:
            print "\n *  reussi  *\n"    
            #On releve la position pour inserrer la reponse dans le dictionaire avec cette valeure        
            position = mot_mystere.find(essai)
            neoChaine[position] = essai 
            dico[position] = essai
            print(neoChaine) 
        else:
            print "\n * raté! *\n"
            print(neoChaine)    
    except:
        # Dans le cas d'une validation de chaine vide, il ne faut pas lever d'erreur (pass) 
        pass   
    return neoChaine 


# Transformation du mot mystere
def transforme(mot_mystere):
    b=mot_mystere[0:-1]
    global mot_tmp
    mot_tmp = '     ' + len(b) * '*'

    return mot_tmp


  
# Tentative Joueur
def Tentative():
    print"  ---------------- "
    print("\n * Voici votre mot *\n")
    print"  ---------------- \n"

    recupM()
    
    transforme(mot_mystere)

    print transforme(mot_mystere)

    # dico des entrees du joueur
    global dico
    dico = {}
    global ma_liste
    ma_liste = []
    BBB =""    
    # Debut de la boucle pour les tentatives du joueur
    aa=0
    while aa < 9 and BBB != mot_mystere:
        bb = aa + 1
        chaine=" \n" + str(bb) + " Tentative:    "

        recupL(chaine)
       
        # Substitution des lettres du mot mystere par des *
        b=mot_mystere[0:-1]
        mot_tmp = len(b) * '*' 

        # Création d'une nouvelle chaine avec bitearray pour faire apparaitre les essais réussis   
        global neoChaine
        neoChaine= bytearray(mot_tmp)
        testL(essai)
        valeur = ""
        for valeur in dico.values():            
            print valeur,

            assemblage(dico, ma_liste, essai, BBB) 

        BBB = ''.join(ma_liste) + "\n" 

        Assenble(dico, ma_liste, essai, BBB)
        aa += 1
 

  
    print "\n  Le mot était: " + mot_mystere 
    print "\n  *    PENDU !!    *\n"
    Choix()
     

# Comparaison d'égalitée avec le mot_mystere
def Test(BBB, mot_mystere, joueur): 
    if BBB == mot_mystere:
        print "\n  Le mot était: " +mot_mystere 
        print "\n  * :: JACKPOT :: *\n"
        Calcul(joueur)
        Choix()


# Calcul du score
def Calcul(joueur):
    with open( 'scores', 'rb') as fich:
        nirvana = pickle.Unpickler(fich)
        dictio = nirvana.load()
    with open( 'scores', 'wb') as fich:
        nirvana = pickle.Pickler(fich)
        dictio[joueur] += 10
        nirvana.dump(dictio)
    Affiche(joueur)


def Assenble(dico, ma_liste, essai, BBB):
    ma_liste=[]
    for valeur in dico.values():
        ma_liste.append(valeur)
    BBB = ''.join(ma_liste) + "\n" 
    Test(BBB, mot_mystere, joueur)


# Assemblage mot_mystere
def assemblage(dico, ma_liste, essai, BBB):
    for valeur in dico.values():    
       if valeur == essai:
            # Si l'essai n'a pas déja était proposé
            if essai not in ma_liste:
                ma_liste.append(valeur)

    Test(BBB, mot_mystere, joueur)
   










