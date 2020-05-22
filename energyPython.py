# -*- coding: utf-8 -*-
"""
Created on Fri May 22 08:44:48 2020

@author: deads
"""


import numpy as np
from math import pi,cos
from datetime import date
import matplotlib.pyplot as plt

"Wind - https://www.irena.org/wind"
"Nuclear - https://www.eia.gov/nuclear/outages/"
"Nuclear Cost - https://www.world-nuclear.org/information-library/economic-aspects/economics-of-nuclear-power.aspx"
"Solar - https://www.greenmatch.co.uk/blog/2014/11/how-efficient-are-solar-panels"
"Solar Cost - https://www.greenmatch.co.uk/blog/2014/08/what-is-the-installation-cost-for-solar-panels"
"Wind Cost - http://www.windustry.org/how_much_do_wind_turbines_cost"
"Cost to build plants  - https://marketrealist.com/2015/01/natural-gas-fired-power-plants-cheaper-build/"
class Energy:
    
    def __init__(self,angle,NumWind,day,month,year,effSolar,areaSolar,numWind,numNuclear,numWater):
        self.dn = np.arange(0,365)
        self.NumWind = NumWind
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
        
    def startup(self):
        self.Nuclear = 1100 #MW/generator
        self.NuclearCost = 7500000000 #dollars per reactor
        self.CommWind = 8 #MW/generator commercial
        self.LandWind = 2 #MW/generator inland
        self.SeaWind = 4 #3-5 MW/generator on sea
        self.solarEff = .20 #Can be anywhere from 15% - 40%
        self.SolarCost = 321.37 #dollars per meter squared solar(commerical could be cheaper)
        self.WindCost = 35000000 #dolars per commercial wind turbine. Higher for personal
         
        
    def SunIntensity(self):
        "first in lux then to watts/meter"
        #dn = date(self.year,self.month,self.day)
        numOfDays = self.dn.tolist()
        two = []
        self.LightIntensity = []
        for i in numOfDays:
            two.append(1 + 0.033412 * cos(2*pi*(i - 3)/365))
            self.LightIntensity.append(128000*two[-1]/105)
        "need to multiply by area to get our final watts/meter"
        plt.plot(numOfDays,self.LightIntensity)
        plt.xlabel("Days")
        plt.ylabel("Light intensity")
  
latitude = 30
NumberOfWindyDays = 150
day = 1
month = 1
year = 2020
effSolar = 0.30
areaSolar = 100 
NumberOfWind = 10
NumNuclear = 2
numWater = 2

      
myPower = Energy(latitude,NumberOfWindyDays,day,month,year,effSolar,areaSolar,NumberOfWind,NumNuclear,numWater)
#myPower = Energy()
myPower.startup()
myPower.SunIntensity()
        