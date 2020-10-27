# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 20:03:16 2020
@author: G.S. Verhoeven
"""
import numpy as np
  
"""
Exercise Classes & Inheritance.
1. Maak een class Beleidsmedewerker, met attributen naam, leeftijd, en afdeling.
2. Maak een method verjaardag() die de leeftijd met 1 verhoogt.
3. Maak een method werken() die random drie acties kiest uit deze lijst: 
    "memo_schrijven",  "videobellen" , "koffie halen".
    Tip: gebruik np.random.choice()
4. Maak een class Datascientist, die erft van Beleidsmedewerker.
De datascientist heeft een extra actie: coden(). Deze actie print een stukje python code.
"""



class Beleidsmedewerker:

    def __init__(self, naam, leeftijd, afdeling):  
        self.naam = naam
        self.leeftijd = leeftijd
        self.afdeling = afdeling
        
    def verjaardag(self):
        self.age +=1

    def werken(self):
        self.werken = np.random.choice(["memo_schrijven",  "videobellen" , "koffie halen"], 1)       

    def Beleidsmedewerkerinfo(self):
        print(self.naam + " is " + str(self.leeftijd) + " year(s) and old works at " + self.afdeling)
  
class Datascientist(Beleidsmedewerker):
    def __init__(self, naam, leeftijd, afdeling):    #niet noodzakkelijk
        super().__init__(naam, leeftijd, afdeling)   #niet noodzakkelijk
        
    def coden(self):    
        print("x = x + 1")
        
        
 
Haaland = Datascientist("Haaland", 20, "BVB")
Haaland.Beleidsmedewerkerinfo() 
Haaland.coden()      