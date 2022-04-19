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
Today = Today.strftime("%d/%m/%Y")
CustomDate = '17/09/2022' 

# Produces an array of the date from september until now to intiate the SIR time series 
DateRange= pd.date_range('17/09/2021', CustomDate)

# Day when you want data collected- TESTING TO SEE IF DAY OF DATA COLLECTION CAN BE SELECTED BY THE USER
# CollectDataDay = input('as %d-%m-%Y 00:00:00, input the date you want data collected:')
# counter = 0
# for date in DateRange:
#     counter += 1
#     if date == CollectDataDay:
#         CollectDataDay = counter
#         continue

dataCollection = input('would you like to collect any other data? yes/no ')


if dataCollection == 'yes':
    CollectDataDay = int(input('What day would you like the data collected '))
else:   
    CollectDataDay = -1
        
# Creater the SIR time series from the start of universirty 2021 until now
SIRSeries = pd.DataFrame(DateRange, columns=['Date'])

# Empty lists to collect people of SIR statuses respectively 
S = []
I = []
R = []

# Going through each days until now 
for Day in range(0,len(DateRange)):
    
    # Collecting Data example 
    m.BarChartHalls(Day, DateRange, CollectDataDay)
    m.BarChartCountries(Day, DateRange,CollectDataDay)
    
    # Holidays only add the data and do not change the infection numbers
    if Day in range (30,37):
        
        # Each time this is called it collects the data and adds it to the time series 
        m.CollectSIRdata(S,I,R)
                
        # Collects whatever data you want at the start of the reading week 1
        if Day == 31:            
            
            # Randomly Infects 10 percent of the pupolation when they travel home - this function can be tailored to wight certain ethnicities 
            for StudentNumber in range(0,round(s.PopulationSize/20)):                 
                    f.InfectRandomStudent(Day,DateRange)
        else:
            continue
            
        # Christomas hols
    elif Day in range (90,120):        
        m.CollectSIRdata(S,I,R)               
        if Day == 118:           
            for StudentNumber in range(0,round(s.PopulationSize/90)):                   
                   f.InfectRandomStudent(Day,DateRange)                    
        elif Day == 119:         
           
            # Collects whatever data you want at the start of the Christmas holidays- if you want data on a day other than a collect data day then call today as the collectdataday
            ChristmasData = m.SIRinfoFilter('I', None, None, None, None, Day,Day)     
        else:
            continue    
        
    #   Easter hols
    elif Day in range (200,214):        
        m.CollectSIRdata(S,I,R)
        
        # Collects whatever data you want at the start of the reading week 2
        if Day == 213:            
            for StudentNumber in range(0,round(s.PopulationSize/17)):                 
                    f.InfectRandomStudent(Day,DateRange)                   
            ReadingWeek2Data = m.SIRinfoFilter('I', None, None, None, None,Day,Day)
        else:
            continue
    else:
        
        # Week days add normal infecton data            
        if 0<= Day%7 <=5:            
            m.CollectSIRdata(S,I,R)               
            f.infected( Day , DateRange,S,I,R)           
            continue
        
        # Weekends add an extra 2 people to everyones social number
        elif 6<= Day%7 <=7:       
            m.CollectSIRdata(S,I,R)       
            for StudentNumber in range(s.PopulationSize):            
                s.StudentObjects[StudentNumber].Social = (s.StudentObjects[StudentNumber].Social) +2                  
            f.infected( Day , DateRange,S,I,R)         
            for StudentNumber in range(s.PopulationSize):
                s.StudentObjects[StudentNumber].Social = (s.StudentObjects[StudentNumber].Social) -2              
            continue   
    
SIRSeries['S'] = S
SIRSeries['I'] = I           
SIRSeries['R'] = R
SIRSeries.set_index('Date',inplace=True)


#  Look at certain periods of time
# SIRSeries = SIRSeries.drop(labels=range(200, 365 ), axis=0)

m.MainTimeSeriesPlot(SIRSeries)




plt.show

# SIRSeries.pivot(index='Date', columns='SIR', values='y')
 
# SIRSeries.plot(SIR=SIRSeries.columns, figsize=(5, 3))       

# InfectionsAgainstTime = m.lineGraph(SIRSeries)
     
# InfectionsAgainstTime.show()   
          
            
        
        
        
    
    