# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:37:06 2022

@author: farka
"""

import random
origin = ['China' , 'US' , 'UK' , 'EU']
weight = [.1 , .4 , .3 , .2]
randlist = random.choices(origin , weight , k =20)

InfDict = {'China':0.1 , 'UK':0.2 , 'US':0.15 , 'EU':.05}

Status = ['I' , 'S' ,'R' ]



def InitInfected(Nation):
    TempList = []
    for Individual in PopulationList:
        if Individual.origin == Nation;:
            TempList.append(Individual)
    affected = InfDict[Nation]
    InfWeight = [affected , 1-affected , 0]
    InfList = random.choices(Status , InfWeight , k = len(TempList))
    return InfList
    