# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 13:46:01 2022

@author: Ted Mellow
"""

import pandas as pd
from datetime import date as d 
import assignments as s
import Metrics as m
import random as r
import numpy as np
#import argparse as ap

StudentInfoDataFrame = m.CreateDataFrame()

def InfectRandomStudent(Day,DateRange):
    
    randomStudent = r.randint(0,s.PopulationSize-1)
    
    if s.StudentObjects[randomStudent].SIR == 'S':
        s.StudentObjects[randomStudent].SIR = 'I'  
        s.StudentObjects[randomStudent].DayInfected = ([DateRange[Day],Day])
        
def infected(Day , DateRange,S,I,R):
    
    # Number that defines how likely an infectious person is to infect the person they interact with
    N = 0.2
        
    
    for StudentNumber in range(s.PopulationSize):
        
        # Susceptible people 
        if s.StudentObjects[StudentNumber].SIR == 'S': 
            continue    
        
        # Infected people 
        elif s.StudentObjects[StudentNumber].SIR == 'I':
            
            # If a student has been infected for longer than 14 days they will recover and their date of recovery will be added to the attribute
            if (Day - s.StudentObjects[StudentNumber].DayInfected[-1] ) >= r.choice(np.random.normal(14,6, s.PopulationSize)):
                s.StudentObjects[StudentNumber].SIR = 'R'
                s.StudentObjects[StudentNumber].DayRecovered = [DateRange[Day],Day]
                continue
            else:
                
                # Iterating through the number of people this infected person runs into each day by multiplying social number with number of susceptible people 
                for SingleInfection in range(int(round(S[-1]*s.StudentObjects[StudentNumber].Social*N))):
                    
                    # Picks a student at random
                    randomStudent = r.randint(0,s.PopulationSize-1)
                                     
                    if s.StudentObjects[randomStudent].SIR == 'S':
                        s.StudentObjects[randomStudent].SIR = 'I'
                        
                        # Adds date of infection as attribute
                        s.StudentObjects[randomStudent].DayInfected = ([DateRange[Day],Day])
                    else:
                        continue            
            
        # Recovery time is 30 days       
        elif s.StudentObjects[StudentNumber].SIR == 'R':
            if (Day - s.StudentObjects[StudentNumber].DayRecovered[-1] ) >= r.choice(np.random.normal(30,3, s.PopulationSize)):
                s.StudentObjects[StudentNumber].SIR = 'S'
            else:
                s.StudentObjects[StudentNumber].SIR == 'R'
                      
        
            
        

    

