# -*- coding: cp1252 -*-
## Required Work
## Multiple PDF Input
## Intelligently select utility
## Exclude Pages without data. 
## Problem with encoding came back WTFFFFFF

import useful as jc
import ocr_module as ocr
import extraction_module as exmo
import tesseract 


unicode_charsx={"—":"-","‘":"'","’":"'","é":"e",'“':'"',"‘":"'"}

#-----------------------------------------------------------------------------------------
#Step one: Check to see if there is a default/most recent directory to use as
# argument for get_Path
#-----------------------------------------------------------------------------------------

default_directory=jc.get_default_directory()

util_lib_filename="Utility_Libraries"

util_lib_path=default_directory+'/'+util_lib_filename

list_of_utilsx=exmo.get_utility_list(util_lib_path)

## Get the utility being analyzed from the uuusseeeeer
util=exmo.get_current_utility(list_of_utilsx)
print "You Selected "+str(util)
util_lib_loc=exmo.get_utility_library_directory()
util_lib=exmo.get_utility_library(util,util_lib_loc)


#-----------------------------------------------------------------------------------------
#Step ???: Ask user to navigate to the pdf file/directory
#-----------------------------------------------------------------------------------------
print "Use File Open Dialog to Choose Target PDFS"
pdf_paths=jc.getPaths(default_directory)

#-----------------------------------------------------------------------------------------
#Step three: Generate text file containing the ocr'ed text
#-----------------------------------------------------------------------------------------

##  Initializations for Tess
apix = tesseract.TessBaseAPI()   
apix.SetOutputName("outputName");
apix.Init(".","eng",tesseract.OEM_DEFAULT)
apix.SetPageSegMode(tesseract.PSM_AUTO)

## Put this stuff in a file?
scale_factorx = 4    #Each page of each PDF gets magnified by this
extx='.png'          #Desired Image Extension
page_numx=1

## This has to be automated or asked of the user
#utility="Consolidated Edison"
#utility="Castle Oil"

## For every PDF in the directory/ Selection
for pdf in pdf_paths:

    num_pagesx=ocr.getNumPages(pdf) ## Get num of pages in pdf

    #This function generates all the OCR test at once, I want to do it by page and then
    # extract just that page of data. That way if something goes awry, You still have the
    # spreadsheet with the data up to where the program erred.
    # But then I would need to iterate through pages out here and pass the page
    # number to both functions. Not actually that hard.
    
    output_file=ocr.pdf2txt(pdf,page_numx,scale_factorx,extx,num_pagesx,apix)
        
    book_name=exmo.txt2xlsx(output_file,util_lib,unicode_charsx)























