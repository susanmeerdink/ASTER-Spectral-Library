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
##inMetaFileName = "C:\\Users\\Susan\\Documents\\GitHub\\ASTER-Spectral-Library\\Example_Metadata.csv"
##inASDFileName = "C:\\Users\\Susan\\Documents\\GitHub\\ASTER-Spectral-Library\\Example_Spectra_ASD.csv"
##inNicoletFileName = "C:\\Users\\Susan\\Documents\\GitHub\\ASTER-Spectral-Library\\Example_Spectra_Nicolet.csv"
##outDir = "C:\\Users\\Susan\\Documents\\GitHub\\ASTER-Spectral-Library\\Output Spectral Libraries\\"

inMetaFileName = "F:\\Dropbox\\Analysis\\ASTER Spectral Library\\Input Spectral Library Files\\Huntington_Gardens_Metadata.csv"
inASDFileName = "F:\\Dropbox\\Analysis\\ASTER Spectral Library\\Input Spectral Library Files\\Huntington_Gardens_Spectra_ASD.csv"
inNicoletFileName = "F:\\Dropbox\\Analysis\\ASTER Spectral Library\\Input Spectral Library Files\\Huntington_Gardens_Spectra_Nicolet.csv"
outDir = "F:\\Dropbox\\Analysis\\ASTER Spectral Library\\ASTER Spectral Library Files\\"
# ---------------------------------------------------------------------

import numpy as np #import numpy for array manipulation
import textwrap #import textwrap to make the description on six lines

inMetaFile = open(inMetaFileName,'r') #Open metadata file
inASDFile = open(inASDFileName,'r') #Open ASD spectra file
inNicoletFile = open(inNicoletFileName,'r') #Open Nicolet spectra file

## READING IN DATA
numRow = 0 # Keeps a counter of the number of rows
arrayMeta = [] # empty array to hold meta data
arrayASD = [] # empty array to hold ASD spectra data
arrayNicolet = [] # empty array to hold Nicolet spectra data

for line in inMetaFile: # Loop through the Metadata file
    strLine = line.split(",")

    if numRow == 0: # if this is the first row
        strLine[len(strLine)-1] = strLine[len(strLine)-1].rstrip('\n') # removing newline character from last field
        headersMeta = strLine # Store the first line for output files
        descriptIndex = strLine.index('Description')
        addinfoIndex = strLine.index('Additional Information')
        headersMeta.insert(descriptIndex + 1,' ')
        headersMeta.insert(descriptIndex + 2,' ')
        headersMeta.insert(descriptIndex + 3,' ')
        headersMeta.insert(descriptIndex + 4,' ')
        headersMeta.insert(descriptIndex + 5,' ')
        numRow = numRow + 1 # advance counter
    else: # if it isn't the first row              
        strTemp = ['None']*25
        descript = textwrap.wrap(strLine[descriptIndex],initial_indent = 'Description: ')
        strTemp[0:descriptIndex - 1] = strLine[0:descriptIndex]
        for i in range(0,6):
            if i < len(descript):
                strTemp[descriptIndex + i] = descript[i]
            else:
                strTemp[descriptIndex + i] = ''
        strTemp[16:-1] = strLine[descriptIndex + 1:addinfoIndex]
        arrayMeta.append(strTemp)

numRow = 0 # restart counter
for line in inASDFile: # loop through ASD file
    strLine = line.split(",")

    if numRow == 0: # if this is the first row
        strLine[len(strLine)-1] = strLine[len(strLine)-1].rstrip('\n') # removing newline character from last field
        headersASD = strLine # Store the first line for output files
        numRow = numRow + 1 # advance counter
    else: # if it isn't the first row
        arrayASD.append(strLine)

numRow = 0 # restart counter
for line in inNicoletFile: #loop through Nicolet file
    strLine = line.split(",")

    if numRow == 0: # if this is the first row
        strLine[len(strLine)- 1] = strLine[len(strLine)- 1].rstrip('\n') #removing newline character from last field
        headersNicolet = strLine #Store the first line for output files
        numRow = numRow + 1 # advance counter
    else: # if it isn't the first row
        arrayNicolet.append(strLine)

## OUTPUTING DATA
for row in range(len(arrayMeta)):
    if 'non' in arrayMeta[row][1]: # if it's non photosynthetic vegetation spectra name file this way
        # Output file name format: location.instrument.type.class.genus.species.samplenumber.filetype.txt
        # Example file name format: jpl.asdnicolet.npv.bark.abies.concolor.vh311.spectrum.txt
        outFileName = outDir + ('jpl.asdnicolet.npvegetation.' + arrayMeta[row][3] + '.' + arrayMeta[row][4] + '.' + arrayMeta[row][5] + '.spectrum.txt').lower()
        addinfoLine = ('jpl.asdnicolet.npvegetation.' + arrayMeta[row][3] + '.' + arrayMeta[row][4] + '.' + arrayMeta[row][5] + '.ancillary.txt').lower()
        outFile = open(outFileName,'w') #open file
    else:    # if it's vegetation spectra name file this way
        # Output file name format: location.instrument.type.class.genus.species.samplenumber.filetype.txt
        # Example file name format: jpl.asdnicolet.vegetation.class.aloe.bainesii.jpl057.spectrum.txt
        outFileName = outDir + ('jpl.asdnicolet.vegetation.' + arrayMeta[row][2] + '.' + arrayMeta[row][3] + '.' + arrayMeta[row][4] + '.spectrum.txt').lower()
        addinfoLine = ('jpl.asdnicolet.vegetation.' + arrayMeta[row][2] + '.' + arrayMeta[row][3] + '.' + arrayMeta[row][4] + '.ancillary.txt').lower()
        outFile = open(outFileName,'w') # open file

    #Outputing Metadata
    for i in range(len(headersMeta)): # loop through metadata fields
        if i == len(headersMeta) - 1:
            outFile.write(headersMeta[i] + ': ' + addinfoLine + '\n')
            outFile.write('\n')
        elif i in range(descriptIndex, descriptIndex + 6):
            outFile.write(arrayMeta[row][i] + '\n')
        else:
            outFile.write(headersMeta[i] + ': ' + arrayMeta[row][i] + '\n')

    for j in range(1,len(headersASD)): # loop through asd fields
        outFile.write(headersASD[j] + "   " + ("{0:.7s}".format(arrayASD[row][j])) + '\n')

    for k in range(1,len(headersNicolet)): # loop through nicolet fields
        if arrayNicolet[row][k] != "":
            outFile.write(headersNicolet[k] + "   " + ("{0:.7s}".format(arrayNicolet[row][k])) + '\n')

    outFile.close() # close file so it can be reused at the beginning

print('Finished Converting to ASTER Spectral Library Files')
    


        
    


