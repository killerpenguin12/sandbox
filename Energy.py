# -*- coding: utf-8 -*-
"""
Created on Fri May 22 08:44:48 2020

@author: deads
"""


import numpy as np
from math import pi,cos,sin,pow,asin,radians
from datetime import date
import matplotlib.pyplot as plt
from random import randrange

"Wind - https://www.irena.org/wind"
"Nuclear - https://www.eia.gov/nuclear/outages/"
"Nuclear Cost - https://www.world-nuclear.org/information-library/economic-aspects/economics-of-nuclear-power.aspx"
"Solar - https://www.greenmatch.co.uk/blog/2014/11/how-efficient-are-solar-panels"
"Solar Cost - https://www.greenmatch.co.uk/blog/2014/08/what-is-the-installation-cost-for-solar-panels"
"Wind Cost - http://www.windustry.org/how_much_do_wind_turbines_cost"
"Cost to build plants  - https://marketrealist.com/2015/01/natural-gas-fired-power-plants-cheaper-build/"
"solar insolation - https://www.pveducation.org/pvcdrom/properties-of-sunlight/calculation-of-solar-insolation"
"cost of silicon,energywise  - https://www.crmalliance.eu/silicon-metal"
"1.5kg of silicon per 1m panel solar"
"per 907kg silicon: 1,360 kg of coal and 13MW per ton(0.014MW per kg)"
"770 kg of coal for one 907kg of steel"
"coal energy/kg = 2.4KwHours"
"200 tons of steel per wind turbine, 181,400 kg of steel"
"27 tons of uranium per year, 24,489kg of uranium"
class Energy:
    
    def __init__(self,angle,NumWindDays,day,month,year,effSolar,areaSolar,numWind,numNuclear,numWater,years):
        self.dn = np.arange(0,365*years)
        self.NumWindDays = NumWindDays
        self.angleRad = angle * pi/180
        self.angle = angle
        self.effSolar = effSolar
        #self.effWind = effWind
        self.areaSolar = areaSolar
        #self.areaWind = areaWind
        self.numWind = numWind
        self.numNuclear = numNuclear
        self.numWater = numWater
        self.day = day
        self.month = month
        self.year = year
        self.years = years
        
    def startup(self):
        self.Nuclear = 1100 #MW/generator
        self.NuclearCost = 7500000000 #dollars per reactor
        self.CommWind = 8 #MW/generator commercial
        self.LandWind = 2 #MW/generator inland
        self.SeaWind = 4 #3-5 MW/generator on sea
        self.solarEff = .20 #Can be anywhere from 15% - 40%
        self.SolarCost = 321.37 #dollars per meter squared solar(commerical could be cheaper) 100$
        self.WindCost = 35000000 #dolars per commercial wind turbine. Higher for personal
        self.EcostWind = (181400*770/907) * 2.4/1000 #kg of coal and how much power that is(MWh)
        self.EcostSolar = 0.014 * 1.5 + (1.5 * 1360/907 * 2.4/1000) #second is MWh and first is MW so....
         
        
    def SunIntensity(self):
        "first in lux then to watts/meter"
        #dn = date(self.year,self.month,self.day)
        numOfDays = self.dn.tolist()
        two = []
        self.LightIntensity = []
        Id = 1.353 * pow(0.7,(pow(1/cos(30),0.678)))
        print(Id)
        
        for i in numOfDays:
            two.append(1 + 0.033412 * cos(2*pi*(i - 3)/365))
            "need to multiply by area to get our final watts/meter"
            
            decl = 23.45 * sin((360/365) * (284 + i))
            #beta = asin(sin(decl)*sin(self.angleRad) + cos(decl)*cos(self.angleRad))
            alpha = 90 - self.angle + decl
            self.LightIntensity.append((128000*two[-1]/105))# * sin(radians(alpha)))
            #Id.append(1.353 * 0.7**(sec(self.angleRad)**(0.678)))
        plt.plot(numOfDays,self.LightIntensity)
        plt.xlabel("Days")
        plt.ylabel("Light intensity")
        plt.show()
        
    def PossiblePower(self):
        power = sum(self.LightIntensity)/len(self.LightIntensity) * self.solarEff 
        powerSolar = power*self.solarEff*self.areaSolar  
        powerNuclear = self.Nuclear * self.numNuclear * self.dn[-1]
        powerWind = self.LandWind * self.numWind * self.dn[-1]
        plt.figure(1)
        plt.title("Power of different sources")
        plt.ylabel('MW of power generated per year(capacity)')
        plt.xticks(np.arange(3),('Solar','Nuclear','Wind'))
        plt.bar(np.arange(3),(powerSolar,powerNuclear,powerWind))
        #plt.figure(2)
        plt.show()
        
    
    def Cost(self):
         costSolar = self.SolarCost*self.areaSolar
         costNuclear = self.NuclearCost * self.numNuclear
         costWind = self.WindCost * self.numWind
         plt.bar(np.arange(3),(costSolar,costNuclear,costWind))
         plt.xticks(np.arange(3),('Solar','Nuclear','Wind'))
         plt.ylabel('US Dollars')
         plt.title('Cost of amount of generators')
         plt.show()
        
    def breakEven(self):
        powerSolar = [x * self.solarEff for x in self.LightIntensity]
        arrayOfWindDays = np.zeros(365*self.years).tolist()
        numOfDays = self.dn.tolist()
        while sum(arrayOfWindDays) < self.NumWindDays:
            i = randrange(0,len(arrayOfWindDays))
            arrayOfWindDays[i] = 1
        powerWind = [x * self.LandWind for x in arrayOfWindDays]
        powerWindBASE = []
        powerSolarBASE = []
        powerSECost = []
        powerWECost = []
        for i in range(len(numOfDays)):
            powerSECost.append(self.EcostSolar*self.areaSolar)
            powerWECost.append(self.EcostWind*self.numWind)
        for i in range(len(arrayOfWindDays)):
            j = 0
            PowerSum = 0
            PowerSum2 = 0
            while j < i:
                #trying to add the power of wind so that we have an increasing graph.
                #so each 
                PowerSum += powerWind[j]
                PowerSum += powerSolar[j]
                j += 1
            powerWindBASE.append(PowerSum)
            powerSolarBASE.append(PowerSum2)
       
        plt.figure(1)
        plt.xlabel("Days")
        plt.ylabel("MW required")
        plt.plot(numOfDays,powerWindBASE,label='Wind Power')
        plt.plot(numOfDays,powerWECost,label='Wind Energy Cost')
        plt.legend()
        plt.show()
        plt.figure(2)
        plt.plot(numOfDays,powerSolarBASE,label='Solar Power')
        plt.plot(numOfDays,powerSECost,label='Solar Energy Cost')
        plt.legend()
        
  
latitude = 40
NumberOfWindyDays = 150
day = 1
month = 1
year = 2020
effSolar = 0.30
areaSolar = 10000
NumberOfWind = 100
NumNuclear = 1
numWater = 2
years = 4

      
myPower = Energy(latitude,NumberOfWindyDays,day,month,year,effSolar,areaSolar,NumberOfWind,NumNuclear,numWater,years)
#myPower = Energy()
myPower.startup()
myPower.SunIntensity()
myPower.PossiblePower()
myPower.Cost()
myPower.breakEven()


        
