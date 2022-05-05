#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 18:58:23 2022

@author: louisswanepoel
"""
import pandas as pd
from datetime import date as d 
import Assignments as s
import argparse as ap
import Metrics as m
import Functions as f
import matplotlib.pyplot as plt
import plotly.express as px
import random as r
import numpy as np

# Todays Date 
Today = d.today()
Today = Today.strftime("%d/%m/%Y")
    
# Produces an array of the date from september until now to intiate the SIR time series 
DateRange= pd.date_range('17/09/2021', Today)

# Creater the SIR time series from the start of university 2021 until now
SIRSeries = pd.DataFrame(DateRange, columns=['Date'])

# Empty lists to collect people of SIR statuses respectively 
S = []
I = []
R = []

# Going through each days until now 
for Day in range(0,len(DateRange)):
    
    # Data collection functions 
    m.BarChartHalls(Day, DateRange, s.Day[0])
    m.BarChartCountries(Day, DateRange,s.Day[2])
    m.BarChartCourse(Day, DateRange, s.Day[1])
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
        
        # Weekends adds extra people to everyones social number
        elif 6<= Day%7 <=7:       
            m.CollectSIRdata(S,I,R)       
            for StudentNumber in range(s.PopulationSize):            
                Library = 2 # adds 2 people
                Home = 0 # adds 0 people
                Coffeeshop = 2 # adds 2 people
                Exercise = 1 # adds 1 person
                Friends = 3 #adds 3 people
                Clubs = 4 # adds 4 people
                Restaurants = 2 # adds 2 people
                Parties = 4 # adds 4 people
                StudyTime = [Library, Home, Coffeeshop] # places to study list
                Hobbies = [Exercise, Friends, Home] # activities/hobbies list
                Nightlife = [Clubs, Restaurants, Parties, Home] # nightlife places list for weekends
                WStudyTime = [True, False] # WeekEnd StudyTime
                ChoiceWS = np.random.choice(WStudyTime, p=[0.7,0.3]) # A weighted assumed choice whether someone studies on the weekend (70% YES/ 30% NO)
                if ChoiceWS == True: 
                    s.StudentObjects[StudentNumber].Social = np.random.choice(StudyTime, p=[0.5, 0.2, 0.3]) + np.random.choice(Hobbies, p=[0.4, 0.4, 0.2]) + np.random.choice(Nightlife, p=[0.25,0.2,0.4,0.15]) # assigns each person a social value
                else:
                    s.StudentObjects[StudentNumber].Social = np.random.choice(Hobbies, p=[0.4, 0.4, 0.2]) + np.random.choice(Hobbies, p=[0.4, 0.4, 0.2]) + np.random.choice(Nightlife, p=[0.25,0.2,0.4,0.15]) #if someone does not study over the weekend then 2x hobbies higher social value
                                        
            f.infected( Day , DateRange,S,I,R) 
        
# Formats the SIR vals for plotting into a time series 
SIRSeries['S'] = S
SIRSeries['I'] = I           
SIRSeries['R'] = R
SIRSeries.set_index('Date',inplace=True)

# Function that plots the main SIR time series for the whole simulation
if s.PlotOrNot[3] == 'TRUE':
    m.MainTimeSeriesPlot(SIRSeries)
else:
    print('Simulation finished')

# Creates an excel file in the directory with all the attributes of the population 
m.SaveMainDataframeOfAttributes()                 


          
            
        
        
        
    
    