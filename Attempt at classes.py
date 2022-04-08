# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 14:38:28 2022

@author: Ted Mellow
"""

import csv
import pandas as pd

# with open(r'\Users\Ted Mellow\Documents\GitHub\FCP\names.csv') as f:

#     csvreader =csv.reader(f)
#     header = []
#     header = next(csvreader)
#     print(header)
#     rows = []
#     for row in csvreader:
#         rows.append(row)
#     print(rows)

# def AllocateAttributesHalls(position):
#     with open(r'\Users\Ted Mellow\Documents\GitHub\FCP\names.csv') as f:

#         csvreader =csv.reader(f)
#         header = []
#         header = next(csvreader)
#         print(header)
#         rows = []
#     for row in csvreader:
#         rows.append(row)
#     print(rows)
    
#     for i in f:
#         if i in range(0,200):
#             Halls = 'east'
#         if i in range(201, 500):
#             Halls = 'west'
#     return Halls
def AllocateAttributesHalls(position):
        with open(r'\Users\Ted Mellow\Documents\GitHub\FCP\names.csv') as f:
            csvreader =csv.reader(f)
            header = []
            header = next(csvreader)
            print(header)
            rows = []
            for row in csvreader:
                rows.append(row)
            print(rows)
           
            
        for i in f:
            if i in range(0:200):
                Halls = 'east'
            if i in range(201, 500):
                Halls = 'west'
        f.write(Halls)
               

class Person:
    def __init__(self, Halls):
        self.Halls = AllocateAttributesHalls()
        
        
        with open(r'\Users\Ted Mellow\Documents\GitHub\FCP\names.csv') as f:
            csvwriter = csv.writer(f)
            for column in csvwriter:
                column.append(AllocateAttributesHalls())
    
