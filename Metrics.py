#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 13:03:36 2022

@author: louisswanepoel
"""
# import names as nm
from ast import Break
import pandas as pd 
import random as r
import Assignments as s


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
def CollectSIRdata(S,I,R):
    
    # Tally up frequency of each bin to find out how many people are S, I OR R
    todaysFrequencyS = len(SIRinfoFilter('S', None, None, None, None, True,True))
    todaysFrequencyI = len(SIRinfoFilter('I', None, None, None, None, True,True))
    todaysFrequencyR = len(SIRinfoFilter('R', None, None, None, None, True,True))
    
    # Find Proportion
    todaysProportionS = todaysFrequencyS/s.PopulationSize
    todaysProportionI = todaysFrequencyI/s.PopulationSize
    todaysProportionR = todaysFrequencyR/s.PopulationSize
    
    proportionsSIR = [todaysProportionS,todaysProportionI,todaysProportionR]
    
    S.append(proportionsSIR[0])
    I.append(proportionsSIR[1])
    R.append(proportionsSIR[2])     
      
   
# returns--  SIRlistNorth, SIRlistEast, SIRlistSouth , SIRlistWest where each is a nested list of SIR data 

   
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
    if Day == CollectDataDay and s.PlotOrNot[0]== 'TRUE':

        if s.Sir[0] == 'S':
            yAxisName = "Susceptible"
        elif s.Sir[0] == 'I':
            yAxisName = "Infected"
        else:
           yAxisName = "Recovered"
        
        North = len(SIRinfoFilter(s.Sir[0], None, None, 'North',None , Day, Day))
        East = len(SIRinfoFilter(s.Sir[0], None, None, 'East',None, Day, Day))
        South = len(SIRinfoFilter(s.Sir[0], None, None, 'South', None, Day, Day))
        West = len(SIRinfoFilter(s.Sir[0], None, None, 'West', None, Day, Day))        
       
        SIR = [North,South,East,West] 
        Halls = 'North', 'South', 'East', 'West'
        
        plt.bar(Halls,SIR, color=['red', 'green', 'blue', 'cyan'])
        plt.title('Halls infection data:'+ str(DateRange[Day]))
        plt.xlabel('Halls')
        plt.ylabel(yAxisName)
        plt.show()   
        
def BarChartCourse(Day, DateRange, CollectDataDay):
    
    if Day == CollectDataDay and s.PlotOrNot[1]== 'TRUE':
        
        Course = 'STEM', 'ARTS'

        if s.Sir[1] == 'S':
            yAxisName = "Susceptible"
        elif s.Sir[1] == 'I':
            yAxisName = "Infected"
        else:
           yAxisName = "Recovered"
        
        Stem = len(SIRinfoFilter(s.Sir[1], None, None, None, 'STEM', Day, Day))
        Arts = len(SIRinfoFilter(s.Sir[1], None, None, None, 'ARTS', Day, Day))
        
        SIR = [Stem, Arts]
        
        plt.bar(Course,SIR,color=['red', 'green'])
        plt.title('Course infection data:'+ str(DateRange[Day]))
        plt.xlabel('Course')
        plt.ylabel(yAxisName)
        plt.show()
        
def BarChartCountries(Day, DateRange,CollectDataDay):
    
    if Day == CollectDataDay and s.PlotOrNot[2]== 'TRUE':
        
        countries = 'China' , 'US' , 'UK' , 'EU'

        if s.Sir[2] == 'S':
            yAxisName = "Susceptible"
        elif s.Sir[2] == 'I':
            yAxisName = "Infected"
        else:
           yAxisName = "Recovered"
        
        china = len(SIRinfoFilter(s.Sir[2], 'China', None, None, None, Day,Day))
        us = len(SIRinfoFilter(s.Sir[2], 'US', None, None, None, Day,Day))
        uk = len(SIRinfoFilter(s.Sir[2], 'UK', None, None, None, Day,Day))
        eu = len(SIRinfoFilter(s.Sir[2], 'EU', None, None, None, Day,Day))
        
        SIR = [china,us,uk,eu]
    
        plt.bar(countries,SIR, color=['red', 'cyan'])
        plt.title('Nationality infection data:'+ str(DateRange[Day]))
        plt.xlabel('Nationality')
        plt.ylabel(yAxisName)
        plt.show()
        
        
def MainTimeSeriesPlot(SIRSeries):
    
    def SIRchoice(q):

        if q == 'S':
            SIRSeries['S'].plot()
            plt.title('Infection Data Time Series Plot')
            plt.ylabel('Proportion of population')

        elif q == 'I':
            SIRSeries['I'].plot()
            plt.title('Infection Data Time Series Plot')
            plt.ylabel('Proportion of population')

        elif q == 'R':
            SIRSeries['R'].plot()
            plt.title('Infection Data Time Series Plot')
            plt.ylabel('Proportion of population')

            
    # Plotting the time series for certain user commands
    SIRtimeseriesOptions = s.Sir[3].split(',')
    for SIR in SIRtimeseriesOptions:
        if SIR == ' ':
            Break
        SIRSeries[SIR].plot()
    plt.title('Infection Data Time Series Plot')
    plt.ylabel('Proportion of population') 
    plt.show()


def SaveMainDataframeOfAttributes():
    # Creates an excel file of all the attributes of each person at the end of the simulation 
    df = (CreateDataFrame())
    MainData = pd.ExcelWriter('MainSpreadsheet.xlsx')
    df.to_excel(MainData)
    MainData.save()
    
  

        
