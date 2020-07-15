#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: pedroaugustofreitasdearaujo
"""

import os

import pandas as pd


'''Special case handling to address the lack of a std data format'''
    
def _handleLackOfGeometricData(filename,verbose): 
    '''Function that determines what the program should do with files that do not provide pitch information, 
    currently I am ignoring them but this could easily be changed by altering this function and the marked  
    if statement in prop_file_filter
    
    Parameters:
        filename - name of the file that does not follow the standard format
        
        verbose - Boolean print the propellers that were ignored if set to true.
    '''
    
    if verbose:
        print("The propeller named: %s was not included in list due to non-compliant format." % filename)
    
    
    
def _find_Metric_Props():
    '''Return list of metric propellers, this was hardcoded since there were only 5 of them across 4 brands'''
    
    METRIC_PROPELLERS = ("ef","kpf","pl","vp")
    
    
    return METRIC_PROPELLERS

    
def _findCharOccurrences(string, char):
    '''Return iterable of every occurence of char character '''
    return [i for i, letter in enumerate(string) if letter == char]


def _scrapeUniqueName(filename):
    ''' Return a version of the filename which will match across different types of files, e.g. the static and geometric
    files referring to the same dataframe will have the same filename if this function is applied. Useful for merging columns
    
    filename: name of file as seen in folder. e.g. "apcff_9x4_geom.txt"
    '''
    
    breaks = _findCharOccurrences(filename, "_")
    
    
    
    return filename[:breaks[1]]



def prop_File_Filter(path, contains="all", metric=False, verbose=False): 
    '''This function accesses a path with the desired propeller data and returns
    only the elements requested along with the information embedded in the filename.
    
    Parameters:
        path - Absolute path to desired Propeller data folder
        contains - An optional substring to filter content, useful for:  
                    extracting the geometric files for every Propeller, for example.
        metric - Boolean return diameter and pitch in meters when set to true, 
                    otherwise it will return those values in inches
        verbose - Boolean print the propellers that were ignored if set to true.
        '''
    
    assert(os.path.exists(path))
        
    files = []
    Prop_Name = []

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
    # the Prop_Name in a new list    
       
        
    # Lets extract the diamters, and pitches and name of the prop in each file
         
        
    for file in files:
        
        currentFile = file[cut:]
        
        if contains != "all":
            if currentFile.find(contains) == -1:
                continue
        
        # Within the propeller data set the names and dimensions are encoded
        # in the file name separated by "_" characters
        
        breaks = _findCharOccurrences(currentFile, "_")
        
       
        ''' Change here to include discarded propeller files'''
        
        # Within each filename the dimensions are in the following format:
        # _Propeller-Diameter[Inches]xPropeller-Pitch[Inches]_
        # Where the first and second "_" are ALWAYS the 
        #       first and second in the file
        
        
        
        # finding the x split within this section is then given by:
        
        position_x = _findCharOccurrences(currentFile,"x")
        

        if len(breaks) < 2 or len(position_x) < 2:
            _handleLackOfGeometricData(currentFile, verbose)
            continue
        
                
        # Unfortunately the dataset naming convention is not standardized 
        # and thus a small number of propellers need to be treated separately
        # This particular block is meant to handle this issue.
        
        
        
        
        ''' end of block '''

        # End of execption handling block
        
        
        
        # select only the 'x' between the desired breaks
        
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
        
        if metric:
            if any(prop in currentFile for prop in METRIC_PROPELLERS):
                diameterValue = diameterValue / 1000
                pitchValue = pitchValue / 1000
            
            else:
                diameterValue = round(diameterValue * METERS_PER_INCH,3)
                pitchValue = round(pitchValue * METERS_PER_INCH,3)                
        
        

        # For convinience, returning only unique name
        
        currentFile = _scrapeUniqueName(currentFile)
        
        Prop_Name.append(currentFile) 
        
        diameters.append(diameterValue)
        
        pitches.append(pitchValue)
        
        filePaths.append(file)

        
    if len(diameters) == len(Prop_Name):
        
        return [Prop_Name,diameters,pitches,filePaths]
    else:
        print("Error: data dimensions are incorrect, result might be incorrect. Please check the path provided \
              to deetermine if it contains files from outside the UIUC database")
        return [Prop_Name,diameters,pitches,filePaths]



def mergePropellerFiles(path,target_1,target_2,metric=False,dropDuplicates=True,sort=True):
    '''Return single pandas dataframe where each file path column contains the path to the file with "target" substring.
    Merges files based on Propeller name, drops duplicate names.
    
    Parameters
    path: Absolute path to folder with propeller text files
    target_1: First substring for filetype (e.g. static, geom)
    target_2: Second substring for filetype (e.g. static, geom)
    metric: Boolean return set to true if data in metric is preferred
    dropDuplicates: Set to false if files that share the same filename are to be kept.
    sort: Set to true to return the dataframe in alphabetical order
    '''
    
    assert(isinstance(target_1, str))
    assert(isinstance(target_2, str))
    
    assert(target_1 != target_2)
    
    
    tlist1 = prop_File_Filter(path,contains=target_1,metric=metric)
    
    tlist2 = prop_File_Filter(path,contains=target_2,metric=metric)
    
    
    
    df1 = pd.DataFrame({'Prop_Name' : tlist1[0],'diameter' : tlist1[1], 
                      'pitch' : tlist1[2], target_1 + '_path' : tlist1[3]})
    
    
    df2 = pd.DataFrame({'Prop_Name' : tlist2[0],'diameter' : tlist2[1], 
                      'pitch' : tlist2[2], target_2 + '_path' : tlist2[3]})
    
    
    if dropDuplicates:
        df1.drop_duplicates(subset=['Prop_Name'],inplace=True)
        df2.drop_duplicates(subset=['Prop_Name'],inplace=True)
        pass
    
        
    mergedf = pd.merge(df1,df2,on='Prop_Name',how='inner')
        
    mergedf.drop(['diameter_y','pitch_y'],axis=1,inplace=True)
    
    mergedf.columns = ['Prop_Name','diameter','ptich',target_1 + '_path',target_2 + '_path']
    if sort:
        mergedf.sort_values(by='Prop_Name',ignore_index=True,inplace=True)
        pass
    
    return mergedf










