#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:16:10 2022

@author: dj21255
"""


def Infected(proximity, Immunity): #arguments proximity and Immunity relating to whether they have been in contact with someone infected, and whether they are susceptible or not
    if Immunity == True:
        InfectedStatus = 0   
    else:
        if proximity == True:
            InfectedStatus = 1
        if proximity == False: 
            InfectedStatus = 0
    return InfectedStatus             # returns 1 for infected and 0 for not infected
      
# print(Infected(True, False))

def Immunity(Infected, DateOfInfection, currentt):
    ImmunityStatus = 0
    if Infected == 1:
        if DateOfInfection + 14 < currentt: #current time
            return  1
        else:
            return  0    #returns 0 for immune 
   
        
#Infected(proximity, Immunity()):
    
print(Immunity(1,30,40))

# for i in list:
#     Infected(i.proximity, i.Immunity)
        