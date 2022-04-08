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
import Functions as f
import matplotlib.pyplot as plt
import plotly.express as px

# Todays Date 
Today = d.today()

# Produces an array of the date from september until now to intiate the SIR time series 
DateRange= pd.date_range('17/09/2021', Today.strftime("%d/%m/%Y"))

# Creater the SIR time series from the start of universirty 2021 until now
SIRSeries = pd.DataFrame(DateRange, columns=['Date'])

# Empty lists to collect people of SIR statuses respectively 
S = []
I = []
R = []

# Going through each days until now 
for Day in range(0,len(DateRange)):
    
    # Holidays only add the data and do not change the infection numbers
    if Day in range (30,37):
        
        # Collects whatever data you want at the start of the reading week 1
        if Day == 30:
            
            #Calling function SIRinfofilter to find out who was infected in the onrth halls at the start of the reading week 
            ReadingWeek1Data = m.SIRinfoFilter('I', None, None, 'North', None)
        
        SIRvalsToday = m.CollectSIRdata()
        S.append(SIRvalsToday[0])
        I.append(SIRvalsToday[1])
        R.append(SIRvalsToday[2])
    
        # Christomas hols
    elif Day in range (70,100):
        
        # Collects whatever data you want at the start of the Christmas holidays
        if Day == 70:
            
            ChristmasData = m.SIRinfoFilter('I', None, None, 'North', None)
            
        SIRvalsToday = m.CollectSIRdata()
        S.append(SIRvalsToday[0])
        I.append(SIRvalsToday[1])
        R.append(SIRvalsToday[2])
        
    elif Day in range (110,117):
        
        # Collects whatever data you want at the start of the reading week 2
        if Day == 110:
            ReadingWeek2Data = m.SIRinfoFilter(None, None, None, None, None)
            
        SIRvalsToday = m.CollectSIRdata()
        S.append(SIRvalsToday[0])
        I.append(SIRvalsToday[1])
        R.append(SIRvalsToday[2])
    
    # Week days add normal infecton data            
    elif 0<= Day%7 <=5:
        
        for StudentNumber in range(s.PopulationSize):
            f.infected(StudentNumber, Day , DateRange)         
          
        SIRvalsToday = m.CollectSIRdata()
        S.append(SIRvalsToday[0])
        I.append(SIRvalsToday[1])
        R.append(SIRvalsToday[2])
    
    # Weekends add an extra 2 people to everyones social number
    elif 6<= Day%7 <=7:
        
        for StudentNumber in range(s.PopulationSize):
            
            s.StudentObjects[StudentNumber].Social = (s.StudentObjects[StudentNumber].Social) +2
            f.infected(StudentNumber, Day , DateRange)     
            s.StudentObjects[StudentNumber].Social = (s.StudentObjects[StudentNumber].Social) -2
          
        SIRvalsToday = m.CollectSIRdata()
        S.append(SIRvalsToday[0])
        I.append(SIRvalsToday[1])
        R.append(SIRvalsToday[2])
    
SIRSeries['S'] = S
SIRSeries['I'] = I           
SIRSeries['R'] = R


SIRSeries.set_index('Date',inplace=True)
print(SIRSeries)
SIRSeries.plot()

print(ReadingWeek1Data)

# SIRSeries.pivot(index='Date', columns='SIR', values='y')
 
# SIRSeries.plot(SIR=SIRSeries.columns, figsize=(5, 3))       

# InfectionsAgainstTime = m.lineGraph(SIRSeries)
     
# InfectionsAgainstTime.show()   
          
            
        
        
        
    
    