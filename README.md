# ASTER-Spectral-Library
Code associated with getting spectral libraries into the ASTER spectral library format (Soon to be renamed ECOSTRESS spectral library). Current library can be found here: https://speclib.jpl.nasa.gov/. In the library, each sample is a separate text file that contains 20 lines of header or metadata values and then the spectra associated with that sample. This repository is for vegetation and non-photosynthetic vegetation (NPV) spectral library files.

## Input Spectra Format
First row is wavelength
First column is spectrum ID
See Example_Spectra_ASD.csv and Example_Spectra_Nicolet.csv
If a sample does not have an associated ASD or Nicolet spectrum, create a row with that sample's ID but leave wavelength columns empty.

## Input Metadata Format
See Metadata_Template for a csv format. Each row is a samples's metadata, while each column is a metadata field
Also see Example_Metadata.csv

## Input Ancillary Data Format
See Example_Ancillary.csv for example format. The first column of ancillary data must be Additional Information with a value of TRUE or FALSE for each sample (aka row). In addition, Name, Type, Class, Genus, Species, Sample No., and Owner must also be included for proper naming of ancillary data file. This file is to include ANY information that did not fit into the ASTER/ECOSTRESS metadata fields. You can have as much additional text and values as neccessary. Each column of ancillary data will be a new row in the ancillary text file. 

### Metadata Fields:
	* The numbering donates which line the metadata values can be found
	1. Name
	2. Type
	3. Class
	4. Genus
	5. species
	6. Sample No.
	7. Owner
	8. Wavelength Range
	9. Origin
	10. Collection Date
	11. Description
	12. Measurement
	13. First Column
	14. Second Column
	15. X Units
	16. Y Units
	17. First X Value
	18. Last X Value
	19. Number of X Values
	20. Additional Information: if value is TRUE this cateogory will be set to the ancillary text file name
	21. Empty Space
	22. List of Spectra Start on this line
	
NOTES:
None of the fields can have a comma as the code splits columns on the comma.
