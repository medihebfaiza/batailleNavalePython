#! /usr/bin/python
# -*- coding: utf-8 -*-
#authors : Thais Aurard, Maxime Soustelle
from Joueur import *
from Bateau import *

#Fonctions
class Tir:
	def __init__(self, coordA, coordB, joueur):
        #			int x int x Joueur --> Tir
		self.coordA = coordA
		self.coordB = coordB
		self.joueur = joueur
        
	def resultatTir(self):
	#			Tir --> str
		for i in range(0,len(self.joueur.bateaux())): #Itere sur les bateaux du joueur
			for l in range(0,len(self.joueur.bateaux()[i].positionBateau())) : #Itere sur les positions du bateau courant
				if(self.joueur.bateaux()[i].positionBateau()[l][0] == self.coordA and self.joueur.bateaux()[i].positionBateau()[l][1] == self.coordB and (not self.joueur.bateaux()[i].etatPosition()[l])) : #Si les coordonnées du tir concorde avec la position du bateaux et quelle n'est pas touche
					self.joueur.bateaux()[i].etatPosition()[l] = True
					isDead = True
					cpt = 0
					while (isDead and cpt < len(self.joueur.bateaux()[i].etatPosition())) : #Verifie si le bateau est mort
						if((not self.joueur.bateaux()[i].etatPosition()[cpt])):
							isDead = False
						cpt = cpt + 1
					if(isDead):
						self.joueur.bateaux().pop(i)
						return "coulé"
                        #coule
					else:
						return "touché"
                        #Touche
				elif(self.joueur.bateaux()[i].positionBateau()[l][0] == self.coordA or self.joueur.bateaux()[i].positionBateau()[l][1] == self.coordB) :
					return "en vue"
                    #En vue
				else :
					return "à l’eau"
                    #A l'eau


	def verifierEnVue(self):
	#			Tir --> bool
		for i in range(0,len(self.joueur.bateaux())) : #Itere sur les bateaux du joueur
			for l in range(0,len(self.joueur.bateaux()[i].positionBateau())) : #Itere sur les positions du bateau courant
				if((self.joueur.bateaux()[i].positionBateau()[l][0] == coordA and self.joueur.bateaux()[i].positionBateau()[l][1] != coordB) or (self.joueur.bateaux()[i].positionBateau()[l][1] == coordB and self.joueur.bateaux()[i].positionBateau()[l][0] != coordA)) :
					return True
		return False

