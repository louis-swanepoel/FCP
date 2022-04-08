#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 13:03:36 2022

@author: louisswanepoel
"""
# import names as nm
import pandas as pd 
import random as r
import assignments as s


# Function to create dataframe of students information  -- returns dataframe of all the students attributes 
def CreateDataFrame():
    
    # Creation of empty variable list to append column headings
    Columns = []

    # Create empty dictionary for values of each column for each student
    StudentsDict = {}

    # Iterates through the attributes of each student defined by the Person class and assigns an empty list to each one
    for keys, values in vars(s.StudentObjects[0]).items():
        Columns.append(keys)
        StudentsDict[keys] = []

    # Iterate through Student Numbers 
    for StudentNumber in range(s.PopulationSize):  

        # Extract student as an object 
        StudentInfo = s.StudentObjects[StudentNumber]

        # Extract student attributes iteratively and add to the list which is a value of the attribute key
        for column in Columns:
            value = getattr(StudentInfo, column)
            StudentsDict[column].append(value) 
            
     # Convert dictionary into a pandas dataframe 
    StudentInfoDataFrame = pd.DataFrame(StudentsDict) 
    
    return StudentInfoDataFrame


# Function to collect SIR data for population -- returns a dataframe of proportiona and frequency against SIR 
def CollectSIRdata():
    # Create Lists to collect S, I and R statuses in bins 
    Slist = []
    Ilist = []
    Rlist = []
    
    # Iterate through each student
    for StudentNumber in range(s.PopulationSize):
        
        # Add each students SIR status to the correct bin so now the bins have collected all students
        if s.StudentObjects[StudentNumber].SIR == 'S':
            Slist.append(s.StudentObjects[StudentNumber].SIR)        
        elif s.StudentObjects[StudentNumber].SIR == 'I':
            Ilist.append(s.StudentObjects[StudentNumber].SIR)
        elif s.StudentObjects[StudentNumber].SIR == 'R':
            Rlist.append(s.StudentObjects[StudentNumber].SIR)
        else:
            raise ValueError('Student must have an SIR value')
            
    # Tally up frequency of each bin to find out how many people are S, I OR R
    todaysFrequencyS = len(Slist)
    todaysFrequencyI = len(Ilist)
    todaysFrequencyR = len(Rlist)
    
    # Find Proportion
    todaysProportionS = todaysFrequencyS/s.PopulationSize
    todaysProportionI = todaysFrequencyI/s.PopulationSize
    todaysProportionR = todaysFrequencyR/s.PopulationSize
                
    ## Creation of a dictionary holding SIR proportion/frequencies 
    # informationDictSIR = {'S':{"Proportion":todaysProportionS , 'Frequency' : todaysFrequencyS } , 
    #                       'I':{"Proportion":todaysProportionI , 'Frequency' : todaysFrequencyI } , 
    #                      'R':{"Proportion":todaysProportionR , 'Frequency' : todaysFrequencyR }  }
    
    ## Dataframe of SIR preportions in first row
    # dailyDataSIR = pd.DataFrame(informationDictSIR)
    
    # Creation of a matrix of SIR proportions in total population
    proportionsSIR = [todaysProportionS,todaysFrequencyI,todaysProportionR]
    
    return proportionsSIR
      
   
# returns--  SIRlistNorth, SIRlistEast, SIRlistSouth , SIRlistWest where each is a nested list of SIR data 
def DailyDataSIR():
    
    # Create Lists to collect S, I and R statuses in bins 
    SlistPop = []
    IlistPop = []
    RlistPop = []
    
        
    # List of SIR for each halls 
    SIRlistNorth = [[],[],[]]
    SIRlistEast = [[],[],[]]
    SIRlistWest = [[],[],[]]
    SIRlistSouth = [[],[],[]]

    # Iterate through each student
    for StudentNumber in range(s.PopulationSize):

        # Add each students SIR status to the correct bin so now the bins have collected all students
        if s.StudentObjects[StudentNumber].SIR == 'S':
            SlistPop.append(s.StudentObjects[StudentNumber]) 

            if s.StudentObjects[StudentNumber].Halls == 'North':
                SIRlistNorth[0].append(s.StudentObjects[StudentNumber])           
            elif s.StudentObjects[StudentNumber].Halls == 'East':
                SIRlistEast[0].append(s.StudentObjects[StudentNumber])
            elif s.StudentObjects[StudentNumber].Halls == 'West':
                SIRlistWest[0].append(s.StudentObjects[StudentNumber])
            elif s.StudentObjects[StudentNumber].Halls == 'South':
                SIRlistSouth[0].append(s.StudentObjects[StudentNumber])
            else:
                ValueError('Student must have an SIR value')


        elif s.StudentObjects[StudentNumber].SIR == 'I':
            IlistPop.append(s.StudentObjects[StudentNumber])

            if s.StudentObjects[StudentNumber].Halls == 'North':
                SIRlistNorth[1].append(s.StudentObjects[StudentNumber])           
            elif s.StudentObjects[StudentNumber].Halls == 'East':
                SIRlistEast[1].append(s.StudentObjects[StudentNumber])
            elif s.StudentObjects[StudentNumber].Halls == 'West':
                SIRlistWest[1].append(s.StudentObjects[StudentNumber])
            elif s.StudentObjects[StudentNumber].Halls == 'South':
                SIRlistSouth[1].append(s.StudentObjects[StudentNumber])
            else:
                ValueError('Student must have an SIR value')

        elif s.StudentObjects[StudentNumber].SIR == 'R':
            RlistPop.append(s.StudentObjects[StudentNumber])

            if s.StudentObjects[StudentNumber].Halls == 'North':
                SIRlistNorth[2].append(s.StudentObjects[StudentNumber])           
            elif s.StudentObjects[StudentNumber].Halls == 'East':
                SIRlistEast[2].append(s.StudentObjects[StudentNumber])
            elif s.StudentObjects[StudentNumber].Halls == 'West':
                SIRlistWest[2].append(s.StudentObjects[StudentNumber])
            elif s.StudentObjects[StudentNumber].Halls == 'South':
                SIRlistSouth[2].append(s.StudentObjects[StudentNumber])
            else:
                ValueError('Student must have an SIR value')

        else:
            raise ValueError('Student must have an SIR value')
            
    return  (SIRlistNorth), (SIRlistEast), (SIRlistSouth) , (SIRlistWest)
   
                           
SIRlistNorth, SIRlistEast, SIRlistSouth , SIRlistWest  = DailyDataSIR()

StudentInfoDataFrame = CreateDataFrame()

S = StudentInfoDataFrame['SIR']
print(S)
   
###### TESTING


# StudentInfoDataFrame = CreateDataFrame()
# SIRdata = CollectSIRdata

# # Pull certain people from the data frame
# StudentInfoDataFrame.iloc[1]

# # Sort the dataframe by social number in descending order 
# StudentInfoDataFrame.groupby('StudentNumber')['Social'].max().reset_index().sort_values(['Social'], ascending=False)



# print(StudentInfoDataFrame)
# print(CollectSIRdata())
