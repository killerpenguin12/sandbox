# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:55:39 2020

@author: deads
"""
import numpy as np
import matplotlib.colors as color
import string 
from bs4 import BeautifulSoup        
import requests 
import pandas as pd
import re

class Pokemon:
    
    def __init__(self,UserInput = None):
        page_link = "https://play.pokemonshowdown.com/data/pokedex.js?fe67f5ac"

        page_response = requests.get(page_link,timeout = 10)
        body = BeautifulSoup(page_response.content,"lxml")
        data = str(body.get_text())
        self.names = (re.findall(r'name:"(.+?)"', data))
        self.stats = (re.findall(r'baseStats:{(.+?)}', data))
        self.types = (re.findall(r'types:\[(.+?)]', data))
        self.tier = (re.findall(r'tier:"(.+?)"', data))
        self.UserInput = UserInput

    def numOfTypes(self,ourTypes,tierName = None):
        import matplotlib.pyplot as plt 
        from numpy import arange
        self.fire = 0    #fire
        self.water = 0    #water
        self.electric = 0    #electric
        self.ground = 0    #ground
        self.fighting = 0    #fighting
        self.dragon = 0    #dragon
        self.poison = 0    #poison
        self.dark = 0    #dark
        self.fairy = 0    #fairy
        self.psychic = 0   #psychic
        self.ice = 0    #ice
        self.flying = 0
        self.grass = 0   #grass
        self.ghost = 0   #ghost
        self.rock = 0   #rock
        self.bug = 0   #bug
        self.steel = 0   #steel
        self.normal = 0   #normal
        Alltypes = (re.findall(r'"(.*?)"',str(ourTypes)))
        for i in range(len(Alltypes)):
            if (Alltypes[i] == 'Fire'):
                self.fire += 1
            if (Alltypes[i] == 'Water'):
                self.water += 1
            if (Alltypes[i] == 'Electric'):
                self.electric += 1
            if (Alltypes[i] == 'Ground'):
                self.ground += 1
            if (Alltypes[i] == 'Fighting'):
                self.fighting += 1
            if (Alltypes[i] == 'Dragon'):
                self.dragon += 1
            if (Alltypes[i] == 'Poison'):
                self.poison += 1
            if (Alltypes[i] == 'Dark'):
                self.dark += 1
            if (Alltypes[i] == 'Ice'):
                self.ice += 1
            if (Alltypes[i] == 'Flying'):
                self.flying += 1
            if (Alltypes[i] == 'Fairy'):
                self.fairy += 1
            if (Alltypes[i] == 'Psychic'):
                self.psychic += 1
            if (Alltypes[i] == 'Grass'):
                self.grass += 1
            if (Alltypes[i] == 'Ghost'):
                self.ghost += 1
            if (Alltypes[i] == 'Rock'):
                self.rock += 1
            if (Alltypes[i] == 'Bug'):
                self.bug += 1
            if (Alltypes[i] == 'Steel'):
                self.steel += 1
            if (Alltypes[i] == 'Normal'):
                self.normal += 1
        data = (self.fire,self.water,self.electric,self.ground,self.fighting,
                    self.dragon,self.poison,self.dark,self.fairy,self.psychic,
                    self.grass,self.ghost,self.rock,self.bug,self.steel,self.normal,
                    self.flying, self.ice)
        plt.bar(arange(18),data,0.50)
        plt.ylabel('Number of Pokemon')
        if tierName != None:
            plt.title('Types of Pokemon in ' + tierName + ' tier')
        else: 
            plt.title('Types of Pokemon')
        plt.xticks(arange(18), ('Fire', 'Water', 'Electric', 'Ground', 
                                    'Fighting','Dragon','Poison','Dark','Fairy','Psychic'
               ,'Grass','Ghost','Rock','Bug','Steel','Normal','Flying','Ice'),rotation=90)
        #plt.yticks(np.arange(0, 81, 10))
        plt.show()
        
    def sepTiers(self): #To seperate different tiers and compute with them 
        """Tier names are as follows:
        Uber -- as the name implies, very strong (Uber is done like (Uber) for some but not for others, so include both)
        OU   -- Overused, lots of useful pokemon, competitive is mostly here 
        UUBL -- Underused Ban List, broken but not used that much 
        UU   -- Not used becuase of some flaws 
        RUBL -- Rarely Used Ban List, typically outclassed but better than Rarely used 
        RU   -- Rarely Used, easily outclassed, have specific niches in play
        NUBL -- Never Used Ban List, too broken for neverused
        NU   -- Never Used, that about says it
        PUBL -- PU Ban list, below NU
        PU   -- Rarely if ever seen in competitive 
        NFE  -- Not Fully evolved, just the base forms of all other pokemon
        Illegal -- Not defined
        https://pokemon.neoseeker.com/wiki/Tier_listings"""
        GroupTypes = []
        GroupBaseStats = []
        GroupSpecies = []
        print("here is names: " , len(self.names))
        print("here is stats: " , len(self.stats))
        for i in range(len(self.tier)):
            if self.UserInput == 'Uber':
                if self.tier[i] == '(Uber)': #whatever tier we want to investigate:
                    GroupTypes.append(self.types[i])
                    GroupBaseStats.append(self.stats[i])
                    GroupSpecies.append(self.names[i])
            if self.tier[i] == self.UserInput: #whatever tier we want to investigate, this is only for uber:
                GroupTypes.append(self.types[i])
                GroupBaseStats.append(self.stats[i])
                GroupSpecies.append(self.names[i])
        self.names = GroupSpecies
        self.stats = GroupBaseStats
        self.types = GroupTypes
        #return (GroupSpecies, GroupTypes, GroupBaseStats)
        #numOfTypes(GroupTypes,tierName = UserInput)

    def getBaseStats(self):  
        self.hp = (re.findall(r'hp:(.*?),',str(self.stats)))
        self.atk = (re.findall(r'atk:(.*?),',str(self.stats))) 
        self.defense = (re.findall(r'def:(.*?),',str(self.stats))) 
        self.spA = (re.findall(r'spa:(.*?),',str(self.stats)))   
        self.spD = (re.findall(r'spd:(.*?),',str(self.stats))) 
        spe = (re.findall(r'spe:(.*?),',str(self.stats)))
        self.spe = [x[:-1] for x in spe]

    def compareBaseStats(self):
        if (self.UserInput != None):
            self.sepTiers()
        self.getBaseStats()
        self.indices = []
        ourTypes = []
        for i in range(len(self.names)-1): #last pokemon is unrealistic, and ruins code :/
            if(int(self.hp[i]) > 120):
                self.indices.append(i)
            elif(int(self.atk[i]) > 120):
                self.indices.append(i)
            elif(int(self.defense[i]) > 120):
                self.indices.append(i)
            elif(int(self.spA[i]) > 120):
                self.indices.append(i)
            elif(int(self.spD[i]) > 120):
                self.indices.append(i)
            elif(int(self.spe[i]) > 120):
                self.indices.append(i)

        for i in range(len(self.indices)):
        #    self.cout(self.indices[i])
            ourTypes.append(self.types[i])
        
        self.numOfTypes(ourTypes)
            
            
    def cout(self,index):
        print(self.names[index] + ' ' + self.types[index])# + ' ' + self.tier[index])
        print('hp: ' + self.hp[index] + ' atk: ' + self.atk[index] + ' def: ' + self.defense[index] + ' spA: ' + self.spA[index] + 
              ' spD: ' + self.spD[index] + ' speed: ' + self.spe[index])
            

    def FindAdvantage(self):
        import matplotlib.pyplot as plt 
        from numpy import arange
        """So each advantage will gain the type one point of advantage, this gives us a way to classify which types
            we should have on our group of five, then we can find out which pokemon have these types in the area that
            we are interested in. Each strength will be +1, each weakness will be -1, and each immunity will be +2 for each 
            Pokemon of the specific type in our group. Strength/Weakness/immunity
            Normal - 0/2/1
            Fire - 4/4/0
            Water - 3/3/0
            Grass - 3/7/0
        Electric - 2/3/0
        Ice - 4/4/0
        Fighting - 5/5/0
        Poison - 2/4/0
        Ground - 5/2/1
        Flying - 3/3/1
        Psychic - 2/2/0
        Bug - 3/7/0
        Rock - 4/3/0
        Ghost - 2/1/2
        Dragon - 1/1/0
        Dark - 2/3/1
        Steel - 3/4/1
        Fairy - 3/3/1"""
        if (self.indices != 0):
            number = self.indices
        fireScore = (self.grass + self.ice + self.bug + self.steel - self.ground
                     - self.water - self.rock)
        waterScore = (self.fire + self.ground + self.rock - self.grass - self.electric)
        normalScore = self.ghost
        grassScore = (self.water + self.ground + self.rock - self.fire - 
                      self.ice - self.poison - self.flying - self.bug)
        elecScore = (self.water + self.flying - self.ground)
        iceScore = (self.grass + self.ground + self.flying + self.dragon - 
                    self.fire - self.fighting - self.rock - self.steel)
        fightScore = (self.normal + self.ice + self.rock + self.dark + 
                      self.steel - self.flying - self.psychic - self.fairy)
        poisonScore = (self.grass + self.fairy - self.ground - self.psychic)
        groundScore = (self.fire + (self.electric*2) + self.poison + self.rock 
                       - self.grass - self.water - self.ice)
        flyScore = (self.grass + self.fighting + self.bug + (self.ground) - 
                    self.electric - self.ice - self.rock)
        psychicScore = (self.fighting + self.poison - self.bug - self.ghost - self.dark)
        bugScore = (self.grass + self.psychic + self.dark - self.fire - self.flying
                     - self.rock)
        rockScore = (self.fire + self.ice + self.flying + self.bug - self.water
                     - self.grass - self.fighting - self.ground - self.steel)
        ghostScore = (self.normal + self.psychic + self.fighting - self.dark)
        dragScore = (-self.ice - self.fairy)
        darkScore = ((self.psychic*2) + self.ghost - self.fighting - self.bug - 
                     self.fairy)
        steelScore = (self.ice + self.rock + self.fairy + self.poison - self.fire
                      - self.fighting - self.ground)
        fairyScore = (self.fighting + (2*self.dragon) + self.dark - self.poison - self.steel)
        
        print("Fire: " + str(fireScore) + " Water: " + str(waterScore) + " Normal: " + str(normalScore) + 
              " Grass: " + str(grassScore) + " Electric: " + str(elecScore) + " Ice: " + str(iceScore) + 
              " Fighting: " + str(fightScore) + " Poison: " + str(poisonScore) + " Ground: " + str(groundScore) + 
              " Flying: " + str(flyScore) + " Psychic: " + str(psychicScore) + " Bug: " + str(bugScore) + 
              " Rock: " + str(rockScore) + " Ghost: " + str(ghostScore) + " Dragon: " + str(dragScore) + 
              " Dark: " + str(darkScore) + " Steel: " + str(steelScore) + " Fairy: " + str(fairyScore))
        data = (fireScore,waterScore,elecScore,groundScore,fightScore,
                    dragScore,poisonScore,darkScore,fairyScore,psychicScore,
                    grassScore,ghostScore,rockScore,bugScore,steelScore,normalScore,flyScore,iceScore)
        plt.bar(arange(18),data,0.50)
        plt.ylabel('Number of Pokemon')
        plt.xticks(arange(18), ('Fire', 'Water', 'Electric', 'Ground', 
                                    'Fighting','Dragon','Poison','Dark','Fairy','Psychic'
               ,'Grass','Ghost','Rock','Bug','Steel','Normal','Flying','Ice'),rotation=90)
    
        
        
        
#myPokemon = Pokemon('OU') 
myPokemon = Pokemon()
myPokemon.compareBaseStats() 
myPokemon.FindAdvantage()
#myPokemon.getBaseStats()                  
                
            
            
#numOfTypes(types)
#getBaseStats(stats)
#sepTiers('OU',tier,types,stats,names)
