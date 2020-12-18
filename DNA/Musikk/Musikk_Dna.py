####### Importerer Pakker #######
import pygame
from time import sleep

import os


# Importerer og formaterer DNA-filen
def ImportData(file):
    f = open(file, "r")  
    data = f.read()        
    f.close()                 
    
    
    # Begandler data pga. formateringen
    data = data.replace("\n", "") # fjerner alle enter i strengen
    
    return data # behandlet data.(dna) 


####### Lager Dna #######
path = os.path.dirname(os.path.abspath(__file__))
path = path.replace("Musikk", "")

dna = ImportData(f"{path}/Data/DNA_mouse.txt")

####### Init Musikk module #######
pygame.mixer.init()


####### Lager Noter Pioano #######
D = pygame.mixer.Sound("Noter/D.wav") # D - note
C = pygame.mixer.Sound("Noter/C.wav") # C - note
E = pygame.mixer.Sound("Noter/E.wav") # E - note
G = pygame.mixer.Sound("Noter/G.wav") # G - note


###### Musikk loop #######
for i in dna:
    if i == "G":
        G.play()
    elif i == "T":
        E.play()
    elif i == "C":
        C.play()
    elif i == "A":
        D.play()
        
    sleep(0.5)

