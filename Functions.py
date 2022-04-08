# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 13:46:01 2022

@author: Ted Mellow
"""

from re import S
import pandas as pd
from datetime import date as d 
import assignments as s
import Metrics as m
import random as r
import numpy as np
#import argparse as ap

StudentInfoDataFrame = m.CreateDataFrame()


def infected(Day , DateRange):
    
    # Collects SIR data to determine interactions
    proportionsSIR= m.CollectSIRdata()    
    
    for StudentNumber in range(s.PopulationSize):
        
        # Susceptible people 
        if s.StudentObjects[StudentNumber].SIR == 'S': 
            None    
        
        # Infected people 
        elif s.StudentObjects[StudentNumber].SIR == 'I':
            
            # If a student has been infected for longer than 14 days they will recover and their date of recovery will be added to the attribute
            if (Day - s.StudentObjects[StudentNumber].DayInfected[-1] ) >= r.choice(np.random.normal(14,3, s.PopulationSize)):
                s.StudentObjects[StudentNumber].SIR = 'R'
                s.StudentObjects[StudentNumber].DayRecovered = [DateRange[Day],Day]
            else:
                
                # Iterating through the number of people this infected person runs into each day by multiplying social number with number of susceotible people 
                for SingleInfection in range(round(proportionsSIR[0]*s.StudentObjects[StudentNumber].Social)):
                    
                    # Picks a student at random
                    Student = r.randint(0,s.PopulationSize-1)
                                     
                    if s.StudentObjects[Student].SIR == 'S':
                        s.StudentObjects[Student].SIR = 'I'
                        
                        # Adds date of infection as attribute
                        s.StudentObjects[Student].DayInfected = ([DateRange[Day],Day])
                    else:
                        None
            
            
        # Recovery time is 30 days       
        elif s.StudentObjects[StudentNumber].SIR == 'R':
            if (Day - s.StudentObjects[StudentNumber].DayRecovered[-1] ) >= r.choice(np.random.normal(30,3, s.PopulationSize)):
                s.StudentObjects[StudentNumber].SIR = 'S'
            else:
                s.StudentObjects[StudentNumber].SIR == 'R'
                
               
        
            
        
        
            
        
    # return d.today() as DateOfInfection
    
# def recovered(Infected, DateOfInfection):
    
#     if Infected == 1:
        
#         if DateOfInfection + 14 < d.today(): #current time
#             student.SIR == 'I'    
#         else:
#             student.SIR =='R' #returns R for recovered
#     else:
#         student.SIR =='S'
    
# for student in s.studentobjects():
#     if student.SIR == 'S':
#         student.SIR = infected(student) 
#     elif student.SIR =='I':
#         student.SIR = recovered(student)
#     else:
#         student.SIR = recovered(student)
    

