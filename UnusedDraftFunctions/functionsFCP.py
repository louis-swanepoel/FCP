# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 17:54:48 2022

@author: xd217

"""
from random import randint
def Allocate(PopulationList , AffectedPercentage):
    Blank = [PopulationList]
    AffectedGroup = [] #The list of people allocated with that quality
    PopulationSize = len(PopulationList) # population we are iterating through
    Proportion  = AffectedPercentage/100 #Proportion of population with quality 
    NumberEffected = round(PopulationSize*Proportion) #expected number of cases
    Interval = round(1/Proportion) # the interval
    
    # for i in range(1,PopulationSize): #used to create a list to temporarily
    #     Blank.append(str(i))
    
    Constant = randint(1 , NumberEffected)   #the offset used to add some randomness to the group returned
    
    for i in range(0, NumberEffected):
        Position = Constant + i*Interval
        AffectedGroup.append(Blank[Position])
    return AffectedGroup
    