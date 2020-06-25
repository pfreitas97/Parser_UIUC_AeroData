#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:01:19 2020

@author: pfreitas97
Airfoil_data_util: Filter 
"""

import os


testPATH = os.path.join(os.path.join(os.getcwd(),"Airfoil_Coordinates"),"n0011sc.dat")

# ''.join([char for char in first_line if char not in SPECIAL_CHAR]).replace(" ","_") -- removes everything but spaces 
#     which it replaces with _



def _get_new_filename(absPath):
    SPECIAL_CHAR = (",","/",".","\\","%","&"," ")
    
    with open(absPath) as file:
        
        newFilename = file.readline().strip()
        
        for char in SPECIAL_CHAR:
            newFilename = newFilename.replace(char,"_")
        
        print(newFilename)
        return newFilename
    return


 
def rename_airfoils(path,new_directory=""):
    ''' Utility file to change the filenames of all airfoils from the original to the first line within each file. 
        E.g. n0012 -> NACA_0012
    Params:
    airfoil_path: Path to folder where all airfoil .dat files are stored
    new_directory: Option to create new folder with renamed airfoils, if it is blank function will override current names
    '''
    assert(os.path.exists(path))
    
    targetPath = path
        
    if len(new_directory) > 0:
        os.mkdir(new_directory)
        targetPath = os.path.join(os.getcwd(),new_directory)

    print(path)
    for r, d, f in os.walk(path):
        for file in f:
            if '.dat' in file:
                currentAbsPath = os.path.join(r,file)
                newFilename = _get_new_filename(currentAbsPath)
                os.rename(currentAbsPath,os.path.join(targetPath,newFilename))
                
    print(newFilename)
    
    
    
    
    
    


    
rename_airfoils(os.getcwd())