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
    
    print("%s" % string)
    

def metricDetection(string):
    
    print("at least I got triggered")
    

''' END OF NO CHILD LEFT BEHIND '''


    
def findCharOccurrences(string, char):
    return [i for i, letter in enumerate(string) if letter == char]




# Will return file name pitch and diameter 



'''TODOOOOOO HANDLE METRIC ERROR, AND STOP EXCLUDING POORLY LABELED INPUT '''

'''Missing: Flag saying whether results in metric or imperial are desired
            Way to handle the fact metric data points were included unconverted '''

def Prop_File_Filter(path, contains="all"):
    '''This function accesses a path with the desired propeller data and returns
    only the elements requested with the information embedded in the filename.
    
    KeyWork Arguments:
        Path - Absolute path to desired Propeller data folder
        Contains - An optional substring to filter content, useful for:  
            extracting the geometric files for every Propeller, for example.
        ''' 
            
    files = []
    filenames = []
    
    
    diameters = [] # in original units for now
    
    pitches = [] # in og units
    
    
    ''' NOTEEEEE CURRENTLY ADDING PATHS OF MARGINALIZED FILES TOO ''' 
            
    
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
        
        breaks = findCharOccurrences(currentFile, "_")
        
        
        
        '''TODOOO SUBISTITUE MORE APPROPRIATELY'''
        
        # Unfortunately the dataset naming convention is not standardized 
        # and thus a small number of propellers need to be treated separately
        
        # This particular block is meant to handle this issue.
        
        if not breaks or len(breaks) == 1:
            handleLackOfGeometricData(currentFile)
            continue
        
        
        # Within each filename the dimensions are in the following format:
        # _Propeller-Diameter[Inches]xPropeller-Pitch[Inches]_
        # Where the first and second "_" are ALWAYS the 
        #       first and second in the file
        
        # finding the x split within this section is then given by:
        
        position_x = findCharOccurrences(currentFile,"x")
        
        
        if not position_x:
            handleLackOfGeometricData(currentFile)
            continue


        # End of execption handling block


        # select only the x between the desired breaks
        
        x = [X for X in position_x if X > breaks[0] & X < breaks[1]]
        
        
        ''' TODOOO ADD METRIC HANDLING HERE '''     

                        
        
        filenames.append(currentFile)
        
        diameters.append(currentFile[breaks[0]+ 1: x[0]])
        
        
        pitches.append(currentFile[x[0] + 1: breaks[1] ])
        
        
    # THIS ENTIRE BLOCK NEEDS TO BE REFACTORED    
        
        ###############    
    if len(diameters) == len(filenames):
        print("Array Dimension Check Success")
        #print(filenames)
        return [filenames,diameters,pitches,files]
    else:
        print("Error: data dimensions are incorrect")
        return [filenames,diameters,pitches,files]


def find_Metric_Props(html_file):
    '''Utilizes the HTML file included with the database to determine which files must be converted from metric
        
    Returns a list with the name of every metric propelller'''
    



##############
