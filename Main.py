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
import random as r

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
        
        # Each time this is called it collects the data and adds it to the time series 
        SIRvalsToday = m.CollectSIRdata()
        S.append(SIRvalsToday[0])
        I.append(SIRvalsToday[1])
        R.append(SIRvalsToday[2])
                
        # Collects whatever data you want at the start of the reading week 1
        if Day == 31:
            
            # Randomly Infects 10 percent of the pupolation when they travel home - this function can be tailored to wight certain ethnicities 
            for StudentNumber in range(round(s.PopulationSize/10)):                 
                    f.InfectRandomStudent(Day,DateRange)
                    
            #Calling function SIRinfofilter to find out who was infected in the onrth halls at the start of the reading week 
            ReadingWeek1Data = m.SIRinfoFilter(None, None, None, 'North', None)
        continue
            
        # Christomas hols
    if Day in range (100,150):        
        SIRvalsToday = m.CollectSIRdata()
        S.append(SIRvalsToday[0])
        I.append(SIRvalsToday[1])
        R.append(SIRvalsToday[2])        
        if Day == 145:           
            for StudentNumber in range(round(s.PopulationSize/5)):                   
                   f.InfectRandomStudent(Day,DateRange)                    
        elif Day == 102:
            
            # Collects whatever data you want at the start of the Christmas holidays
            ChristmasData = m.SIRinfoFilter('I', None, None, 'North', None)     
        continue    
    if Day in range (200,230):        
        SIRvalsToday = m.CollectSIRdata()
        S.append(SIRvalsToday[0])
        I.append(SIRvalsToday[1])
        R.append(SIRvalsToday[2])
        
        # Collects whatever data you want at the start of the reading week 2
        if Day == 225:            
            for StudentNumber in range(round(s.PopulationSize/5)):                 
                    f.InfectRandomStudent(Day,DateRange)                   
            ReadingWeek2Data = m.SIRinfoFilter(None, None, None, None, None)
        continue
     
    # Week days add normal infecton data            
    if 0<= Day%7 <=5:
        
        SIRvalsToday = m.CollectSIRdata()
        S.append(SIRvalsToday[0])
        I.append(SIRvalsToday[1])
        R.append(SIRvalsToday[2])               
        f.infected( Day , DateRange)           
        continue
    
    # Weekends add an extra 2 people to everyones social number
    elif 6<= Day%7 <=7:       
        SIRvalsToday = m.CollectSIRdata()
        S.append(SIRvalsToday[0])
        I.append(SIRvalsToday[1])
        R.append(SIRvalsToday[2])       
        for StudentNumber in range(s.PopulationSize):            
            s.StudentObjects[StudentNumber].Social = (s.StudentObjects[StudentNumber].Social) +2                  
        f.infected( Day , DateRange)         
        for StudentNumber in range(s.PopulationSize):
            s.StudentObjects[StudentNumber].Social = (s.StudentObjects[StudentNumber].Social) -2            
        continue   
SIRSeries['S'] = S
SIRSeries['I'] = I           
SIRSeries['R'] = R

#  Look at certain periods of time
SIRSeries = SIRSeries.drop(labels=range(130, 322 ), axis=0)



SIRSeries.set_index('Date',inplace=True)
SIRSeries.plot()

print(ReadingWeek1Data)

# SIRSeries.pivot(index='Date', columns='SIR', values='y')
 
# SIRSeries.plot(SIR=SIRSeries.columns, figsize=(5, 3))       

# InfectionsAgainstTime = m.lineGraph(SIRSeries)
     
# InfectionsAgainstTime.show()   
          
            
        
        
        
    
    