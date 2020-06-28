#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 20:19:11 2020

@author: pedroaugustofreitasdearaujo
"""

from propeller_data_util import prop_File_Filter
import os

import pandas as pd




geometric_files = prop_File_Filter(os.getcwd()  + "/Propeller_Data_V2",contains="geom")

static_files = prop_File_Filter(os.getcwd()  + "/Propeller_Data_V2",contains="static")



geo_test = pd.DataFrame({'filename' : geometric_files[0], 
                         'diameter' : geometric_files[1],
                         'pitch' : geometric_files[2],
                         'path' : geometric_files[3]})


stat_test = pd.DataFrame({'filename' : static_files[0],
                            'diameter' : static_files[1],
                            'pitch' : static_files[2],
                            'path' : static_files[3]})



geo_test = geo_test.sort_values(by='filename')

stat_test = stat_test.sort_values(by='filename')

dummy_col = []


'''TODO FIND OUT HOW TO GET ALL PATHS FROM STATIC TO APPEND TO GEO_TEST'''

# Finding static files that have a geometric file
for i,fname in enumerate(stat_test['filename']):
    print(fname[0])
    pass


