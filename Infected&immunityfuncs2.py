# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 13:46:01 2022

@author: Ted Mellow
"""

from re import S
import pandas as pd
from datetime import date as d 
import assignments.py as s
#import argparse as ap
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

print(CreateDataFrame())

Today = d.today()
DateArray = pd.date_range('17/09/2021', Today.strftime("%d/%m/%Y"))
# Produces an array of the date from september until now 

DateCSV = pd.DataFrame(DateArray)
print(DateCSV)
def infected(StudentNumber):
    if StudentInfoDataFrame.iat[StudentNumber,SIR] == 'S': #checks from dataframe csv
        if proportionsSIR[1]*StudentInfoDataFrame[StudentNumber,Social] > 0.005: #proportion infected *
            student.SIR == 'I'
    if StudentInfoDataFrame.iat[StudentNumber,SIR] == 'I':
        recovered(StudentNumber, d.today())
    # return d.today() as DateOfInfection
    
def recovered(Infected, DateOfInfection):
    if Infected == 1:
        if DateOfInfection + 14 < d.today(): #current time
            student.SIR == 'I'    
        else:
            student.SIR =='R' #returns R for recovered
    else:
        student.SIR =='S'
    
for student in s.studentobjects():
    if student.SIR == 'S':
        student.SIR = infected(student) 
    elif student.SIR =='I':
        student.SIR = recovered(student)
    else:
        student.SIR = recovered(student)
    

