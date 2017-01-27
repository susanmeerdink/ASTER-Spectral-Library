# ASTER-Spectral-Library
Code associated with getting spectral libraries into the ASTER spectral library format

## Input Spectra Format
First row is wavelength
First column is spectrum ID
See Example_Spectra_ASD.csv and Example_Spectra_Nicolet.csv
If a sample does not have an associated ASD or Nicolet spectrum, create a row with that sample's ID but leave wavelength columns empty.

## Input Metadata Format
See Metadata_Template for a csv format. Each row is a spectrum's metadata, while each column is a metadata field
Also see Example_Metadata.csv

### Metadata Fields with Explanations:
  * `Name (REQ): 	
  * `Description (REQ) :
  * `Affiliation (REQ): 	
  * `Measurement Type (Lab, Field, Remote) (REQ):	
  * `Instrument (REQ):	
  * `Illumination Geometry (REQ) :		
  * `Observation Geometry w/ FOV and Distance (REQ) :	
  * `Calibration (eg: type of reflectance, spectralon, gold)  (REQ):	
  * `Location (lat, lon, Datum)  (REQ):	
  * `Collection Date (REQ) :	
  * `Kingdom :	
  * `Family :	
  * `Genus : 	
  * `species :
  * `Scale (eg: leaf, canopy, mixed) :
  * `Material Age :
  * `Height (eg: canopy height, water depth) :
  * `Chemistry (eg: nitrogen, lignin, pigments) :		
  * `Biophysical Properties (eg: specific leaf area, thickness) :		
  * `Sample No. :
  * `Additional Information : 		
  * `Reference Document :	
  * `Point of Contact :		
  * `Acknowledgement : 
  * `Column names (eg: wavelength, reflectance, fwhm) (REQ) :		
  * `Column units (eg: nanometers, percent, nanometers) (REQ):	
  
NOTES:
None of the fields can have a comma as the code splits columns on the comma.
