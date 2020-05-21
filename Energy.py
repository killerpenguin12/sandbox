# -*- coding: utf-8 -*-
"""
Created on Fri May 15 14:58:50 2020

@author: deads
"""


import numpy as np
from math import pi,cos
from datetime import date

"Wind - https://www.irena.org/wind"
"Nuclear - https://www.eia.gov/nuclear/outages/"
"Nuclear Cost - https://www.world-nuclear.org/information-library/economic-aspects/economics-of-nuclear-power.aspx"
"Solar - https://www.greenmatch.co.uk/blog/2014/11/how-efficient-are-solar-panels"
"Solar Cost - https://www.greenmatch.co.uk/blog/2014/08/what-is-the-installation-cost-for-solar-panels"
"Wind Cost - http://www.windustry.org/how_much_do_wind_turbines_cost"
class Energy:
    
    def _init_(self,angle,NumWind,day,month,year,effSolar,effWind,areaSolar,areaWind,numNuclear,numWater):
        self.dn = np.arange(0,365)
        self.NumWind = NumWind
        self.angle = angle
        self.effSolar = effSolar
        self.effWind = effWind
        self.areaSolar = areaSolar
        self.areaWind = areaWind
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
        two = (1 + 0.033412 * cos(2*pi*(self.dn - 3)/365))
        E = 128000*two
        "need to multiply by area to get our final watts/meter"
        self.LightIntensity = E/105
    
    
        
        