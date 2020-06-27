#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:01:19 2020

@author: pfreitas97
Airfoil_data_util: Filter 
"""

import os
import shutil



# ''.join([char for char in first_line if char not in SPECIAL_CHAR]).replace(" ","_") -- removes everything but spaces 
#     which it replaces with _
def _get_new_filename(absPath,filename):
    SPECIAL_CHAR = (",","/",".","\\","%"," ","AIRFOILS","AIRFOIL","__")
    
    newFilename = filename.replace(".dat","").upper()
        
    with open(absPath,"r", encoding="utf-8") as file:
        
        try:
            newFilename = file.readline().strip()
            
        except UnicodeDecodeError:
            idxDot = filename.find(".")
            
            newFilename = filename[:idxDot].upper()
            
            print("Warning the following airfoil file might be in a non-standard encoding: %s \n" % filename)
            
            
                    
        for char in SPECIAL_CHAR:
            
            newFilename = newFilename.replace(char,"_")
        
        return newFilename + ".dat"
    
    
    return newFilename + ".dat"


def rename_airfoils(path,dest_dir="RENAMED_FOLDER"):
    ''' Utility file to change the filenames of all airfoils from the original to the first line within each file. 
        E.g. n0012 -> NACA_0012
    Params:
    airfoil_path: Path to folder where all airfoil .dat files are stored
    new_directory: Option to create new folder with renamed airfoils, if it is blank function will override current names
    '''
    assert(os.path.exists(path))
    

    assigned_names = []
    
    targetPath = path
        
    if len(dest_dir) > 0:
        os.mkdir(dest_dir)
        targetPath = os.path.join(os.getcwd(),dest_dir)

    for r, d, f in os.walk(path):
        for file in f:
            if '.dat' in file:
                                
                currentAbsPath = os.path.join(r,file)
                
                newFilename = _get_new_filename(currentAbsPath,file)
                
                
                # Checking for duplicate names:
                if newFilename in assigned_names:
                    print("Note original name was kept for: %s to prevent a file from being overwritten \n" % file)
                    newFilename = file
                
                assigned_names.append(newFilename)
                
                
                if len(dest_dir) > 0: # If making a new directory, and copying all files there prior to renaming
                    
                    shutil.copy(currentAbsPath,targetPath)
                    
                    dest_dir = os.path.join(targetPath,file)
                    
                    new_Name_dest_dir = os.path.join(targetPath,newFilename)
                    
                    os.rename(dest_dir,new_Name_dest_dir)
                                        
                    
                else: # if overwriting old files
                    
                    new_Name_dest_dir = os.path.join(r,newFilename)
                    
                    os.rename(currentAbsPath,new_Name_dest_dir)




lists = rename_airfoils(os.path.join(os.getcwd(),"Airfoil_Coordinates"))
    
#rename_airfoils(os.path.join(os.getcwd(),"Airfoil_Coordinates"), dest_dir="NEWFOIL")