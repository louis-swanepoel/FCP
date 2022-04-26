#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 13:03:36 2022

@author: louisswanepoel
"""
# import names as nm
#from DictionaryMethod import Halls
from random import choices , randint , choice
import numpy as np
import csv

with open('names.txt' , 'r') as names:
        Names = (names.read().replace('\n' , ' ')).split(' ') # creates a list of names from a text file

Document = open('InitialConditions.csv') # imports the values from a csv
DocumentContents = csv.reader(Document)  
Rows = []
for row in DocumentContents:
    Rows.append(row)
Nations , NationWeight , InfWeight = [] , [] , [] 
for entry in Rows[1:]:
    if entry == []:
        break
    Nations.append(entry[0])
    NationWeight.append(float(entry[1]))
    InfWeight.append(float(entry[2]))
InfDict = {j:InfWeight[i] for i , j in enumerate(Nations)} 

###Initial conditions

Halls = ['East' , 'West' , 'North' , 'South']
HallWeight = [0.1 , 0.2 , 0.4 , 0.3]

Country = Nations
CountryWeight = NationWeight
CountryInfDict = InfDict

# Country = ['China' , 'US' , 'UK' , 'EU']
# CountryWeight = [.1 , .1 , .7 , .1]

# CountryInfDict = {'China':0.01 , 'UK':0.001 , 'US':0.002 , 'EU':.005} #infect % of individual nations

PopulationSize = 1000
Names = Names[:PopulationSize] #trims the names list - idk if necessary

Status = ['I' , 'S' ,'R' ]

Courses =[ 'STEM' , 'ARTS' ]

ParameterValuesDict = {}

ParameterValuesDict['Halls'] = Halls
ParameterValuesDict['Origin'] = Country
ParameterValuesDict['Name'] = Names
ParameterValuesDict['Course'] = Courses



###Initial Allocations
def Jokes(subject):
    if subject == 'STEM':
        return 0
    else:
        return 2   ##Unsure if we carry this into final version 

def InfStatus(Nation):
    affected = CountryInfDict[Nation]
    InfWeight = [affected , 1-affected , 0] #Currently starts of w/ a recovered rate of 0
    InfList = choices(Status , InfWeight )
    return InfList[0]  #The zero indices is used to prevent a list of length 1 being returned

class Person:
    def __init__(self, StudentNumber ):
        self.StudentNumber = (StudentNumber)
        self.Halls = choices(Halls, HallWeight)[0]
        self.Origin = choices(Country, CountryWeight)[0]
        self.Name = Names[StudentNumber]
        self.SIR = InfStatus(self.Origin) 
        self.Course = choice(Courses)
        
        # Performs a normal distribution and adds it to an array and picks a nunber in this so that there is a spread of sociability
        self.Social = choice(np.random.normal(4,1, 1000)) # min(randint(1,10)+Jokes(self.Course) , 10) #Used to determine n# of non uni interactions
        self.DayInfected = [0,0]
        self.DayRecovered = [0,0]

StudentObjects = [Person (i) for i in range(PopulationSize)] #Allocates every student a number

#print(vars(StudentObjects[100]))
    
    
