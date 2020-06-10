#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: pedroaugustofreitasdearaujo
"""

import os

# Specify where files are saved

#location assumes separate folder for prop

def UIUC_Propeller_DWrangler(path):
    
    
    
    files = []
    filenames = []
    diameter = []
    diam = ""
    
    
    # r=root, d=directories, f = files
    
    for r, d, f in os.walk(path):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))
    
    cut = len(path) + 1
    
    # Lets remove the directory from the string and put
    # the filenames in a new list
    
    
    for i in range(len(files)):
        
        currentPath = files[i]
        currentFile = currentPath[cut:]
        filenames.append(currentFile)
        
        print(currentFile +  "still temp2")
        
    # Lets extract the diamters of the prop in each file
        
        
        
    for i in range(len(files)):
        currentFile = filenames[i] #propeller file
        #print(temp)
        brake = 0
        count = 0
        diam = ""
        
        
        # TODO CHANGE THIS TO SOMETHING MORE DIGNIFIED
        # Also add static file catch
        while brake == 0:  
            
            if (currentFile[count] != "_"):
                
                count = count + 1
            elif (currentFile[count] == "_"):
                count = count + 1
            
                while currentFile[count] != "x" and currentFile[count].isalpha() == 0:
                    diam = diam + currentFile[count]
                    count = count + 1
                
                if currentFile[count] == "x":
                    brake = 1
                    count = 0
            
        
        diameter.append(diam)
        
        
        
            
    if len(diameter) == len(filenames):
        print("Array Dimension Check Success")
        print(filenames)
        return [filenames,diameter]
    else:
        print("something broke")
        return None

