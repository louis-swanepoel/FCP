#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 13:03:36 2022

@author: louisswanepoel
"""
# import names as nm
with open('names.txt' , 'r') as names:
        Names = (names.read().replace('\n' , ' ')).split(' ') # creates a list of names from a text file

def halls(StudentNumber):
    if  StudentNumber in range(0,2):
        return 'east'    
    elif StudentNumber in range(2,3):
        return 'west'
    elif StudentNumber in range(3,7):
        return 'north'
    elif StudentNumber in range(7,10):
        return 'north'
    else:
        raise ValueError('Halls assignment error')   

def origin(StudentNumber):   ## THIS SHOULD BE CHANGED TO ENSURE HALLS AND ORIGIN ARE INDEPENDENT
    if NumeratedPerson in range(0,2):
        self.origin = "china" # should also use return
    elif NumeratedPerson in range(2,3):
        self.origin = "usa"
    elif NumeratedPerson in range(3,7):
        self.origin = "england"
    elif NumeratedPerson in range(7,10):
        self.origin = "mexico" 
    else:
        return print('error assigning origin')

class Person:
    def __init__(self, StudentNumber ):
        self.StudentNumber = int(StudentNumber)
        self.Halls = halls(StudentNumber)
        self.Origin = origin(StudentNumber)
        self.Name = Names[StudentNumber]

for Individual in range(1, PopulationSize): # population size should be an interger
    StudentName = Names[Individual]
    StudentName = Person(Individual)
    BigList.append(StudentName) ###unsure of specifics but this is kind of the right idea?

    #IF this works it should choose a name , 
    # use that as a variable name and then create a class object with that name
    # then append this object to the population list

StudentsList = [Person (i) for i in range(PopulationSize)]

    #this seems way more promissing



#class Person:
    
        
    #     # self.Infected = Infected
    #     # self.InfectionDate= InfectionDate
    #     self.Halls = Halls
    #     # self.recovered = reco
        
    # def halls(self):
    #     if  NumeratedPerson in range(0,2):
    #          self.halls = "east"
    #     elif NumeratedPerson in range(2,3):
    #         self.halls = "west"
    #     elif NumeratedPerson in range(3,7):
    #         self.halls = "north"
    #     elif NumeratedPerson in range(7,10):
    #         self.halls = "south" 
    #     else:
    #         return print('error assigning hall')
    # def origin(self, origin):
    #     if NumeratedPerson in range(0,2):
    #          self.origin = "china"
    #     elif NumeratedPerson in range(2,3):
    #         self.origin = "usa"
    #     elif NumeratedPerson in range(3,7):
    #         self.origin = "england"
    #     elif NumeratedPerson in range(7,10):
    #         self.origin = "mexico" 
    #     else:
    #         return print('error assigning origin')



