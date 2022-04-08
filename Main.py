#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 18:58:23 2022

@author: louisswanepoel
"""
import pandas as pd
from datetime import date as d 
import assignments as s
import argparse as ap
import Metrics as m


Today = d.today()
DateRange= pd.date_range('17/09/2021', Today.strftime("%d/%m/%Y"))
# Produces an array of the date from september until now 

SIRSeries = pd.DataFrame(DateRange, columns=['Date'])

S = []
I = []
R = []

for Day in range(0,len(DateRange)):
                   
    SIRvalsToday = m.CollectSIRdata()
    S.append(SIRvalsToday[0])
    I.append(SIRvalsToday[1])
    R.append(SIRvalsToday[2])
    
    if Day == 20:
        StudentInfoDataFrameFiltered,SIRvalsForFilter = m.SIRinfoFilter('I','UK',None,None,'STEM')
        
    
SIRSeries['S'] = S
SIRSeries['I'] = I           
SIRSeries['R'] = R


           

InfectionsAgainstTime = m.lineGraph(SIRSeries)
     
InfectionsAgainstTime.show()   
          
            
        
        
        
    
    