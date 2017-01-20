## Convert to ASTER Spectral Library
# Susan Meerdink
# 12/8/2016
# https://github.com/susanmeerdink/ASTER-Spectral-Library
# This project contains example spectra and metadata
# This code converts a csv of spectra and metadata into ASTER spectral library format
# This code takes four inputs
# 1) Metadata for spectra csv
# 2) ASD Spectra csv - must have the same order as metadata
# 3) Nicolet Spectra csv
# 4) Output directory for ASTER spectral library files
# INPUTS---------------------------------------------------------------------
inMetaFileName = "C:\\Users\\Susan\\Documents\\GitHub\\ASTER-Spectral-Library\\Example_Metadata.csv"
inASDFileName = "C:\\Users\\Susan\\Documents\\GitHub\\ASTER-Spectral-Library\\Example_Spectra_ASD.csv"
inNicoletFileName = "C:\\Users\\Susan\\Documents\\GitHub\\ASTER-Spectral-Library\\Example_Spectra_Nicolet.csv"
outDir = "F:\\Dropbox\\Analysis\\ASTER Spectral Library\\ASTER Spectral Library Files\\"
# ---------------------------------------------------------------------

import numpy as np #import numpy for array manipulation

inMetaFile = open(inMetaFileName,'r') #Open metadata file
inASDFile = open(inASDFileName,'r') #Open ASD spectra file
inNicoletFile = open(inNicoletFileName,'r') #Open Nicolet spectra file

numFile = 0 #Keeps a counter of the number of files or rows

for line in inMetaFile: #Loop through the Metadata file
    strLine = line.split(",");
    print (strLine)

    if numFile = 0: #if this is the first row
        header = strLine #Store the first line for output files
    


