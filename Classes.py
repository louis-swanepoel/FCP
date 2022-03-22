#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 13:48:35 2022

@author: dj21255
"""


RecoveryPeriod = 44 #This is the period of time it takes for someone to be recovered and susceptible to covid again.

HallWeight: {StokeBishop: 0.4, WestVillage:0.3, EastVillage: 0.2, SouthVillage:0.1}
class person;:
    def __init__(self, Name, Origin, Infected, InfectionDay, Halls, Recovered):
        self.Name = Name
        self.Origin = Origin
        self.Infected = Infected
        self.InfectionDate= InfectionDate
        self.Halls = Halls
        self.Recovered = Recovered
        
    def Recovered:
        if t < RecoveryPeriod + InfectionDay:
            Recovered = 1
        if t > RecoveryPeriod + InfectionDay:
            Recovered = 0
    def Halls:
        
        
person(Ted, )
    