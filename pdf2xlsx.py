# -*- coding: cp1252 -*-


## 2,5,8,11,14,17,20,23,26,29

## messing around with breaking the image up into sections so the ocred text makes more sense
##########from PIL import Image
##########import ocr_module
##########
##########im = Image.open('C:/Users/James McGlynn/My Programs/Python Programs/pdf2txt/WorkRelated/APF/24 West 57 Utilities/24 West 57 2011 3rd Floor Electric/Intermediates/24 West 57 2011 3rd Floor Electric_2.png')
##########
##########im1 = im.crop((0,0,im.size[0],180))
##########im1.save('croppedImageTest1.png')
##########page_text_1=ocr_module.img2txt('croppedImageTest1.png')
##########
##########im2=im.crop((0,180,im.size[0]/2,im.size[1]))
##########im2.save('croppedImageTest2.png')
##########page_text_2=ocr_module.img2txt('croppedImageTest2.png')
##########
##########im3=im.crop((im.size[0]/2,180,im.size[0],im.size[1]))
##########im3.save('croppedImageTest3.png')
##########page_text_3=ocr_module.img2txt('croppedImageTest3.png')
##########
##########page_text=page_text_1+page_text_2+page_text_3
##########print page_text



##fix problem with having percentage arguments to a pixel function

## The program won't run again until you also fix problem with saving shit in the right place.
## Specifically in the pdf2txt function in the ocr module.




## Required Work

## Multiple PDF Input - Done

## Intelligently select utility

## Exclude Pages without data. 

## Problem with encoding came back WTFFFFFF

## Add stored regexes for "pure numbers" "decimal numbers"
## Currency, kwh, kw, etc.

## Also consider adding option to split pages into different sections
## Perhaps include that information in the utility library.
## There are some con ed bills for example that would be much better analyzed
## if they were split down the middle. (keeping the top in tact)

## Write a regex test platform
## Write a regex creation platform

## make it so that people can make utility templates on the fly that
## Gathered only the required data. (like highlighting the areas with
## data and ocr-ing only those areas.

## Collect vicinity text - regex used to match - the match itself.
## everytime the program runs - as well as information about the bill
## type. 


import useful as jc
import ocr_module as ocr
import extraction_module as exmo

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

## Put this stuff in a file?
scale_factorx = 4    #Each page of each PDF gets magnified by this
extx='.png'          #Desired Image Extension
page_numx=1


## For every PDF in the directory/ Selection
for pdf in pdf_paths:

    num_pagesx=ocr.getNumPages(pdf) ## Get num of pages in pdf

    #This function generates all the OCR test at once, I want to do it by page and then
    # extract just that page of data. That way if something goes awry, You still have the
    # spreadsheet with the data up to where the program erred.
    # But then I would need to iterate through pages out here and pass the page
    # number to both functions. Not actually that hard.
    
    output_file=ocr.pdf2txt(pdf,page_numx,scale_factorx,extx,num_pagesx,util_lib)
        
    book_name=exmo.txt2xlsx(output_file,util_lib,unicode_charsx)






