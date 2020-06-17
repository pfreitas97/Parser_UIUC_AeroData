#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: pedroaugustofreitasdearaujo
"""

import os

# Specify where files are saved

#location assumes separate folder for prop





def findCharOccurrences(string, char):
    return [i for i, letter in enumerate(string) if letter == char]


# Will return file name pitch and diameter 

def Propeller_File_Selector(path, contains="all"):
    
    EXCEPTIONS = []
        
    files = []
    filenames = []
    
    
    diameters = [] # in original units for now
    
    pitches = [] # in og units
    
    filePaths = []
        
    
    # r=root, d=directories, f = files
    
    for r, d, f in os.walk(path):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))
    
    cut = len(path) + 1
    
    # Lets remove the directory from the string and put
    # the filenames in a new list
    
    
    for i in range(len(files)):
        
        
       # This block prevents the inclusion of every file when required 
        if contains != "all":
            if files[i].find(contains) == -1:
                continue
        
            
            
        
        currentPath = files[i]
        currentFile = currentPath[cut:]
        filenames.append(currentFile)
        
       # print(currentFile +  "still temp2")
       
       
       
        
    # Lets extract the diamters, and pitches and name of the prop in each file
         
        
    for i in range(len(filenames)):
        
        currentFile = filenames[i] #propeller file
        
        
        # Unfortunately the dataset is not standardized and a small number of
        # propellers need to be treated separately
        
        
                
             
        # Within the propeller data set the names and dimensions are encoded
        # in the file name separated by "_" characters
        
        breaks = findCharOccurrences(currentFile, "_")
        
        
        # Within each filename the dimensions are in the following format:
        # _Propeller-Diameter[Inches]xPropeller-Pitch[Inches]_
        # Where the first and second "_" are ALWAYS the 
        #       first and second in the file
        
        # finding the x split within this section is then given by:
        
        x = findCharOccurrences(currentFile,"x")
        
        
        #print(currentFile)
        #print(breaks)
        
        # select only the x between the desired breaks
        
        x = [X for X in x if X > breaks[0] & X < breaks[1]]
                
        
        diameters.append(currentFile[breaks[0]+ 1: x[0]])
        
        
        pitches.append(currentFile[x[0] + 1: breaks[1] ])
        
        
        filePaths.append(os.path.join(path,currentFile))
        
        #filePaths.append(path + "/" + currentFile)
        
        
        #In case only a subset of files is desired.
        
        
        
        
        
            
    if len(diameters) == len(filenames):
        print("Array Dimension Check Success")
        #print(filenames)
        return [filenames,diameters,pitches,filePaths]
    else:
        print("something broke")
        return None

