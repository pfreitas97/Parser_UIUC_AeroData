#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 16:54:19 2020

@author: pedroaugustofreitasdearaujo
"""



import pandas as pd

import numpy as np

from propeller_data_util import Prop_File_Filter

import os



## Assumed known values that become parameters in this analysis

Velocity = 10;  #m/s

CD_aircraft = 0.057

S_ref = 0.6 # reference area AIRCRAFT

Rho = 1.225 #Atmo densityge

inch__Meter = 0.0254;


computeDrag = lambda rho,V,S_ref,CD : 0.5 * rho * (V**2) * S_ref * CD

computeThurst = lambda rho, CT, n, D : CT * rho * (n**2) * (D**4)

computeQuadratic_Sol = lambda a,b,c : np.array([  (-1*b + np.sqrt((b**2) - 4*a*c ))/(2*a), (-1*b - np.sqrt((b**2) - 4*a*c ))/(2*a)])


lists = Prop_File_Filter(os.getcwd()  + "/Propeller_Data_V2",contains="geom",metric=True)

    


filenames = lists[0]

Diams = lists[1]

Pitches = lists[2]

paths = lists[3]

#TESTER = paths


text = paths[0]

geomTest = pd.read_csv(paths[0],delim_whitespace=True)

#plt.plot(geomTest['r/R'],geomTest['c/R'] )



# for i in range(0,len(temp[0])):
    
#     prop = pd.read_csv('apccf_7.4x8.25_2884cm_4019.txt',delim_whitespace=True)





#prop = pd.read_table('apccf_7.4x8.25_2884cm_4019.txt',delim_whitespace=True)

#prop.colums = ["J", "CT", "CP", "eta"]


## Inside the prop pipeline:


#prop = pd.read_csv("/Users/pedroaugustofreitasdearaujo/PycharmProjects/aae451/MEINER_451/" + filenames[0] ,delim_whitespace=True)


# D = 7.4 * inch__Meter # diam in meters




# J_from_n = lambda n : Velocity / (n * D)


# poly_coeff = np.polyfit(prop['J'],prop['CT'],2)

# a0 = poly_coeff[0]

# a1 = poly_coeff[1]

# a2 = poly_coeff[2]

# J = V/(n D) V : freestream u,  n : rev / s, D : diam prop

# T = CT * rho * n ^ 2 * D ^ 4 

# D = 0.5 * rho * V^2 * S_ref * CD

# for poly fit order 2 we assume: a0* (J^2) + a1 * J + a2 =~ CT

# Substituting Assumption into T = D drag and solving for n:

# (a2 * V^2 * D^2)*n^2 + (a1 * V * D^3)*n + ( (a0* V^2 * D^2) - (0.5 * V^2 * S_ref* CD)) = 0

# current propeller is valid solution if: n > 0 & \in Reals (Im = 0)


# A = a2 * (D ** 4)

# B = a1 * (Velocity) * (D ** 3)

# C = (a0 * (Velocity ** 2) * (D ** 2) )  - 0.5 * (Velocity**2) * S_ref * CD_aircraft


# if  (B ** 2) < (4*A*C):
    
#     #break Solution will NOT exist
    
#     #TODO WHEN ACTUAL LOOP
    
#     print("fail")
    
# else:
#     n_candidates = computeQuadratic_Sol(A,B,C) # computes the two roots for n if a real solution exists
#     print(n_candidates)
    
    
    

    
# if n_candidates[0] <= 0 and n_candidates[1] <= 0:
#     # also break, solutions make no physical sense, should be impossible to happen but oh well
    
#     print('fail pt2')
# elif n_candidates[0] < 0 and n_candidates[1] > 0:
    
#     #only second solutiin valid, return that one
    
#     n_star = n_candidates[1]
    
    
# elif n_candidates[0] > 0 and n_candidates[1] < 0:
    
    
    
#     #only first solutiin valid, return that one
    
#     n_star = n_candidates[0]

# else:
#     # Two valid solutions, must now interpolate CP and check which one is smaller
    
#     # will utilize an order FOUR polyfit on account of the two points of inflection observed in the actual data
    
#     CP_poly_coeff = np.polyfit(prop['J'],prop['CP'],4)

#     CP_poly = np.poly1d(CP_poly_coeff)
    
#     #    n_star = n_candidates[0] if CP_poly(n_candidates[0]) * (n_candidates[0]**3) <  see notes

    
    
#     n_star = n_candidates[0] if CP_poly(J_from_n(n_candidates[0])) < CP_poly(J_from_n(n_candidates[1])) else n_candidates[1]





## Actual final answer you'd get for this airfoil after running program would then need to select minimum from list of valid powers

# CP_poly_coeff = np.polyfit(prop['J'],prop['CP'],4)

# CP_poly = np.poly1d(CP_poly_coeff)

# Power_star = Rho * (D **5) * (n_star ** 3) * CP_poly(J_from_n(n_star)) #Power in Watts




# # CTpoly = np.poly1d(poly_coeff)

# # print(CTpoly(0))

# # print(CTpoly(1))

# print(CTpoly.coeffs)



# plt.plot(CTpoly(np.linspace(0,1.5,100)))



#print(np.polyfit(prop['J'],prop['CT'],2)) second order fit
