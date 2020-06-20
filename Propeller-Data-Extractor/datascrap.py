#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: pedroaugustofreitasdearaujo
"""

import os

# Specify where files are saved

#location assumes separate folder for prop




'''NO CHILD LEFT BEHIND SUPER STARS
    Special case handling to address the lack of a std data format'''
    
def handleLackOfGeometricData(string):    
    
    print("FUCKKKKKKK %s" % string)
    

def metricDetection(string):
    
    print("at least I got triggered")
    

''' END OF NO CHILD LEFT BEHIND '''


    
def findCharOccurrences(string, char):
    return [i for i, letter in enumerate(string) if letter == char]




# Will return file name pitch and diameter 



'''TODOOOOOO HANDLE METRIC ERROR AND STOP EXCLUDING POORLY LABELED INPUT '''

def Propeller_File_Selector(path, contains="all"):
            
    files = []
    filenames = []
    
    
    diameters = [] # in original units for now
    
    pitches = [] # in og units
            
    
    # r=root, d=directories, f = files
    
    for r, d, f in os.walk(path):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))
    
    cut = len(path) + 1
    
    # Lets remove the directory/root from each string and put
    # the filenames in a new list    
       
        
    # Lets extract the diamters, and pitches and name of the prop in each file
         
        
    for file in files:
        
        
        
        currentFile = file[cut:]
        
        if contains != "all":
            if currentFile.find(contains) == -1:
                continue
        


        
        # Unfortunately the dataset is not standardized and a small number of
        # propellers need to be treated separately
        
        
                
             
        # Within the propeller data set the names and dimensions are encoded
        # in the file name separated by "_" characters
        
        breaks = findCharOccurrences(currentFile, "_")
        
        
        
        '''TODOOO SUBISTITUE MORE APPROPRIATELY'''
        # This is meant to account for the fact the second volume 
        # does not maintain a consistent naming convention
        
        if not breaks or len(breaks) == 1:
            handleLackOfGeometricData(currentFile)
            continue
        
        
        # Within each filename the dimensions are in the following format:
        # _Propeller-Diameter[Inches]xPropeller-Pitch[Inches]_
        # Where the first and second "_" are ALWAYS the 
        #       first and second in the file
        
        # finding the x split within this section is then given by:
        
        x = findCharOccurrences(currentFile,"x")
        
        
        
        '''TODOOO SUBISTITUE MORE APPROPRIATELY'''
        # This is meant to account for the fact the second volume 
        # does not maintain a consistent naming convention
        if not x:
            handleLackOfGeometricData(currentFile)
            continue


        
        
        # select only the x between the desired breaks
        
        
        ''' TODO refactor for user friendliness '''
        
        
        x = [X for X in x if X > breaks[0] & X < breaks[1]]
        
        
        
        ###
                
        
        filenames.append(currentFile)
        
        diameters.append(currentFile[breaks[0]+ 1: x[0]])
        
        
        pitches.append(currentFile[x[0] + 1: breaks[1] ])
        
        
        
        #filePaths.append(path + "/" + currentFile)
        
        
        #In case only a subset of files is desired.
        
        
        
    # THIS ENTIRE BLOCK NEEDS TO BE REFACTORED    
        
        ###############    
    if len(diameters) == len(filenames):
        print("Array Dimension Check Success")
        #print(filenames)
        return [filenames,diameters,pitches,files]
    else:
        print("something broke")
        return [filenames,diameters,pitches,files]



##############
