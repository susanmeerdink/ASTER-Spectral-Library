# Create Ancillary Data for ASTER Spectral Library
# Susan Meerdink
# 3/29/17
# https://github.com/susanmeerdink/ASTER-Spectral-Library
# This code reads in a csv with additional information to create text files with ancillary data for ASTER/ECOSTRESS
# spectral library. The first column of the Ancillary data must be Additional Information: TRUE or FALSE
# INPUTS----------------------------------------------------------------------------------------------------------------
inAncFileName = "C:\\Users\\Susan\\Documents\\GitHub\\ASTER-Spectral-Library\\Example_Ancillary.csv"
outDir = "C:\\Users\\Susan\\Documents\\GitHub\\ASTER-Spectral-Library\\Output Spectral Libraries\\"
# ----------------------------------------------------------------------------------------------------------------------

# Reading in Data
numRow = 0  # Keeps a counter of the number of rows
arrayAnc = []  # empty array to hold meta data

for line in open(inAncFileName):
    strLine = line.split(',')
    strLine[len(strLine) - 1] = strLine[len(strLine) - 1].rstrip('\n')  # removing newline character from last field
    if numRow == 0:  # if this is the first row
        headersMeta = strLine  # Store the first line for output files
    else:
        arrayAnc.append(strLine)
    numRow += 1

# Output Data
rowCount = 0
for row in range(len(arrayAnc)):
    if 'TRUE' in arrayAnc[row][0]:
        # Output file name format: location.instrument.type.class.genus.species.samplenumber.filetype.txt
        # Example file name format: jpl.asdnicolet.npvegetation.bark.abies.concolor.vh311.ancillary.txt
        outFileName = outDir + (arrayAnc[row][7] + '.asdnicolet.' + arrayAnc[row][2] + '.' + arrayAnc[row][3] + '.' + arrayAnc[row][4] + '.' + arrayAnc[row][5] + '.' + arrayAnc[row][6] + '.ancillary.txt').lower()
        outFile = open(outFileName, 'w')  # open file

        for i in range(1, len(headersMeta)):
            outFile.write(headersMeta[i] + ': ' + arrayAnc[row][i] + '\n')

        outFile.close()
        rowCount += 1
    else:
        continue

print '%s ancillary files were created out of %s samples' %(rowCount, len(arrayAnc))