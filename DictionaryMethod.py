#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 13:03:36 2022

@author: louisswanepoel
"""
# import names as nm
import pandas as pd 
    
Names = []
        
with open("names.txt", "r") as NamesTxt:
    lines = NamesTxt.read().split('\n')
for line in lines:
    Names.append(line)

# Independent parameters that do not change 
Halls = ['east','west','south','north']
Origin = ['China', 'England', 'USA', 'Mexico','Australia']


Students = {}
counter = 0  
while counter <= 1000: # Limits the population size under investigation 
    for Name in Names:
        NameInfo = {}
        counter += 1
        
        # Code below iterates through each name and for each name it assigns values to the parameter
        # origin or halls , nore can be added 
        #
        
        # halls assingment
        if counter <= 120:        
            NameInfo['Hall']= Halls[0]
        elif 120 < counter <= 400:
            NameInfo['Hall']= Halls[1]
        elif 400 < counter <= 600:
            NameInfo['Hall']= Halls[2]
        elif 600 < counter <= 1000:
            NameInfo['Hall']= Halls[3]  
        else:
             print('Halls assignment error') 
             break
         # origin assingment
        if counter%5 == 0:        
            NameInfo['Origin'] = Origin[0]
        elif counter%5 == 1:
            NameInfo['Origin'] = Origin[1]
        elif counter%5 == 2:
            NameInfo['Origin'] = Origin[2]
        elif counter%5 == 3:
            NameInfo['Origin'] = Origin[3]
        elif counter%5 == 4:
            NameInfo['Origin'] = Origin[4]
        else:
            print('Origin assignment error')
            break
        
        
        Students[Name] = dict(NameInfo)


PopulationIndependentData = pd.DataFrame(Students)

# PopulationIndependentData.style

print(PopulationIndependentData)

PopulationIndependentData.to_csv('RawIndependentPopData.csv', index=True)
PopulationIndependentData.to_excel('RawIndependentPopDataCSV.xlsx', index=True)