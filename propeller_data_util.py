#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: pedroaugustofreitasdearaujo
"""

import os

# Specify where files are saved

#location assumes separate folder for prop




'''Special case handling to address the lack of a std data format'''
    
def _handleLackOfGeometricData(string):    
    
    print("The propeller named: %s was not included in list due to non-compliant format." % string)
    

def _find_Metric_Props():
    '''Returns the list of metric propellers, this was hardcoded since there were only 5 of them across 4 brands'''
    
    METRIC_PROPELLERS = ("ef","kpf","pl","vp")
    
    
    return METRIC_PROPELLERS

    
def _findCharOccurrences(string, char):
    return [i for i, letter in enumerate(string) if letter == char]





'''Missing: Handling of additional unorthodox propeller names'''


''' Also change for more silent result '''

def Prop_File_Filter(path, contains="all", metric=False):
    
    '''This function accesses a path with the desired propeller data and returns
    only the elements requested with the information embedded in the filename.
    
    KeyWork Arguments:
        path - Absolute path to desired Propeller data folder
        contains - An optional substring to filter content, useful for:  
                    extracting the geometric files for every Propeller, for example.
        metric - Boolean return diameter and pitch in meters when set to true, 
                    otherwise it will return those values in inches
        '''
    
    assert(os.path.exists(path))
        
    files = []
    filenames = []

    diameters = []
    
    pitches = [] 
    
    filePaths = []
        
    METRIC_PROPELLERS = _find_Metric_Props()
    
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
        
        # Within the propeller data set the names and dimensions are encoded
        # in the file name separated by "_" characters
        
        breaks = _findCharOccurrences(currentFile, "_")
        
        
        
                
        # Unfortunately the dataset naming convention is not standardized 
        # and thus a small number of propellers need to be treated separately
        # This particular block is meant to handle this issue.
        
        if not breaks or len(breaks) == 1:
            _handleLackOfGeometricData(currentFile)
            continue
        
        # Within each filename the dimensions are in the following format:
        # _Propeller-Diameter[Inches]xPropeller-Pitch[Inches]_
        # Where the first and second "_" are ALWAYS the 
        #       first and second in the file
        
        # finding the x split within this section is then given by:
        
        position_x = _findCharOccurrences(currentFile,"x")
        
        
        if not position_x or len(position_x) == 1:
            _handleLackOfGeometricData(currentFile)
            continue


        # End of execption handling block
        
        
        
        
        
        # select only the x between the desired breaks
        
        x = [X for X in position_x if X > breaks[0] & X < breaks[1]]
        
        
        diameterValue = float(currentFile[breaks[0]+ 1: x[0]])
              
        pitchValue = float(currentFile[x[0] + 1: breaks[1]])
        
        
        # Converting to the appropriate units
        
        
        INCHES_PER_MILIMETER = 0.0393701
        
        METERS_PER_INCH = 0.0254
        
        if not metric:
            if any(prop in currentFile for prop in METRIC_PROPELLERS):
                diameterValue = round(diameterValue * INCHES_PER_MILIMETER,3)
                pitchValue = round(pitchValue * INCHES_PER_MILIMETER,3)
                print(diameterValue)
        
        
        if metric:
            if any(prop in currentFile for prop in METRIC_PROPELLERS):
                diameterValue = diameterValue / 1000
                pitchValue = pitchValue / 1000
            
            else:
                diameterValue = round(diameterValue * METERS_PER_INCH,3)
                pitchValue = round(pitchValue * METERS_PER_INCH,3)                
                          
         
        filenames.append(currentFile) 
        
        diameters.append(diameterValue)
        
        pitches.append(pitchValue)
        
        filePaths.append(file)

    # THIS ENTIRE BLOCK NEEDS TO BE REFACTORED    
        
        ###############    
    if len(diameters) == len(filenames):
        print("Array Dimension Check Success")
        #print(filenames)
        return [filenames,diameters,pitches,filePaths]
    else:
        print("Error: data dimensions are incorrect")
        return [filenames,diameters,pitches,filePaths]
##############
