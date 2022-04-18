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
    
    proportionsSIR = [todaysProportionS,todaysProportionI,todaysProportionR]
    
    return proportionsSIR
      
   
# returns--  SIRlistNorth, SIRlistEast, SIRlistSouth , SIRlistWest where each is a nested list of SIR data 
def DailyDataSIR(Day,CollectDataDay):
    
    if Day == CollectDataDay:
    
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
   
def SIRinfoFilter(SIRstatus, Origin, Name, Halls, Course, Day,CollectDataDay):
    
    if Day == CollectDataDay:
        
        # Reuses CreateDataframe function to produce a data frame of all students data
        StudentInfoDataFrame = CreateDataFrame()
        
        #   Checks to see if each respective attribute to be filtered by was defined when inputting the function 
        if isinstance(SIRstatus,str) == True:    
            
            # If it was defined then it adds the filtering condition tot the dataframe
            StudentInfoDataFrameFiltered = StudentInfoDataFrame[(StudentInfoDataFrame['SIR'] == SIRstatus)]   
        else:
            
            # If no infomation was given to filter then it does not filter it by the variable and says so to the user       
            StudentInfoDataFrameFiltered = StudentInfoDataFrame[~(StudentInfoDataFrame['SIR'] == SIRstatus)] 
            
        
        # These steps are repeated for each attribute that could be filtered by  
        if isinstance(Origin,str) == True:       
            StudentInfoDataFrameFiltered = StudentInfoDataFrameFiltered[(StudentInfoDataFrameFiltered['Origin'] == Origin) ]
        else:        
            StudentInfoDataFrameFiltered = StudentInfoDataFrameFiltered[~(StudentInfoDataFrameFiltered['Origin'] == Origin) ]
            
        
        if isinstance(Name,str) == True:       
            StudentInfoDataFrameFiltered = StudentInfoDataFrameFiltered[(StudentInfoDataFrameFiltered['Name'] == Name) ]
        else:         
            StudentInfoDataFrameFiltered = StudentInfoDataFrameFiltered[~(StudentInfoDataFrameFiltered['Name'] == Name) ]
            
        
        if isinstance(Halls,str) == True:
            StudentInfoDataFrameFiltered = StudentInfoDataFrameFiltered[(StudentInfoDataFrameFiltered['Halls'] == Halls) ]
        else:         
            StudentInfoDataFrameFiltered = StudentInfoDataFrameFiltered[~(StudentInfoDataFrameFiltered['Halls'] == Halls) ]
                 
            
        if isinstance(Course,str) == True:
            StudentInfoDataFrameFiltered = StudentInfoDataFrameFiltered[(StudentInfoDataFrameFiltered['Course'] == Course) ]
        else:        
            StudentInfoDataFrameFiltered = StudentInfoDataFrameFiltered[~(StudentInfoDataFrameFiltered['Course'] == Course) ]
             
        
        # The filtered dataframe is returned
        return  StudentInfoDataFrameFiltered    
                         

#### Graphing

import matplotlib.pyplot as plt


# fig = px.line(SIRSeries, x='Date', y= SIRSeries.columns)

# fig.show(renderer="svg")

def plotlinegraph(SIRSeries):
    # Using a inbuilt style to change
    # the look and feel of the plot
    plt.style.use("fivethirtyeight")
     
    # setting figure size to 12, 10
    plt.figure(figsize=(12, 10))
     
    # Labelling the axes and setting
    # a title
    plt.xlabel("Date")
    plt.ylabel("Values")
    plt.title("SIR")
     
    # plotting the "A" column and "A" column
    # of Rolling Dataframe (window_size  = 20)
    SIRSeries.plot('Date', 'S')
    SIRSeries.plot('Date', 'I')
    SIRSeries.plot('Date', 'R')
    SIRSeries.show()

# Bar chart for halls SIR data
def BarChartHalls(Day, DateRange,CollectDataDay):
    if Day == CollectDataDay:
        
        (SIRlistNorth), (SIRlistEast), (SIRlistSouth) , (SIRlistWest) = DailyDataSIR(Day,Day)
        
        SIRinputChoice = input('input 0,1,2 for SIR y axis in Halls plot:')
        if SIRinputChoice == '0':
            yAxisName = "Susceptible"
        elif SIRinputChoice == '1':
            yAxisName = "Infected"
        else:
           yAxisName = "Recovered"
           
        SIR = [len(SIRlistNorth[int(SIRinputChoice)]), len(SIRlistEast[int(SIRinputChoice)]), len(SIRlistSouth[int(SIRinputChoice)]) , len(SIRlistWest[int(SIRinputChoice)])] 
        Halls = "North","South","East","West"
    
        plt.bar(Halls,SIR)
        plt.title('Halls infection data:'+ str(DateRange[Day]))
        plt.xlabel('Halls')
        plt.ylabel(yAxisName)
        plt.show()   
        
def BarChartCountries(Day, DateRange,CollectDataDay):
    
    if Day == CollectDataDay:
        
        countries = 'China' , 'US' , 'UK' , 'EU'

        SIRinputChoice = input('input S,I,R for SIR vals in y axis for countries plot:')
        if SIRinputChoice == 'S':
            yAxisName = "Susceptible"
        elif SIRinputChoice == 'I':
            yAxisName = "Infected"
        else:
           yAxisName = "Recovered"
        
        china = len(SIRinfoFilter(SIRinputChoice, 'China', None, None, None, Day,Day))
        us = len(SIRinfoFilter(SIRinputChoice, 'US', None, None, None, Day,Day))
        uk = len(SIRinfoFilter(SIRinputChoice, 'UK', None, None, None, Day,Day))
        eu = len(SIRinfoFilter(SIRinputChoice, 'EU', None, None, None, Day,Day))
        
        SIR = [china,us,uk,eu]
    
        plt.bar(countries,SIR)
        plt.title('Nationality infection data:'+ str(DateRange[Day]))
        plt.xlabel('Nationality')
        plt.ylabel(yAxisName)
        plt.show()   
def MainTimeSeriesPlot(SIRSeries):
    
    # Plotting the time series for certain user commands
    SIRtimeseries = input('what would you like to see 1 var 2 var or 3 var against one another: ')

    if SIRtimeseries == '1':
        q = input('which one would you like to see (S,I,R): ')
        if q == 'S':
            SIRSeries['S'].plot()
            plt.show()
        elif q == 'I':
            SIRSeries['I'].plot()
            plt.show()
        elif q == 'R':
            SIRSeries['R'].plot()
            plt.show()
    elif SIRtimeseries == '2':
        q = input('which one would you like to see (S,I,R): ')
        if q == 'S':
            SIRSeries['S'].plot()
            q = input('which other one would you like to see (S,I,R): ')
            if q == 'S':
                SIRSeries['S'].plot()
                plt.show()
            elif q == 'I':
                SIRSeries['I'].plot()
                plt.show()
            elif q == 'R':
                SIRSeries['R'].plot()
                plt.show()
        elif q == 'I':
            SIRSeries['I'].plot()
            q = input('which other one would you like to see (S,I,R): ')
            if q == 'S':
                SIRSeries['S'].plot()
                plt.show()
            elif q == 'I':
                SIRSeries['I'].plot()
                plt.show()
            elif q == 'R':
                SIRSeries['R'].plot()
                plt.show()
        elif q == 'R':
            SIRSeries['R'].plot()
            q = input('which other one would you like to see (S,I,R): ')
            if q == 'S':
                SIRSeries['S'].plot()
                plt.show()
            elif q == 'I':
                SIRSeries['I'].plot()
                plt.show()
            elif q == 'R':
                SIRSeries['R'].plot()
                plt.show()
    else:
        SIRSeries.plot()        
    ###### TESTING


# StudentInfoDataFrame = CreateDataFrame()
# SIRdata = CollectSIRdata

# # Pull certain people from the data frame
# StudentInfoDataFrame.iloc[1]

# # Sort the dataframe by social number in descending order 
# StudentInfoDataFrame.groupby('StudentNumber')['Social'].max().reset_index().sort_values(['Social'], ascending=False)



# print(StudentInfoDataFrame)
# print(CollectSIRdata())