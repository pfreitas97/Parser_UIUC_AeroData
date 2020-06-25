#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: pfreitas97

Helper file to download both datasets directly if you'd like the complete data (with pictures, a report, etc...)
as opposed to just the raw files I uploaded.

This script can be run with your favorite IDE or just the run of the mill command line and it'll download and unzip
both datasets to wherever your current directory is.

"""

import requests, zipfile, io


# File paths for each database

PROPELLER_URL = "https://m-selig.ae.illinois.edu/props/download/UIUC-propDB.zip"

AIRFOIL_COORD_URL = "https://m-selig.ae.illinois.edu/ads/archives/coord_seligFmt.zip"


# NOTE: If you encounter issues with the propeller database, it is likely an issue with the server in that case
# simply use the link below to download the files directly:
    
PROP_BACKUP_URL = "https://m-selig.ae.illinois.edu/props/propDB.html"
AIRFOIL_BACKUP_URL = "https://m-selig.ae.illinois.edu/ads/coord_database.html"
   




r = requests.get(PROPELLER_URL)

if r.ok:
    PROP_Zip = zipfile.ZipFile(io.BytesIO(r.content))
    PROP_Zip.extractall()
else:
    print("Oh  oh server trouble... please download the file directly at %s it should be as \
          simple as clicking a link."
           % PROP_BACKUP_URL)


rFoil = requests.get(AIRFOIL_COORD_URL)

if rFoil.ok:
    AIR_Zip = zipfile.ZipFile(io.BytesIO(rFoil.content))
    AIR_Zip.extractall()
else:
    print("Oh  oh server trouble... please download the file directly at %s it should be as simple as clicking a link. \
           The Zip file you're looking for is in the Archives section. Search for 'Zip archive' "
           % AIRFOIL_BACKUP_URL)





