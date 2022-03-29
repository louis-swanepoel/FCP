# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import integrate, linalg, optimize #integration and odes, linear␣ 􏰀→algebra, optimization/root-finding
from scipy.integrate import solve_ivp # import solve_ivp from scipy integrate from scipy.linalg import solve # solve function for later...
from scipy.integrate import solve_ivp
from scipy.optimize import root 

# code from lecture notes that i have edited slightly to suit our model to give a start to solving the differential equations 
# we need to create differential equations with rate of change of SIR preportions on LHS so we can enter the RHS of the equation below in solve_ivp

InitialInfectionRates = [0.9999, 0.0001, 0] # where vector is [S,I,R] respectively 

period = [0, 1000]   # time over which study is done 

infectionRatio = 0.019    #  percentage of encounters that are infected by a person of status I

Ip = 1/(14*24)      # constant for infection time where infection takes 14 days
Rp = 1/(30*24)      # constant for recovery time where recovery takes a month plus the infected time of 14 days
  

def SIRmodel(t, y):    


    # for t%24 in range(0,8):      # sleeping infections
    #     a = 0
    # for t%24 in range(8,10):   # flat infections
    #     a = 8
    # for t%24 in range(10,16):  # uni campus infections
    #     a = 30
    # for t%24 in range(16,24):  # nighttime infections  
    #     a = 12   
    # else:
    #     print("error, variable a not assigned ")   
           # Ludo check for modular changes over the weekend to make encounters a function of lifestyle     
    # above i tried to create varying variable a but this will be done later
    
    a = 2    
    b = a*infectionRatio
    
    return [Rp*y[2] - b*y[0]*y[1], b*y[0]*y[1] - Ip*y[1],Ip*y[1] - Rp*y[2]]     # returns differential equations 

sol = solve_ivp(SIRmodel, period, InitialInfectionRates, t_eval = np.linspace(0, 1000, num = 400))

plt.plot(sol.t, sol.y.T)

plt.legend(['susceptible', 'infected', 'recovered'], shadow=True) 

plt.xlabel('days')

plt.title('SIR model')

#function using scipy.optimize root module for returning roots of the function so we can see where minimum and maximum infection rates occur 
#def func(x):
 #   return x + np.exp(x) sol = root(func, 0) sol.x