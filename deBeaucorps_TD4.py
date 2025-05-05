# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 00:20:57 2022

@author: Etienne de Beaucorps P2A
"""

from random import randrange
from random import randint
import pygame
from os import chdir

#=============================================================================

#1.1
def position_initiale()->list:
    ''' 
    Renvoie la position initiale du jeu du puissance 4 sous forme de liste
    de listes de 0 composé de 6 lignes et 7 colonnes 
    '''
    
    L=[[0 for i in range(7)] for i in range(6)]
    
    return L

# print('\n\n-------------------------------\n')
# print('Partie 1 : Construction du jeu  ')
# print('\n-------------------------------\n')

grille_init=position_initiale()

# print('Soit grille_init une grille de jeu initialisée par position_initiale()',
#       ':\n')
# for k in range(6):
#     print(grille_init[k])
# print('\n')

#=============================================================================

#1.2
def affichage(grille:list)->str:
    '''
    Prend en argument une grille et renvoie sa représentation sous forme 
    de str avec un '.' pour dire que la place est libre, un 'o' pour 
    représenter le joueur 2 et un 'x' pour représenter  le joueur 1
    '''
    F=''
    for i in range(6):
        L=''
        X='.'
        Y='o'
        Z='x'
        for j in range(0,len(grille[0])):
            if grille[5-i][j]==0:
                L=L+X
            if grille[5-i][j]==2:
                L=L+Y
            if grille[5-i][j]==1:
                L=L+Z
                
            #permet une meilleure lecture    
            L=L+' '
        F+='\n'+L
        
    return print(F)

# print('Affichage d une grille à l etat initial : ')
# affichage(grille_init)
# print('\n')

Grille0=[[0, 1, 2, 1, 2, 2, 2],
         [0, 0, 0, 2, 1, 1, 1],
         [0, 0, 0, 2, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]

# print('Soit Grille0 une grille réellement atteignable : \n')
# for k in range(len(Grille0)):
#     print(Grille0[k])
    
# print('\nSon affichage est : \n')
# affichage(Grille0)

#=============================================================================

#1.3
def coups_possibles(grille:list)->list:
    ''' 
    Prend en argument une grille de jeu réellement atteignable nommé grille
    en tant que liste de listes et renvoie la liste des coups possible
    sous forme d'une liste de tuple a double indice
    '''
    
    #initialisation des coups possibles
    L=[(5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6)]
    
    #recherche des coups possibles :
    for i in range(6):
        for j in range(7):
            if grille[i][j]==0 and L[j][0]>i:
                L[j]=(i,j)
                
            #recherche des coups impossible
            if grille[i][j]!=0 and i==5:
                L[j]=None
                
    #élémination des coups impossible
    L=[x for x in L if x!=None]
        
    return L

# print('\nles coups possibles de grille_init sont :\n')
# print(coups_possibles(grille_init))

# print('\nLes coups possibles pour grille0 sont :\n')
# print(coups_possibles(Grille0),'\n')

Grille1=[[1, 1, 2, 2, 2, 1, 2],
         [2, 1, 1, 1, 2, 1, 1],
         [3, 2, 2, 2, 1, 2, 2],
         [2, 1, 1, 2, 2, 2, 1],
         [1, 2, 2, 1, 1, 1, 2],
         [2, 1, 1, 2, 1, 1, 2]]

# print('Soit Grille1 la grille d un partie nulle : \n')
# for k in range(len(Grille1)):
#     print(Grille1[k])

# print('\nLes coups possibles pour Grille1 sont :\n')
# print('(Aucun coup n est possible donc on doit avoir une liste vide)\n')
# print(coups_possibles(Grille1),'\n')

#=============================================================================

#1.4
def est_gagnant(grille:list,coup:tuple,joueur:int)->bool:
    ''' 
    Prend en argument une grille de jeu réellement ateignable sous forme de 
    liste de listes, le tuple représentant le coup joué qui doit être possible,
    un entier joueur représentant le joueur 1 ou 2. Renvoie True si le coup est
    gagnant pour le joueur joueur et False sinon
    '''
    assert coup in coups_possibles(grille), f'{coup}, {grille}'

    #verification horizontale
    L=[]
    for j in range(coup[1]-3,coup[1]+4):
        if j>-1 and j<7:
            if grille[coup[0]][j]==joueur and j!=coup[1]:
                L.append(grille[coup[0]][j])
                if len(L)==3:

                    return True
            elif j!=coup[1]:
                L=[]
             
    #verification verticale
    L=[]
    for i in range(coup[0]-3,coup[0]+4):
        if i>-1 and i<6:
            if grille[i][coup[1]]==joueur and i!=coup[0]:
                L.append(grille[i][coup[1]])
                if len(L)==3:

                    return True
            elif i!=coup[0]:
                L=[]
          
    #verification diagonale haut hauche vers bas droite
    L=[]
    for k in range(7):
        i=coup[0]-3+k
        j=coup[1]-3+k
        if i>-1 and j>-1 and i<6 and j<7:
            #on peut simplifier en ne mettant la condi que sur i ou j
            if grille[i][j]==joueur and i!=coup[0] and j!=coup[1]:
                L.append([(i,j)])
                if len(L)==3:

                    return True
            elif i!=coup[0] and j!=coup[1]:
                L=[]

    #verification diagonale bas gauche vers haut droite
    L=[]
    for k in range(7):
        i=coup[0]+3-k
        j=coup[1]-3+k
        if i>-1 and j>-1 and i<6 and j<7:
            #on peut simplifier en ne mettant la condi que sur i ou j
            if grille[i][j]==joueur and i!=coup[0] and j!=coup[1]:
                L.append([(i,j)])
                if len(L)==3:

                    return True
            elif i!=coup[0] and j!=coup[1]:
                L=[] 
    
    return False

Grille2=[[1, 1, 1, 0, 2, 2, 2],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]] 

# print('Soit Grille2 une grille réellement atteignable, coup gagnant en [0][3]',
#       'pour le joueur 1 et le joueur 2 mais coup au joueur 1\n')
# for k in range(len(Grille2)):
#     print(Grille2[k])
    
# print(f'\nest_gagnant(Grille2,(3,3),1) : \n {est_gagnant(Grille2,(0,3),1)}')
# print(f'\nest_gagnant(Grille2,(3,3),2) : \n {est_gagnant(Grille2,(0,3),2)}')

# print('\nPrenons un coup possible dans la grille initiale donc forcément non',
#       'gagnant grille_init et (0,0)\n est_gagnant(grille_init,(0,2),1) :\n',
#       est_gagnant(grille_init,(0,2),1),'\n')
# print('De même si on prend le joueur 2 :\nest_gagnant(grille_init,(0,2),2)\n',
#       est_gagnant(grille_init,(0,0),2),'\n')

#=============================================================================

#1.5.a
def puissance4_aleatoire()->tuple:
    '''
    Sans argument, simule une partie et renvoie la grille finale sous forme
    de liste de listes et un entier correspondant au résultat de la partie,
    0 pour nulle, 1 victoire joueur 1 et 2 victoire joueur 2
    '''
    
    #initialisation des variables
    partie_finie=False
    grille=position_initiale()
    j=0
    
    while partie_finie==False:
        
        #permet de retracer le joueur via la parité de j
        j+=1
        
        #recherche du coup allant être joué
        liste_possible=coups_possibles(grille)
        if len(liste_possible)==0:
            return(grille,0)
        ind_joue=randrange(len(liste_possible))
        coup_joue=liste_possible[ind_joue]

        #cas d'un coup hors de la grille 
        while grille[coup_joue[0]][coup_joue[1]]==1 or grille[coup_joue[0]][coup_joue[1]]==2:
            
            
            #cas d'un match nul
            if len(liste_possible)==0:
                return (grille,0)
            
            ind_joue=randrange(len(liste_possible))
            print(ind_joue)
            coup_joue=liste_possible[ind_joue]

        
        #cas d'un coup non gagnant pour le joueur 1
        if j%2==1 and est_gagnant(grille,coup_joue,1)==False:

            grille[coup_joue[0]][coup_joue[1]]=1
            
        #cas d'un coup non gagnant pour le joueur 2
        elif j%2==0 and est_gagnant(grille,coup_joue,2)==False:

            grille[coup_joue[0]][coup_joue[1]]=2
        
        #cas d'un coup gagnant pour le joueur 2
        elif j%2==0 and est_gagnant(grille,coup_joue,2)==True:
            
            grille[coup_joue[0]][coup_joue[1]]=2
            return (grille,2)
        
        #cas d'un coup gagnant pour le joueur 1
        elif j%2==1 and est_gagnant(grille,coup_joue,1)==True:
            
            grille[coup_joue[0]][coup_joue[1]]=1
            return (grille,1)
        
# print('Exemple 1 de partie aléatoire générée : \n')
# Grille3=puissance4_aleatoire()
# print(f'Le gagnant est : {Grille3[1]}\n\n et la partie est : \n')
# for k in range(len(Grille3[0])):
#     print(Grille3[0][k])
    
# print('\nExemple 2 de partie aléatoire générée : \n')
# Grille3=puissance4_aleatoire()
# print(f'Le gagnant est : {Grille3[1]}\n\n et la partie est : \n')
# for k in range(len(Grille3[0])):
#     print(Grille3[0][k])

#=============================================================================

#1.5.b                
def taux_victoire_puissance(N:int)->tuple:
    ''' 
    prend en argument un entier naturel non nul N, simule N parties aléatoires
    via la fonction puissance4_aleatoire() et renvoie un tuple à 3 éléments
    donnant le quotient par N du nombre de parties par le joueur 1, du nombre
    de parties gagnées par le joueur 2, du nombre de parties nulles
    '''
    
    #initialisation des compteurs
    j1=0
    j2=0
    j0=0
    
    #construction de j1,j2 et j0
    for k in range(N):
        res=puissance4_aleatoire()
        if res[1]==1:
            j1+=1
        elif res[1]==2:
            j2+=1
        elif res[1]==0:
            j0+=1
            
    return(j1/N,j2/N,j0/N)

# print('\nRésultat approximé de taux_victoire_puissance(N) pour N= 1 000 000 :')
# print('\njoueur 1 : p(j1)=0,555')
# print('joueur 2 : p(j2)=0,442')
# print('partie nulle : p(j0)=0,0025\n')
# print('On a donc 0,555+0,442+0,0025 = 0,9995 ~ 1')
# print('Cela m a pris 1H et 20 minutes au alentour de 10 000 cela devient long')

#=============================================================================

#2.1
#code utilisé pour construire la liste des alignements vu que 69 listes de 
#4 paires parait un peu long à écrire
'''
#initialisation de la liste
X=[]
alignements=X

#Construction colonne
for k in range(4):
    for i in range(6):
        D=[]
        for j in range(4):
            D.append((i,j+k))
        X.append(D)

#Construction ligne
for k in range(3):
    for i in range(7):
        D=[]
        for j in range(4):
            D.append((j+k,i))
        X.append(D)

#construction diagonale n°1

for k in range(3):
    for l in range(4):
        i=k
        j=l
        D=[]
        for _ in range(4):
            D.append((i,j))
            i+=1
            j+=1
        X.append(D)

#construction diagonale n°2
for k in range(3):
    for l in range(4):
        i=k
        j=6-l
        D=[]
        for _ in range(4):
            D.append((i,j))
            i+=1
            j-=1
        X.append(D)
'''

alignements=[[(0, 0), (0, 1), (0, 2), (0, 3)],
             [(1, 0), (1, 1), (1, 2), (1, 3)],
             [(2, 0), (2, 1), (2, 2), (2, 3)],
             [(3, 0), (3, 1), (3, 2), (3, 3)],
             [(4, 0), (4, 1), (4, 2), (4, 3)],
             [(5, 0), (5, 1), (5, 2), (5, 3)],
             [(0, 1), (0, 2), (0, 3), (0, 4)],
             [(1, 1), (1, 2), (1, 3), (1, 4)],
             [(2, 1), (2, 2), (2, 3), (2, 4)],
             [(3, 1), (3, 2), (3, 3), (3, 4)],
             [(4, 1), (4, 2), (4, 3), (4, 4)],
             [(5, 1), (5, 2), (5, 3), (5, 4)],
             [(0, 2), (0, 3), (0, 4), (0, 5)],
             [(1, 2), (1, 3), (1, 4), (1, 5)],
             [(2, 2), (2, 3), (2, 4), (2, 5)],
             [(3, 2), (3, 3), (3, 4), (3, 5)],
             [(4, 2), (4, 3), (4, 4), (4, 5)],
             [(5, 2), (5, 3), (5, 4), (5, 5)],
             [(0, 3), (0, 4), (0, 5), (0, 6)],
             [(1, 3), (1, 4), (1, 5), (1, 6)],
             [(2, 3), (2, 4), (2, 5), (2, 6)],
             [(3, 3), (3, 4), (3, 5), (3, 6)],
             [(4, 3), (4, 4), (4, 5), (4, 6)],
             [(5, 3), (5, 4), (5, 5), (5, 6)],
             [(0, 0), (1, 0), (2, 0), (3, 0)],
             [(0, 1), (1, 1), (2, 1), (3, 1)],
             [(0, 2), (1, 2), (2, 2), (3, 2)],
             [(0, 3), (1, 3), (2, 3), (3, 3)],
             [(0, 4), (1, 4), (2, 4), (3, 4)],
             [(0, 5), (1, 5), (2, 5), (3, 5)],
             [(0, 6), (1, 6), (2, 6), (3, 6)],
             [(1, 0), (2, 0), (3, 0), (4, 0)],
             [(1, 1), (2, 1), (3, 1), (4, 1)],
             [(1, 2), (2, 2), (3, 2), (4, 2)],
             [(1, 3), (2, 3), (3, 3), (4, 3)],
             [(1, 4), (2, 4), (3, 4), (4, 4)],
             [(1, 5), (2, 5), (3, 5), (4, 5)],
             [(1, 6), (2, 6), (3, 6), (4, 6)],
             [(2, 0), (3, 0), (4, 0), (5, 0)],
             [(2, 1), (3, 1), (4, 1), (5, 1)],
             [(2, 2), (3, 2), (4, 2), (5, 2)],
             [(2, 3), (3, 3), (4, 3), (5, 3)],
             [(2, 4), (3, 4), (4, 4), (5, 4)],
             [(2, 5), (3, 5), (4, 5), (5, 5)],
             [(2, 6), (3, 6), (4, 6), (5, 6)],
             [(0, 0), (1, 1), (2, 2), (3, 3)],
             [(0, 1), (1, 2), (2, 3), (3, 4)],
             [(0, 2), (1, 3), (2, 4), (3, 5)],
             [(0, 3), (1, 4), (2, 5), (3, 6)],
             [(1, 0), (2, 1), (3, 2), (4, 3)],
             [(1, 1), (2, 2), (3, 3), (4, 4)],
             [(1, 2), (2, 3), (3, 4), (4, 5)],
             [(1, 3), (2, 4), (3, 5), (4, 6)],
             [(2, 0), (3, 1), (4, 2), (5, 3)],
             [(2, 1), (3, 2), (4, 3), (5, 4)],
             [(2, 2), (3, 3), (4, 4), (5, 5)],
             [(2, 3), (3, 4), (4, 5), (5, 6)],
             [(0, 6), (1, 5), (2, 4), (3, 3)],
             [(0, 5), (1, 4), (2, 3), (3, 2)],
             [(0, 4), (1, 3), (2, 2), (3, 1)],
             [(0, 3), (1, 2), (2, 1), (3, 0)],
             [(1, 6), (2, 5), (3, 4), (4, 3)],
             [(1, 5), (2, 4), (3, 3), (4, 2)],
             [(1, 4), (2, 3), (3, 2), (4, 1)],
             [(1, 3), (2, 2), (3, 1), (4, 0)],
             [(2, 6), (3, 5), (4, 4), (5, 3)],
             [(2, 5), (3, 4), (4, 3), (5, 2)],
             [(2, 4), (3, 3), (4, 2), (5, 1)],
             [(2, 3), (3, 2), (4, 1), (5, 0)]]

# print('\n-----------------------------------------------------------------\n')
# print(''' Partie 2 : Implémentation du minimax et 1ère fonction d'utilité''')
# print('\n-----------------------------------------------------------------\n')

# print('\nCalcul du nombre d alignements total :\n')
# print('-Pour chaque ligne on a 4 possibilités d alignement horizontal-> ',
#       '6*4=24 donc 24 alignements horizontal\n')
# print('-Pour chaque colonne on a 3 possibilités d alignement vertical-> ',
#       '3*7=21 donc 21 alignements vertical\n')
# print('-Pour les alignements diagonale dirigé du haut gauche vers bas droite',
#       'on dispose de 4 colonnes pour 3 lignes donc 4*3=12`\n')
# print('-De meme pour les alignements diagonaux de haut droite vers bas gauche')
# print('\n->On trouve donc 21+ 24 +12 +12 = 69 alignements possible\n')

# assert len(alignements)==69

# print('taille de la liste alignements :  ',len(alignements),'\n')

#============================================================================

#2.2
def utilité(G:list,k:int,w:list)->int:
    '''
    Prend en argument G une grille de jeu sous forme de liste de listes, k un 
    entier (1,2) représentant le joueur et w une fonction de poids sous forme
        de liste. Renvoie la valeur de l'utilité U_k pour le joueur k
    '''
    
    #initialisation de la valeur d'utilité
    U_k=0
    
    #test pour tous les alignements possibles
    for i in range(69):
        L=[]
        #recherche des n_k(A) et n_(3-k)(A)
        for l in range(4):
            if G[alignements[i][l][0]][alignements[i][l][1]]==k:
                L.append(1)
                
            elif G[alignements[i][l][0]][alignements[i][l][1]]==3-k:
                L.append(-1)

        #ajout à la valeur d'utilité selon la fonction de poids :
            
        #cas de n_k(A) et n_(3-k)(A) non tous deux nuls
        if -1 in L and 1 in L:
            None
        
        else:
            U_k+= w[L.count(1)]-w[L.count(-1)]
            
    return U_k

w0=[0,1,5,10,float('inf')]
# print(f' Soit w0 la fonction de poids suivante :\n\n w0 = {w0} \n')

Grille3=[[0, 0, 1, 1, 2, 1, 2],
         [0, 0, 2, 1, 1, 0, 0],
         [0, 0, 2, 0, 1, 0, 0],
         [0, 0, 2, 0, 0, 0, 0],
         [0, 0, 2, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]    

# print(' soit Grille3 une grille réellement atteignable avec une victoire',
#       'pour le joueur 2 sur la colonne 2\n' )
# for k in range(len(Grille3)):
#     print(Grille3[k])
# print('\n')

# print("L'utilité de Grille3 pour le joueur 2 par w0 est :\n", 
#       utilité(Grille3,2,w0))

# print("\nL'utilité de Grille3 pour le joueur 1 par w0 est :\n",
#       utilité(Grille3,1,w0),'\n')

Grille4=[[1, 2, 1, 2, 1, 2, 2],
         [1, 2, 0, 1, 1, 0, 1],
         [2, 2, 0, 2, 2, 0, 1],
         [1, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 2],
         [0, 0, 0, 0, 0, 0, 0]]

# print('Soit Grille4 une grille réellement atteignable avec coup gagnant',
#       'pour le joueur 1 en [1][5] mais beaucoup d alignements avantageux',
#       'pour le joueur 2\n')

# for k in range(len(Grille4)):
#     print(Grille4[k])
# print('\n')

# print("l'utilité de Grille4 pour le joueur 2 par w0 est :\n",
#       utilité(Grille4,2,w0))
# print("l'utilité de Grille4 pour le joueur 1 par w0 est :\n",
#      utilité(Grille4,1,w0))
# print('\nEn prenant une fonction de poids qui avantage les alignements de 3',
#       'pions, on doit donc trouver une valeur plus importante dans les 2 cas!')
# print('Je reprend la fonction de poids w0 en changeant le 10 en 50')

w0_2=[0,1,5,50,float('inf')]
# print('On obtient w0_2 : ',w0_2,'\n')

# print("l'utilité de Grille4 pour le joueur 2 par w0_2 est :\n",
#      utilité(Grille4,2,w0_2))
# print("l'utilité de Grille4 pour le joueur 1 par w0_2 est :\n",
#      utilité(Grille4,1,w0_2))

#=============================================================================

#refaire comme L1 mais en version max max pour avoir l'utilité maximale 
#souvent completement con

#prob sur les feuilles (prend par forcément le bon joueur en compte)
#2.3
def minmax(grille:list,joueur:int,poids:list,p:int)->tuple:
    '''
    Prend en argument grille une grille de jeu sous forme de liste de listes,
    joueur un entier 1 ou 2 représentant le joueur, poids une liste de poids
    de taille 5 et p un entier représentant la profondeur d'analyse.
    Renvoie l'utilité maximale à p coups U_k (indice de puissance p)
    '''

    #initialisation
    U_j_0=utilité(grille,joueur,poids)
    liste_possible=coups_possibles(grille)
    
    # 2 cas d'une partie déjà finie
        #Partie gagnée par 1 ou 2
    if U_j_0==poids[4] or U_j_0==-poids[4]:
        return (U_j_0,None)
    
        #Partie nulle
    if len(liste_possible)==0:
        return(0,None)
    
    #compteur permettant de trouver qui joue le coup
    i=0
    for k in range(len(grille)):
        i+=grille[k].count(1)
        i+=grille[k].count(2)
    
    #cas des feuilles
    for s in liste_possible:
        if est_gagnant(grille,s,joueur)==True and i%2!=joueur%2:
            return (float('inf'),s)
            
        elif est_gagnant(grille,s,3-joueur)==True and i%2==joueur%2:
            return (-float('inf'),s)

    #cas d'une profondeur 0
    if p==0:
        return (U_j_0,None)
    
    
    #Traitement du minmax pour chaque coup :
    
    L1=[]
    #cas joueur=1 et le joueur 2 joue
    if i%2==1 and joueur==1:
        for s in liste_possible:
            grille[s[0]][s[1]]=2
            L1.append(minmax(grille,joueur,poids,p-1)[0])
            
            if  L1!=[]:
                if min(L1)==L1[-1]:
                    S1=s
            else:
                S1=None

            grille[s[0]][s[1]]=0
            
        return (min(L1),S1)
    
    #cas joueur=2 et le joueur 2 joue
    elif i%2==1 and joueur==2:
        for s in liste_possible:
            grille[s[0]][s[1]]=2
            L1.append(minmax(grille,joueur,poids,p-1)[0])
            
            if  L1!=[]:
                if max(L1)==L1[-1]:
                    S1=s
            else:
                S1=None
                
            grille[s[0]][s[1]]=0
            
        return (max(L1),S1)
    
    #cas joueur=1 et le joueur 1 joue
    elif i%2==0 and joueur==1:
        for s in liste_possible:
            grille[s[0]][s[1]]=1
            L1.append(minmax(grille,joueur,poids,p-1)[0])
            
            if  L1!=[]:
                if max(L1)==L1[-1]:
                    S1=s
            else:
                S1=None

            grille[s[0]][s[1]]=0
       
        return (max(L1),S1)
    
    #cas joueur=2 et le joueur 1 joue
    elif i%2==0 and joueur==2:
        for s in liste_possible:
            grille[s[0]][s[1]]=1
            L1.append(minmax(grille,joueur,poids,p-1)[0])
            
            if  L1!=[]:
                if min(L1)==L1[-1]:
                    S1=s
            
            else:
                S1=None
                
            grille[s[0]][s[1]]=0  
            
        return (min(L1),S1)

#=============================================================================

#2.4
def strategie_minimax(grille:list,joueur:int,poids:list,p:int)->tuple:
    '''     
    Prend en arguments un entier joueur égal à 1 ou 2, poids une liste de 5 
    floats et p un entier naturel, renvoie un dictionnaire qui à comme clés
    les positions post du jeu, réputées appertenant au joueur concerné et 
    pour valeur associée à une telle position posrt un coup possible à partir
    de posn et qui est préconisée par la stratégie du minmax à profondeur 
    limitée p.
    '''
    
    #initialisation du dictionnaire
    
    '''
    grille=position_initiale()
    
    for k in range(25):
        
        U=utilité(grille,joueur,poids)
        
        liste_possible=coups_possibles(grille)
        if len(liste_possible)==0 or U==poids[4] or U==-poids[4]:
            break
        
        if joueur == 1:
            
            J1=minmax(grille,1,poids,p)
            t_grille=[]
            for k in range(5):
                t_grille.extend(grille[k])
            dic[tuple(t_grille)]=J1[1]
            print(J1)
            print(grille)
            grille[J1[1][0]][J1[1][1]]=1
            
            liste_possible=coups_possibles(grille)
            coup_joue=liste_possible[randrange(len(liste_possible))]
            grille[coup_joue[0]][coup_joue[1]]=2
            
        if joueur == 2:
            None
      '''
    return minmax(grille,joueur,poids,p)[1]



#=============================================================================

#strategie pour faire des tests

def strategie_1(grille:list,joueur=1,a=1,b=1)->tuple:
    ''' 
    Stratégie pour le joueur 1 qui joue aléatoirement s'il n'a aucun coup 
    gagnant ( n'utilise pas poids et p)
    '''
    
    liste_possible=coups_possibles(grille)
    L=[]
    for s in liste_possible:
        if est_gagnant(grille,s,1):
            return s
        else:
            L.append(s)
    return L[randrange(len(L))]
            
def strategie_2(grille:list,joueur=2,a=1,b=1)->tuple:
    ''' 
    Stratégie pour le joueur 2 qui joue aléatoirement s'il n'a aucun coup 
    gagnant ( n'utilise pas a et b)
    '''
    
    liste_possible=coups_possibles(grille)
    L=[]
    for s in liste_possible:
        if est_gagnant(grille,s,2):
            return s
        else:
            L.append(s)
    return L[randrange(len(L))]

#2.5
def partie(strategie_1:tuple,strategie_2:tuple,Affichage=False)->tuple:
    ''' 
    Prend en argument 2 fonctions pythons qui représente une stratégie pour
    le joueur 1 et 2 respectivement et retourne la grille obtenue à la fin
    de la partie réalisée avec un entier désignant le joueur gagnant. Si le 
    bool optionnel Affichage est 'true', à chaque coup joué, l'affichage de la 
    partie sera renvoyée.
    '''
    
    #initilialisation
    grille=position_initiale()
    liste_possible=coups_possibles(grille)
    
    #boucle 'inifinie' pour jouer chacun son tour, (terminaison obligatoire)
    while True:
        
        #cas d'un match nul
        liste_possible=coups_possibles(grille)
        if len(liste_possible)==0:
            return (grille,0)
            
        #joueur 1 joue:
        J1=strategie_1(grille,1)
        #cas d'un coup gagnant joueur 1
        if est_gagnant(grille,J1,1):
            grille[J1[0]][J1[1]]=1
            if Affichage==True:
                affichage(grille)
            return (grille,1)
        
        #cas si le coup n'est pas gagnant pour le joueur 1
        else:
            grille[J1[0]][J1[1]]=1
        
        #affichage
        if Affichage==True:
            affichage(grille)
       
        #joueur 2 joue :
        J2=strategie_2(grille,2)
        #cas d'un coup gagnant joueur 2
        if est_gagnant(grille, J2,2):
            grille[J2[0]][J2[1]]=2
            if Affichage==True:
                affichage(grille)
            return (grille,2)
        
        #cas si le coup n'est pas gagnant pour le joueur 2
        else:
            grille[J2[0]][J2[1]]=2
        
        #affichage
        if Affichage==True:
            affichage(grille)

#=============================================================================

#2.6.a
w=[0,1,10,100,float('inf')]
def strategie_minimax_w_1(grille:list,joueur:list,poids=w,p=1):
    return minmax(grille,joueur,poids,p)[1]
def strategie_minimax_w_2(grille:list,joueur:list,poids=w,p=2):
    return minmax(grille,joueur,poids,p)[1]
def strategie_minimax_w_3(grille:list,joueur:list,poids=w,p=3):
    return minmax(grille,joueur,poids,p)[1]
def strategie_minimax_w_4(grille:list,joueur:list,poids=w,p=4):
    return minmax(grille,joueur,poids,p)[1]

# #p=1
# print(partie(strategie_minimax_w_1,strategie_minimax_w_1)[1])
# print(partie(strategie_minimax_w_1,strategie_minimax_w_2)[1])
# print(partie(strategie_minimax_w_1,strategie_minimax_w_3)[1])
# print(partie(strategie_minimax_w_1,strategie_minimax_w_4)[1])

# #p=2
# print(partie(strategie_minimax_w_2,strategie_minimax_w_1)[1])
# print(partie(strategie_minimax_w_2,strategie_minimax_w_2)[1])
# print(partie(strategie_minimax_w_2,strategie_minimax_w_3)[1])
# print(partie(strategie_minimax_w_2,strategie_minimax_w_4)[1])

# #p=3
# print(partie(strategie_minimax_w_3,strategie_minimax_w_1)[1])
# print(partie(strategie_minimax_w_3,strategie_minimax_w_2)[1])
# print(partie(strategie_minimax_w_3,strategie_minimax_w_3)[1])
# print(partie(strategie_minimax_w_3,strategie_minimax_w_4)[1])

# #p=4
# print(partie(strategie_minimax_w_4,strategie_minimax_w_1)[1])
# print(partie(strategie_minimax_w_4,strategie_minimax_w_2)[1])
# print(partie(strategie_minimax_w_4,strategie_minimax_w_3)[1])
# print(partie(strategie_minimax_w_4,strategie_minimax_w_4)[1])

# print('\n |    Joueur 1|  p=1  | p=2  | p=3  | p=4  |\n',
#       '|Joueur 2    |       |      |      |      |\n',
#       '|------------|-------|------|------|------|\n',
#       '|      p=1   |   1   |  1   |  1   |  1   |\n',
#       '|      p=2   |   1   |  1   |  1   |  1   |\n',
#       '|      p=3   |   2   |  1   |  1   |  2   |\n',
#       '|      p=4   |   1   |  2   |  2   |  1   |')

# print('\n\n')

#=============================================================================

#2.6.b
w1 = [0, 1, 10, 1000, float('inf')]
w2 = [0, 1, 10, 100, float('inf')]
w3 = [0, 1, 10, 30, float('inf')]
w4 = [0, 1, 2, 3, float('inf')]

def strategie_minimax_w1_2(grille:list,joueur:list,poids=w1,p=2):
    return minmax(grille,joueur,poids,p)[1]
def strategie_minimax_w2_2(grille:list,joueur:list,poids=w2,p=2):
    return minmax(grille,joueur,poids,p)[1]
def strategie_minimax_w3_2(grille:list,joueur:list,poids=w3,p=2):
    return minmax(grille,joueur,poids,p)[1]
def strategie_minimax_w4_2(grille:list,joueur:list,poids=w4,p=2):
    return minmax(grille,joueur,poids,p)[1]

#w1
#print(partie(strategie_minimax_w1_2,strategie_minimax_w1_2)[1])
#print(partie(strategie_minimax_w1_2,strategie_minimax_w2_2)[1])
#print(partie(strategie_minimax_w1_2,strategie_minimax_w3_2)[1])
#print(partie(strategie_minimax_w1_2,strategie_minimax_w4_2)[1])

#w2
#print(partie(strategie_minimax_w2_2,strategie_minimax_w1_2)[1])
#print(partie(strategie_minimax_w2_2,strategie_minimax_w2_2)[1])
#print(partie(strategie_minimax_w2_2,strategie_minimax_w3_2)[1])
#print(partie(strategie_minimax_w2_2,strategie_minimax_w4_2)[1])

#w3
#print(partie(strategie_minimax_w3_2,strategie_minimax_w1_2)[1])
#print(partie(strategie_minimax_w3_2,strategie_minimax_w2_2)[1])
#print(partie(strategie_minimax_w3_2,strategie_minimax_w3_2)[1])
#print(partie(strategie_minimax_w3_2,strategie_minimax_w4_2)[1])

#w4
#print(partie(strategie_minimax_w4_2,strategie_minimax_w1_2)[1])
#print(partie(strategie_minimax_w4_2,strategie_minimax_w2_2)[1])
#print(partie(strategie_minimax_w4_2,strategie_minimax_w3_2)[1])
#print(partie(strategie_minimax_w4_2,strategie_minimax_w4_2)[1])

# print(' |    Joueur 1|   w1  |  w2  |  w3  |  w4  |\n',
#       '|Joueur 2    |       |      |      |      |\n',
#       '|------------|-------|------|------|------|\n',
#       '|      w1    |   1   |  1   |  1   |  2   |\n',
#       '|      w2    |   1   |  1   |  1   |  2   |\n',
#       '|      w3    |   1   |  1   |  1   |  2   |\n',
#       '|      w4    |   1   |  1   |  1   |  1   |')


#=============================================================================

#2.7
def partie_hybride(strategie:tuple)->str:
    ''' 
    Prend en argument une stratégie contre qui nous l'humain va jouer
    simule une partie de puissance quatre entre l'humain et la stratégie.
    Fonction demandé mais pas homogène au stratégie de minimax
    n'importe quoi peut etre donné en entrée le programme continuera
    '''
    
    #initialisation
    grille=position_initiale()
    
    #choix du joueur
    verif=False
    while verif==False:
        joueur=input('\nChoix du joueur ?   ')
        if joueur.isdigit()==True: 
            joueur=int(joueur)
            if joueur==1 or joueur==2:
                verif=True
            else: 
                print('Choix non licite')
                
    while len(coups_possibles(grille))!=0:
        
        if joueur == 1:
            #joueur 1/humain joue :
            #interface utilisateur + verification d'un coup licite
            J1=int(input('\nVotre coup ?   '))
            if J1.isdigit()==True: 
                J1=int(J1)
                if J1>0 and J1<8:
                    verif=True
                else: 
                    print('Choix non licite')
            else:
                 print('Choix non licite')  
            
            #recherche du coup associé à la colonne choisie
            for k in coups_possibles(grille):
                if k[1]==J1-1:
                    J1=k
                    break
            
            #cas d'un coup gagnant pour l'utilisateur
            if est_gagnant(grille,J1,joueur)==True:
                grille[J1[0]][J1[1]]=1
                affichage(grille)
                return 'Vous avez gagné !'
            
            #coup non gagnant pour l'utilisateur
            else:
                grille[J1[0]][J1[1]]=1
                affichage(grille)
            
            #joueur 2/Strategie choisie joue :
            J2=strategie(grille)
            
            #cas d'un coup gagnant pour la strategie adverse
            if est_gagnant(grille,J2,2)==True:
                grille[J2[0]][J2[1]]=2
                affichage(grille)
                return "Vous avez perdu :'("
            
            #cas d'un coup non gagnant pour la strategie adverse
            else:
                grille[J2[0]][J2[1]]=2
                affichage(grille)
        
        elif joueur==2:
            
            #joueur 1/Strategie choisie joue :
            J1=strategie(grille)
            
            #cas d'un coup gagnant pour la stratégie adverse
            if est_gagnant(grille,J1,1)==True:
                grille[J1[0]][J1[1]]=1
                affichage(grille)
                return"Vous avez perdu :'("
            
            #cass d'un coup non gagnant pour la strategie adverse
            else:
                grille[J1[0]][J1[1]]=1
                affichage(grille)
            
            #joueur 2/humain joue :
            #interface utilisateur + verification coup licite
            J2=int(input('\nVotre coup ?  '))
            if J2.isdigit()==True: 
                J2=int(J2)
                if J2>0 and J2<8:
                    verif=True
                else: 
                    print('Choix non licite')
                
            #recherche du coup joué à partir de la colonne voulue
            for k in coups_possibles(grille):
                if k[1]==J2-1:
                    J2=k
                    break

            #cas d'un coup gagnant pour l'utilisateur
            if est_gagnant(grille,J2,2)==True:
                grille[J2[0]][J2[1]]=2
                affichage(grille)
                return 'Vous avez gagné !'
            
            #cas d'un coup non gagnant pour l'utilisateur
            else:
                grille[J2[0]][J2[1]]=2
                affichage(grille)
    
    #cas d'une partie nulle si personne n'a gagné et que plus aucun coup n'est
    #possible
    affichage(grille)
    return 'Partie nulle'

def partie_hybride_minmax(strategie:tuple,poids:list,p:int)->str:
    ''' 
    Prend en argument une stratégie contre qui nous l'humain va jouer
    simule une partie de puissance quatre entre l'humain et la stratégie.
    adaptée à choisir une stratégie utilisant le minmax avec le choix du poids
    et de la profondeur
    n'importe quoi peut etre donné en entrée le programme continuera
    '''
    
    #initialisation
    grille=position_initiale()
    
    #choix du joueur
    verif=False
    while verif==False:
        joueur=input('\nChoix du joueur ?  ')
        if joueur.isdigit()==True: 
            joueur=int(joueur)
            if joueur==1 or joueur==2:
                verif=True
            else: 
                print('choix non licite')
        else: 
            print('Choix non licite')
            
    while len(coups_possibles(grille))!=0:
        
        if joueur == 1:
            #joueur 1 joue
            verif =False
            while verif == False:
                J1=(input('\nVotre coup ?'))
                if J1.isdigit()==True: 
                    J1=int(J1)
                    if J1>0 and J1<8:
                        verif=True
                    else: 
                        print('Choix non licite')
                else:
                    print('Choix non licite')
                    
            for k in coups_possibles(grille):
                if k[1]==J1-1:
                    J1=k
                    break
                
            if est_gagnant(grille,J1,joueur)==True:
                grille[J1[0]][J1[1]]=1
                affichage(grille)
                return 'vous avez gagné :)'
            else:
                grille[J1[0]][J1[1]]=1
                affichage(grille)
            
            #joueur 2 joue
            J2=strategie(grille,2,poids,p)
            if est_gagnant(grille,J2,2)==True:
                grille[J2[0]][J2[1]]=2
                affichage(grille)
                return '''  Vous avez perdu :'(   '''
            else:
                grille[J2[0]][J2[1]]=2
                affichage(grille)
        
        elif joueur==2:
            
            #joueur 1 joue
            J1=strategie(grille,1,poids,p)
            if est_gagnant(grille,J1,1)==True:
                grille[J1[0]][J1[1]]=1
                affichage(grille)
                return ''' Vous avez perdu :'(  '''
            else:
                grille[J1[0]][J1[1]]=1
                affichage(grille)
            
            #joueur 2 joue
            verif =False
            while verif == False:
                J2=(input('\nVotre coup ?'))
                if J2.isdigit()==True: 
                    J2=int(J2)
                    if J2>0 and J2<8:
                        verif=True
                    else: 
                        print('Choix non licite')
                else: 
                    print('Choix non licite')
                    
            for k in coups_possibles(grille):
                if k[1]==J2-1:
                    J2=k
                    break

            assert J2 in coups_possibles(grille)
            if est_gagnant(grille,J2,2)==True:
                grille[J2[0]][J2[1]]=2
                affichage(grille)
                return 'vous avez gagné !'
            
            else:
                grille[J2[0]][J2[1]]=2
                affichage(grille)
    
    print(affichage(grille))
    return 'Partie nulle'


w5=[0,1,50000,1000000,float('inf')]


#après modification des feuilles la meilleure stratégie est profondeur de 1
# et un vecteur poids avec un grand écart de valeur entre poids[1],[2] et [3]


# def module_antijeu(grille:list,joueur:int)->list:
#     ''' 
#     Grille une liste de listes, un entier joueur qui est 1 ou 2
#     Si c'est au joueur de jouer ce module va donner un coup qui évitera si 
#     possible une victoire de l'autre joueur
#     '''
#     liste_possible=coups_possibles(grille)
#     for s in coups_possibles(grille):
#         grille[s[0]][s[1]]=joueur
#         for c in coups_possibles(grille):
#             if  est_gagnant(grille,c,3-joueur)==True:
#                 if s in liste_possible:  
#                     liste_possible.remove(s)
#         grille[s[0]][s[1]]=0
#     if len(liste_possible)==0:
#         return coups_possibles(grille)[randrange(7)]
         
#     return(liste_possible)

# 2 stratégie pour le joueur 1 et 2 qui sont pour le moment imbattable par tout
# humain qui c'est lancé en guerre contre

def strategie_minimax1(grille:list,joueur=1,poids=w5,p=5)->tuple:
    return minmax(grille,joueur,poids,p)[1]

def strategie_minimax2(grille:list,joueur=2,poids=w5,p=5)->tuple:
    return minmax(grille,joueur,poids,p)[1]


# print('Test contre des stratégies humaines :')
# print("J'ai testé mon algorithme en w5 et p=4 et pour le moment personne n'a",
#       "réussi à gagner sur un ensemble de 10 personnes différentes",
#       "Que ce soit en tant que joueur 1 et 2, l'aglo gagne en tendant un",
#       "piège en créant des alignements possiblement gagnant",
#       " sur 2 cases de suite")
# print('\nTest contre d autre stratégie informatique :\n',
#       "J'ai testé ma stratégie w5 et p=5 sur différents sites de puissance 4")
# print("\n Gagnant en joueur 1 et 2 contre ",
#       "https://lululataupe.com/tout-age/686-puissance-4",
#       "\nhttps://kevinragonneau.fr/blog/jeux/puissance-4 victoire en seul j=1",
#       'car seul ce mode est disponible',
#       "\nhttps://www.casualarena.com/fr/puissance-4 gagne j1, perd en j=2",
#       "(piège puis remplissage de grille pour atteindre le coup perdant) \n",
#       "https://www.crazygames.fr/jeu/4-in-a-row gagnant et seul j=2 est",
#       "disponible, victoire en difficulté 1 2 et 3",
#       "\nhttps://www.logicieleducatif.fr/math/logique/puissance-4.php",
#       "gagnant en joueur 1 et 2\n")



# print('\n-----------------------------------------------------------------\n')
# print(''' Partie 3 : Amélioration des fonctions d'utilité''')
# print('\n-----------------------------------------------------------------\n')

# III
#1
#==============================================================================

'Reconstruction des alignements possibles sur les colonnes'

# alignements_col=[]
# X=alignements_col
# for k in range(3):
#     for i in range(7):
#         D=[]
#         for j in range(4):
#             D.append((j+k,i))
#         X.append(D)

alignements_col=         [[(0, 0), (1, 0), (2, 0), (3, 0)],
                          [(0, 1), (1, 1), (2, 1), (3, 1)],
                          [(0, 2), (1, 2), (2, 2), (3, 2)],
                          [(0, 3), (1, 3), (2, 3), (3, 3)],
                          [(0, 4), (1, 4), (2, 4), (3, 4)],
                          [(0, 5), (1, 5), (2, 5), (3, 5)],
                          [(0, 6), (1, 6), (2, 6), (3, 6)],
                          [(1, 0), (2, 0), (3, 0), (4, 0)],
                          [(1, 1), (2, 1), (3, 1), (4, 1)],
                          [(1, 2), (2, 2), (3, 2), (4, 2)],
                          [(1, 3), (2, 3), (3, 3), (4, 3)],
                          [(1, 4), (2, 4), (3, 4), (4, 4)],
                          [(1, 5), (2, 5), (3, 5), (4, 5)],
                          [(1, 6), (2, 6), (3, 6), (4, 6)],
                          [(2, 0), (3, 0), (4, 0), (5, 0)],
                          [(2, 1), (3, 1), (4, 1), (5, 1)],
                          [(2, 2), (3, 2), (4, 2), (5, 2)],
                          [(2, 3), (3, 3), (4, 3), (5, 3)],
                          [(2, 4), (3, 4), (4, 4), (5, 4)],
                          [(2, 5), (3, 5), (4, 5), (5, 5)],
                          [(2, 6), (3, 6), (4, 6), (5, 6)]]

# print('Nombre d alignements possibles sur les colonnes :',len(alignements_col))

def utilité2(G:list,k:int,w:list)->int:
    ''' 
    Fonction d'utilité n°2, complément de la fonction utilité mais en rajoutant
    une pondération supplémentaire sur les alignements de 2 positions 
    successives d'une même colonne. Tout les alignements possibles gagnants
    des colonnes sont cité au-dessus dans alignements_col
    '''
    #initialisation de la valeur d'utilité
    U_k=0
    
    #test pour tous les alignements possibles
    for i in range(len(alignements)):
        L=[]
        #recherche des n_k(A) et n_(3-k)(A)
        for l in range(4):
            if G[alignements[i][l][0]][alignements[i][l][1]]==k:
                L.append(1)
                
            elif G[alignements[i][l][0]][alignements[i][l][1]]==3-k:
                L.append(-1)

        #ajout à la valeur d'utilité selon la fonction de poids :
            
        #cas de n_k(A) et n_(3-k)(A) non tous deux nuls
        if -1 in L and 1 in L:
            None
        
        else:
            U_k+= w[L.count(1)]-w[L.count(-1)]
    
    #rajout d'une pondération pour 2 positions successives d'une même colonne
    for i in range(len(alignements_col)):
        L=[]
        for l in range(4):
            if G[alignements_col[i][l][0]][alignements_col[i][l][0]]==k:
                L.append(1)
            elif G[alignements_col[i][l][0]][alignements_col[i][l][0]]==3-k:
                L.append(-1)
            
        #cas de n_k(A) et n_(3-k)(A) non tous deux nuls
        if -1 in L and 1 in L:
            None
        else:
            if L.count(1) == 2 or L.count(-1)==2:
                U_k+= (w[L.count(1)]+w[L.count(1)+1])/2
                U_k-= (w[L.count(-1)]+w[L.count(-1)+1])/2
            
    return U_k

def minmax2(grille:list,joueur:int,poids:list,p:int)->tuple:
    '''
    Prend en argument grille une grille de jeu sous forme de liste de listes,
    joueur un entier 1 ou 2 représentant le joueur, poids une liste de poids
    de taille 5 et p un entier représentant la profondeur d'analyse.
    Renvoie l'utilité maximale à p coups U_k (indice de puissance p)
      !!!Utilise utilité2 comme fonction d'utilité!!!
    '''

    #initialisation
    U_j_0=utilité2(grille,joueur,poids)
    liste_possible=coups_possibles(grille)
    
    # 2 cas d'une partie déjà finie
        #Partie gagnée par 1 ou 2
    if U_j_0==poids[4] or U_j_0==-poids[4]:
        return (U_j_0,None)
    
        #Partie nulle
    if len(liste_possible)==0:
        return(0,None)
    
    #compteur permettant de trouver qui joue le coup
    i=0
    for k in range(len(grille)):
        i+=grille[k].count(1)
        i+=grille[k].count(2)
    
    #cas des feuilles
    for s in liste_possible:
        if est_gagnant(grille,s,joueur)==True and i%2!=joueur%2:
            return (float('inf'),s)
            
        elif est_gagnant(grille,s,3-joueur)==True and i%2==joueur%2:
            return (-float('inf'),s)

    #cas d'une profondeur 0
    if p==0:
        return (U_j_0,None)
    
    
    #Traitement du minmax pour chaque choup :
    
    L1=[]
    #cas joueur=1 et le joueur 2 joue
    if i%2==1 and joueur==1:
        for s in liste_possible:
            grille[s[0]][s[1]]=2
            L1.append(minmax(grille,joueur,poids,p-1)[0])
            
            if  L1!=[]:
                if min(L1)==L1[-1]:
                    S1=s
            else:
                S1=None

            grille[s[0]][s[1]]=0
            
        return (min(L1),S1)
    
    #cas joueur=2 et le joueur 2 joue
    elif i%2==1 and joueur==2:
        for s in liste_possible:
            grille[s[0]][s[1]]=2
            L1.append(minmax(grille,joueur,poids,p-1)[0])
            
            if  L1!=[]:
                if max(L1)==L1[-1]:
                    S1=s
            else:
                S1=None
                
            grille[s[0]][s[1]]=0
            
        return (max(L1),S1)
    
    #cas joueur=1 et le joueur 1 joue
    elif i%2==0 and joueur==1:
        for s in liste_possible:
            grille[s[0]][s[1]]=1
            L1.append(minmax(grille,joueur,poids,p-1)[0])
            
            if  L1!=[]:
                if max(L1)==L1[-1]:
                    S1=s
            else:
                S1=None

            grille[s[0]][s[1]]=0
       
        return (max(L1),S1)
    
    #cas joueur=2 et le joueur 1 joue
    elif i%2==0 and joueur==2:
        for s in liste_possible:
            grille[s[0]][s[1]]=1
            L1.append(minmax(grille,joueur,poids,p-1)[0])
            
            if  L1!=[]:
                if min(L1)==L1[-1]:
                    S1=s
            
            else:
                S1=None
                
            grille[s[0]][s[1]]=0  
            
        return (min(L1),S1)
    
#Pour tester une partie entre ces 2 stratégies il suffit de changer les 
#paramètres par défaut
def strategie_minimax1_2(grille:list,joueur=1,poids=w5,p=5)->tuple:
    return minmax2(grille,joueur,poids,p)[1]

def strategie_minimax2_2(grille:list,joueur=2,poids=w5,p=5)->tuple:
    return minmax2(grille,joueur,poids,p)[1]

# partie(strategie_minimax1_2,strategie_minimax2_2,True)

# print('\nAprès avoir testé pour plusieurs profondeurs (3 , 4 et 5), ',
#       'et des fonctions de poids variées (w1 , w2, w3, w5) On remarque',
#       'qu effectivement les strategies ont tendance a jouer plus sur les',
#       'colonnes')
# print('Le bonus ajouté pour 2 positions sur une même colonne est de :\n',
#       '\nw[2]+w[3]\n----------\n    2\n De même pour le joueur adverse.')

# print('Pour tester les stratégies du minimax liés aux fonction d utilité 1 ou',
#       '2, Elles sont respectivement ligne 1161-1164 et ligne 1401-1404',
#       '\nElles sont déjà paramétrées sur poids w5 et p = 5 en joueur 1-2\n\n'
#       ,'strategie_minimax1 - strategie_minimax2 \n et\n strategie_minimax1_2 -'
#       ,'strategie_minimax2_2')
# print('\nPour tester de jouer contre :\n\n partie_hybride_minmax()')
# #2
#================================================================================================|=

#Je n'ai pas réussi a mettre en oeuvre la derniere fonction d'utilité.


Grille = position_initiale()




chdir('C:\TRAVAIL\P2A\info\TD4')

# Dimensions de la grille
nb_colonnes = 7
nb_lignes = 6

# Dimensions des cases et des jetons
taille_case = 110
rayon_jeton = taille_case // 2 - 5

# Dimensions de la fenêtre
largeur_fenetre = nb_colonnes * taille_case
hauteur_fenetre = (nb_lignes + 1) * taille_case  # +1 pour la ligne supplémentaire pour déposer les jetons

# Couleurs
COULEUR_FOND = (18, 10, 68)  # Couleur de fond de la fenêtre
COULEUR_GRILLE = (255, 255, 255)  # Couleur de la grille
COULEUR_JOUEUR_1 = (255, 0, 0)  # Couleur du jeton du joueur 1
COULEUR_JOUEUR_2 = (255, 255, 0)  # Couleur du jeton du joueur 2

NOIR = (0, 0, 0)
GRIS = (150, 150, 150)
BLEU = (0, 0, 255)
ROUGE = (255, 0, 0)
JAUNE = (255,255,0)


def dessiner_grille(fenetre:any):
    ''' 
    dessine la grille 
    '''
    
    fenetre.fill(COULEUR_FOND)
    
    # Dessiner les cases de la grille
    for colonne in range(nb_colonnes):
        for ligne in range(nb_lignes):
            pygame.draw.rect(fenetre,
                             COULEUR_GRILLE,
                             (colonne * taille_case, (ligne + 1) * taille_case, taille_case,
                              taille_case))
    
    # Dessiner les lignes de séparation verticales
    for colonne in range(nb_colonnes + 1):
        pygame.draw.line(fenetre,
                         COULEUR_GRILLE,
                         (colonne * taille_case, taille_case),
                         (colonne * taille_case, hauteur_fenetre - taille_case), 5)


def dessiner_jetons(grille:list,fenetre:any):
    '''
    dessiner les jetons à partir de la grille
    '''
    
    rayon = int(taille_case/2 - 5)
    for i in range(nb_colonnes):
        for j in range(nb_lignes):
            joueur = grille[j][i]
            couleur = BLEU if joueur == 1 else ROUGE if joueur == 2 else NOIR
            x = i * taille_case + taille_case//2
            y = hauteur_fenetre - (j * taille_case + taille_case//2)
            pygame.draw.circle(fenetre, couleur, (x, y), rayon)
            if joueur == 0:
                pygame.draw.circle(fenetre, GRIS, (x, y), rayon, 3)


# Fonction pour ajouter un jeton dans la colonne sélectionnée
def ajouter_jeton(colonne :int, joueur:int, Grille:list):
    for ligne in range(nb_lignes - 1, -1, -1):
        if Grille[5-ligne][colonne] == 0:
            Grille[5-ligne][colonne] = joueur
            return True
    return False


def trouver_ligne(grille:list, colonne:int)->int or None:
    ''' 
    cherche la ligne possible à partir de la colonne 
    '''
    
    compteur = 0 
    for ligne in range(nb_lignes - 1, -1, -1):
        
        if grille[ligne][colonne] == 0:
            compteur=1
            ligne_f= ligne
    if compteur == 1: 
        return ligne_f
    return None

def animation_victoire(grille:list,gagnant:int,joueur:int,nulle:int,fenetre)->list:
    ''' 
    dessine un trait rouge sur la combinaison gagnante
    '''
    if gagnant == False or nulle == True:
        None 
    else: 

        X=[]
        #test pour tous les alignements possibles
        for i in range(69):
            L=[]
            for l in range(4):
                if grille[alignements[i][l][0]][alignements[i][l][1]]==3-joueur:
                    L.append(alignements[i][l])
                    
                else:
                    break
            if len(L)==4:
                X.append(L)
                
        for k in range(len(X)):
            for position in X[k]:
                ligne, colonne = 5-position[0],position[1]
                x = colonne * taille_case + taille_case // 2
                y = (ligne + 1) * taille_case + taille_case // 2
                rayon = taille_case // 2 - 5
                pygame.draw.circle(fenetre, JAUNE, (x, y), rayon)
                pygame.display.flip()
                pygame.time.wait(300)
    return X


def continu_victoire(X:list,fenetre:any):
    ''' 
    rond jaune en continu
    '''

    for k in range(len(X)):
        for position in X[k]:
            ligne, colonne = 5-position[0],position[1]
            x = colonne * taille_case + taille_case // 2
            y = (ligne + 1) * taille_case + taille_case // 2
            rayon = taille_case // 2 - 5
            pygame.draw.circle(fenetre, JAUNE, (x, y), rayon) 
        



def partie_pvp():
    ''' 
    partie en joueur contre joueur 
    click gauche pour poser un pion sur une colonne
    fleche bas pour relancer la partie 
    '''
    
    # Boucle principale du jeu
    en_cours = True
    partie_terminee = False
    nulle = False 
    stop = 0
    tour_joueur = 1

    Grille=position_initiale()
    
    pygame.init()
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Puissance 4")
    
    
    while en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_cours = False
                
            # Clic gauche de la souris           
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
                if partie_terminee == False:
                    colonne = event.pos[0] // taille_case
                    ligne = trouver_ligne(Grille, colonne)
                    if len(coups_possibles(Grille))==0:
                        partie_terminee = True 
                        nulle = True
                        
                    if ligne is not None and est_gagnant(Grille,
                                                         (ligne, colonne),
                                                         tour_joueur):
                        partie_terminee = True 
                        
                    if ajouter_jeton(colonne, tour_joueur, Grille) == True :
                        # Changer de joueur à chaque coup valide
                        tour_joueur = 2 if tour_joueur == 1 else 1
    
            elif pygame.key.get_pressed()[pygame.K_r] == True: 
                Grille= position_initiale()
                partie_terminee = False
                nulle = False
                tour_joueur = 1
                stop = 0
                
    
        dessiner_grille(fenetre)
        dessiner_jetons(Grille,fenetre)
        if tour_joueur == 1:
            joueur1=pygame.image.load('joueur_1.jpg')
            fenetre.blit(joueur1,(280,50))
        elif tour_joueur == 2:
            joueur2=pygame.image.load('joueur_2.jpg')
            fenetre.blit(joueur2,(280,30))
        
        if partie_terminee == True and stop == 0:
            anim=animation_victoire(Grille,partie_terminee,
                                    tour_joueur,nulle,fenetre)
            stop=1
            
        if partie_terminee == True :
            continu_victoire(anim,fenetre)
            
        pygame.display.flip()            
    pygame.quit()
    


def partie_pc(difficulté=None):
    ''' 
    partie contre l'ordinateur
    difficulté  1, 2 , 3, 4 de base None implique difficulté aléatoire
    ''' 
    if difficulté == None:
        difficulté = randint(1,4)
    
    if difficulté == 1:
        poids = [0,1,2,3,float('inf')]
        prof = 1 
        
    elif difficulté == 2:
        poids = [ 0, 1, 5, 10, float('inf')]
        prof = 2

    elif difficulté == 3:
        poids = [ 0, 1, 100, 1000, float('inf')]
        prof = 4
        
    elif difficulté == 4:
        poids = w5
        prof = 5


        
    #déclaration des variables : 
        
    #sert à faire tourner le jeu
    en_cours = True
    
    #indique une partie finie et si elle est nulle 
    partie_terminee = False
    nulle = False 
    
    #permet l'animation 
    stop = 0
    #trace le tour du joueur ( initialement en j = 1)
    tour_joueur = 1
    
    #grille de jeu
    Grille=position_initiale()
    
    #indique si l'on est au choix du joueur ( 0 ) ou en partie ( 1 )
    start = 0

    
    pygame.init()
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Puissance 4")
    
    # Boucle principale du jeu
    while en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_cours = False
            
            #cas du choix du joueur 1
            elif start == 0 and ( pygame.key.get_pressed()[pygame.K_KP1]):
                start = 1
                joueur = 1
                
            #cas du choix du joueur 2 
            elif start == 0 and ( pygame.key.get_pressed()[pygame.K_KP2] or\
                                 pygame.key.get_pressed()[pygame.K_KP2]):
                start = 1
                joueur = 2 
            
            #partie lancée ->
            elif start == 1:
                
                #input du coup du joueur
                if event.type == pygame.MOUSEBUTTONDOWN and\
                    event.button == 1 and tour_joueur == joueur:  
                        
                    if partie_terminee == False:
                        
                        colonne = event.pos[0] // taille_case
                        ligne = trouver_ligne(Grille, colonne)
                        
                        #si la partie est nulle ->
                        if len(coups_possibles(Grille))==0:
                            partie_terminee = True 
                            nulle = True
                            
                        #si la partie est remportée par le joueur ->
                        elif ligne is not None and est_gagnant(Grille,
                                                               (ligne, colonne),
                                                               tour_joueur):
                            
                            print("Le joueur", tour_joueur, "a gagné !")
                            print(f'difficulté : {difficulté}')
                            partie_terminee = True 
                        
                        #impact du coup joué sur la grille + tour suivant
                        if ajouter_jeton(colonne, tour_joueur, Grille) == True:
                            tour_joueur=3-tour_joueur
                
                #cas du coup de l'ordinateur
                elif tour_joueur == 3-joueur:
                    if partie_terminee == False:
                        (ligne,colonne)= minmax(Grille,3-joueur,poids,prof)[1]
                        
                        #si la partie est nulle ->
                        if len(coups_possibles(Grille))==0:
                            partie_terminee = True 
                            nulle = True
                        
                        #si la partie est remportée par le joueur ->
                        elif ligne is not None and est_gagnant(Grille,
                                                             (ligne, colonne),
                                                             tour_joueur):
                            print("Le joueur", tour_joueur, "a gagné !")
                            print(f'difficulté : {difficulté}')
                            partie_terminee = True 
                        
                        #impact du coup joué sur la grille + tour suivant
                        if ajouter_jeton(colonne, tour_joueur, Grille) == True:
                            tour_joueur=3-tour_joueur
                
                
                #permet de remettre le jeu à 0 sur la sélection du joueur
                #via la touche 'r'
                elif pygame.key.get_pressed()[pygame.K_r] :
                    Grille= position_initiale()
                    partie_terminee = False
                    nulle = False
                    tour_joueur = 1
                    stop = 0
                    start = 0 
                    
        # écran de sélection du joueur 
        if start == 0:
            fenetre.fill(COULEUR_FOND)
            joueur1=pygame.image.load('joueur_1_selec.jpg')
            fenetre.blit(joueur1,(100,250))
            joueur2=pygame.image.load('joueur_2_selec.jpg')
            fenetre.blit(joueur2,(480,250))
        
        #cas de la partie en cours
        elif start == 1:
            
            #représentation de la grille
            dessiner_grille(fenetre)
            dessiner_jetons(Grille,fenetre)
            
            #indication sur le joueur qui joue : 
            if joueur == 1:
                joueur1=pygame.image.load('joueur_1.jpg')
                fenetre.blit(joueur1,(280,50))
            elif joueur == 2:
                joueur2=pygame.image.load('joueur_2.jpg')
                fenetre.blit(joueur2,(280,50))
            
            #animation pour indiquer le coup gagnant
            if partie_terminee == True and stop == 0:
                anim=animation_victoire(Grille,partie_terminee,
                                        tour_joueur,nulle,fenetre)
                stop=1
            
            # fin de l'animation et on garde le changement de l'alignement
            #gagnant
            if partie_terminee == True :
                continu_victoire(anim,fenetre)
        
        #update de l'image
        pygame.display.flip()            
    
    pygame.quit()
    