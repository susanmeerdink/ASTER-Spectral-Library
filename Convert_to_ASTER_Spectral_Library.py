## Convert to ASTER Spectral Library
# Susan Meerdink
# 12/8/2016
# https://github.com/susanmeerdink/ASTER-Spectral-Library
# This project contains example spectra and metadata
# This code converts a csv of spectra and metadata into ASTER spectral library format
# This code takes four inputs
# 1) Metadata for spectra csv - no commas in metadata fields
# 2) ASD Spectra csv - must have the same order as metadata
# 3) Nicolet Spectra csv - must have the same order as metadata
# 4) Output directory for ASTER spectral library files
# INPUTS---------------------------------------------------------------------
inMetaFileName = "C:\\Users\\Susan\\Documents\\GitHub\\ASTER-Spectral-Library\\Example_Metadata.csv"
inASDFileName = "C:\\Users\\Susan\\Documents\\GitHub\\ASTER-Spectral-Library\\Example_Spectra_ASD.csv"
inNicoletFileName = "C:\\Users\\Susan\\Documents\\GitHub\\ASTER-Spectral-Library\\Example_Spectra_Nicolet.csv"
outDir = "C:\\Users\\Susan\\Documents\\GitHub\\ASTER-Spectral-Library\\Output Spectral Libraries\\"
# ---------------------------------------------------------------------

import numpy as np #import numpy for array manipulation

inMetaFile = open(inMetaFileName,'r') #Open metadata file
inASDFile = open(inASDFileName,'r') #Open ASD spectra file
inNicoletFile = open(inNicoletFileName,'r') #Open Nicolet spectra file

## READING IN DATA
numRow = 0 #Keeps a counter of the number of rows
arrayMeta = [] #empty array to hold meta data
arrayASD = [] #empty array to hold ASD spectra data
arrayNicolet = [] #empty array to hold Nicolet spectra data

for line in inMetaFile: #Loop through the Metadata file
    strLine = line.split(",")

    if numRow == 0: #if this is the first row
        strLine[len(strLine)-1] = strLine[len(strLine)-1].rstrip('\n') #removing newline character from last field
        headersMeta = strLine #Store the first line for output files
        numRow = numRow + 1 #advance counter
    else: #if it isn't the first row
        arrayMeta.append(strLine)

numRow = 0 #restart counter
for line in inASDFile: #loop through ASD file
    strLine = line.split(",")

    if numRow == 0: #if this is the first row
        strLine[len(strLine)-1] = strLine[len(strLine)-1].rstrip('\n') #removing newline character from last field
        headersASD = strLine #Store the first line for output files
        numRow = numRow + 1 #advance counter
    else: #if it isn't the first row
        arrayASD.append(strLine)

numRow = 0 #restart counter
for line in inNicoletFile: #loop through Nicolet file
    strLine = line.split(",")

    if numRow == 0: #if this is the first row
        strLine[len(strLine)-1] = strLine[len(strLine)-1].rstrip('\n') #removing newline character from last field
        headersNicolet = strLine #Store the first line for output files
        numRow = numRow + 1 #advance counter
    else: #if it isn't the first row
        arrayNicolet.append(strLine)

## OUTPUTING DATA
for row in range(len(arrayMeta)):
    outFileName = outDir + arrayMeta[row][0] + '-' + arrayMeta[row][19]+'.txt' #output file name is currently name-sampleID.txt
    outFile = open(outFileName,'w') #open file

    #Outputing Metadata
    for i in range(len(arrayMeta[row])-1): #loop through metadata fields
        outFile.write(headersMeta[i] + ': ' + arrayMeta[row][i] + '\n')

    for j in range(1,len(arrayASD[row])-1): #loop through asd fields
        outFile.write(headersASD[j] + "   " + arrayASD[row][j] + '\n')

    for k in range(1,len(arrayNicolet[row])-1): #loop through nicolet fields
        if arrayNicolet[row][k] != "":
            outFile.write(headersNicolet[k] + "   " + arrayNicolet[row][k] + '\n')

    outFile.close() #close file so it can be reused at the beginning 
    


        
    

