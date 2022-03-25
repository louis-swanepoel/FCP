#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 13:03:36 2022

@author: louisswanepoel
"""
# import names as nm

class Person:
    
        
    #     # self.Infected = Infected
    #     # self.InfectionDate= InfectionDate
    #     self.Halls = Halls
    #     # self.recovered = reco
        
    def halls(self):
        if  NumeratedPerson in range(0,2):
             self.halls = "east"
        elif NumeratedPerson in range(2,3):
            self.halls = "west"
        elif NumeratedPerson in range(3,7):
            self.halls = "north"
        elif NumeratedPerson in range(7,10):
            self.halls = "south" 
        else:
            return print('error assigning hall')
    def origin(self, origin):
        if NumeratedPerson in range(0,2):
             self.origin = "china"
        elif NumeratedPerson in range(2,3):
            self.origin = "usa"
        elif NumeratedPerson in range(3,7):
            self.origin = "england"
        elif NumeratedPerson in range(7,10):
            self.origin = "mexico" 
        else:
            return print('error assigning origin')



for NumeratedPerson in (range(1,10)):
    
    NumeratedPerson = Person()
    NumeratedPerson.halls = Person.halls(NumeratedPerson)
    print(NumeratedPerson.halls)
    # with open('names.txt', 'r') as NamesFile:  # Ludo to add names attribute to agents 
       
        # NumeratedPerson.name = NamesFile.readlines(int(NumeratedPerson)
                                                   
           
    
     
    
    

    
    
# print(1.halls)