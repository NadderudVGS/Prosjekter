"""
Av Martin, Sigurd og Axel

Dna-manipulipasjon | oppgave 3

"""

import os
import random as rand


# Importerer og formaterer DNA-filen
def ImportData(file):
    f = open(file, "r")  
    data = f.read()        
    f.close()                 
    
    
    # Begandler data pga. formateringen
    data = data.replace("\n", "") # fjerner alle enter i strengen
    
    return data # behandlet data.(dna) 

# Lager RNA-sekvens av DNA
def DNA_to_RNA(text):
    rna = "" 
    
    # Looper over hver bokstav i text (dna). O(n)
    for boksav in text:
        if boksav == "G":    # Når vi ser G
            rna += "C"            # gjør vi den om til C
            
        elif boksav == "T": # Når vi ser T
            rna += "A"            # gjør vi den om til A
            
        elif boksav == "A": # Når vi ser A
            rna += "U"            # gjør vi den om til U
            
        elif boksav == "C": # Når vi ser C
            rna += "G"            # gjør vi den om til G

    return rna

# Lager amonosyre sekvens
def DNA_to_AMINO(text):
    # Table er et dictionary som vi fant på nettet. Den innholder en 
    # oversikt over hvilke kodon lager hvilke aminosyrer. Denne oversikten
    # har 3 baser fra dna, isteden for de oversatte basene fra rna, som ribosomet
    # bruker. Derfor lager vi aminosyrer fra dna direkte.
    table = {
            'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
            'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
            'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
            'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
            'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
            'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
            'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
            'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
            'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
            'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
            'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
            'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
            'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
            'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
            'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
            'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', 
        } 
    
    amino = "" 
    
    # Looper over hver 3 bokstav i text (dna). O(n/3)
    for i in range(0, len(text)-2, 3): 
        kodon = text[i] + text[i + 1] + text[i + 2] # Definerer et kodon
        amino += table[kodon]                                  # Legger tilhørende aminosyren til aminosyre strengen
        
    amino = amino.split("_") # Splitter teksten ved stop og start kodoner --> 
                                              # En liste med aminosyre kjeder som representerer proteiner

    return amino # proteiner

# Lager Mutert Dna Sekvens
def Mutate_DNA(text, mChance):
    mutations = 0                       
    Mdna = ""                               
    B = ["A", "T", "G", "C", ""] 
    
    # looping over dna seq. O(n)
    for i in text: 
        r = S_Vekt(mChance) # True / False
        
        if r == True:
            Mdna += rand.choice(B) # Adding random mutaion
            mutations += 1               
            
        else:
            Mdna += i              # Dont mutate
            
    return Mdna, format(float(mutations/len(text)),".12f")  # Mutated dna and mutaion %

# Returnerer True/False etter sansyligheten du har oppgitt.0 -> 1. max 4 desimaler
def S_Vekt(chance):
    m = 1000                 
    chance = chance * m          
    r = rand.randint(0, m-1) 
    if chance < r:
        return False

    elif chance > r:
        return True

    
# Finner mappen til programmet
path = os.path.dirname(os.path.abspath(__file__))

# Lager dna
dna = ImportData(f"{path}/Data/DNA_mouse.txt")
# Lager rna 
rna = DNA_to_RNA(dna)
# Lager aminosyrer
amino = DNA_to_AMINO(dna)


# Muterer dna, and mutation %
m_dna, r_m = Mutate_DNA(dna, 0.1)
# Mutert Aminosyrer
m_amino = DNA_to_AMINO(m_dna)