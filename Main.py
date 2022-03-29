#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 18:58:23 2022

@author: louisswanepoel
"""
import pandas as pd
from datetime import date as d 
import DictionaryMethod as s

# Produces an array of the date from september until now 

Today = d.today()
DateArray = pd.date_range('17/09/2021', Today.strftime("%d/%m/%Y"))

print(DateArray)



for Day in range(0,len(DateArray)):
    
    
    #This is where you will put functions to change the attributes of the people in the class Person
    # Namely the attributes that effect infection status 
    
    if Day == 14:
        
        for Names,NamesInfo in s.Students.items(): #goes through the dictionary and finds students of the condition below and changes their values in the dictionary
            if  NamesInfo['Origin']=='China'  :
                NamesInfo['Date of Last Infection'] = str(DateArray[Day]) #applies their date of infection to the data frame
                while Day < Day + 14: # means that it changes back to S after 14 days NEED AMMEDNING
                    NamesInfo['Infection Status'] = 'I' #changes value to infected
        s.CreateCSVRawData(s.Students)        
       
                
             
# s.CreateCSVRawData(s.Students)            
            
        
        
        
    
    