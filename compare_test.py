## TESTING GROUND FOR COMPARING TEXT BASED IMAGES

## IMPORT COMPARE (WRITTEN BY ME)
import compare
## GET THE PYTHON IMAGE LIBRARY UP IN HERE
from PIL import Image as pili
## IMPORT OS MAINLY TO GET FILENAMES FROM PATHS
import os
## IPMORT OPEN CV FOR IMAGE ARRAY MANIPULATION
import cv2
## IMPORT NUMPY BECAUSE OPEN CV USES NUMPY ARRAYS FOR STORING IMAGE DATA
import numpy as np
## IMPORT A "PACKAGE" I MADE TO STORE SOME USEFUL FUNCTIONS IN
from marbles import glass as useful
## IMPORT TIME SO KNOW HOW LONG STUFF TAKES
from time import time

from openpyxl import Workbook
from openpyxl import load_workbook


## TESTING DIRECTORY
wdir="C:/Users/James McGlynn/My Programs/Python Programs/pdf2txt/CompareExperiment/compare/images/"

## GET A LIST OF PNG IMAGES FROM A GIVEN DIRECTORY
image_handle_list=useful.image_handles_from_dir_png(wdir)

## SORT THE LIST BECAUSE IT HELPS ME ANALYZE RESULTS
sorted_list=[]
for item in image_handle_list:
    sorted_list.append(os.path.basename(item[0].filename))
sorted_list.sort()
for item in image_handle_list:
    image_handle_list[sorted_list.index(os.path.basename(item[0].filename))]=item

## THESE ARE INITILIZATIONS FOR BLUR. I MIGHT PUT THESE INTO THE FUNCTION.
## THEY ARE CLUTTERING THE PLACE UP. 
blur_count=0
blur_percent_x=0.10
blur_percent_y=0.10
blur_method=0
blur_output_mode=0
threshold=220


time1=time()
## THIS IS WHERE THE IMAGES ARE PREPARED FOR COMPARISON
## THE IMAGES ARE BLURRED AND SHRUNKEN A CERTAIN AMOUNT OF TIMES
for i in range(len(image_handle_list)):
    ## BLUR IMAGE
    if blur_count>0:
        im_blur=compare.blurify(image_handle_list[i][0],blur_count,blur_percent_x,blur_percent_y,blur_output_mode,blur_method,threshold)
    else:
        im_blur=image_handle_list[i][0]
    ## RESIZE IMAGE TO 256x256
    im_resized=compare.resizify(im_blur,(256,256))
    ## BLUR IT AGAIN
    if blur_count>0:
        im_blur=compare.blurify(im_resized,blur_count,blur_percent_x,blur_percent_y,0,blur_method,220)
    else:
        im_blur=im_resized
    ## RESIZE AGAIN......?
    ## NO. im_resized=compare.resizify(im_blur,(16,16))
    im_final=im_blur
    ## ADD EDITED IMAGE TO HANDLE LIST. THIS PRODUCES A LIST OF THE SAME LENGTH BUT WITH
    ## TWO ITEMS PER ITEM IN THE LIST (IMAGE AND EDITED IMAGE)
    image_handle_list[i].append(im_final)

time2=time()
print "Preparing all images took ",
print (time2-time1)/float(60),
print " minutes"


image_comparison_list=[]
for i in range(len(image_handle_list)):
    for j in range(len(image_handle_list)):
        if i<j:
            percent_sim=compare.pixel_compare(image_handle_list[i][1],image_handle_list[j][1])
            image_comparison_list.append([image_handle_list[i][0],image_handle_list[j][0],percent_sim])

time3=time()
print "Comparing all images took ",
print (time3-time2),
print " seconds"

## KEEP THIS AROUND FOR EASY PRINTING OF COMPARISON RESULTS
##for item in image_comparison_list:
##	print os.path.basename(item[0].filename),
##	print os.path.basename(item[1].filename),
##	print item[2]

book_name=wdir+'compare.xlsx'
wb = Workbook()
ws=wb.get_active_sheet()

c=ws.cell(row=0, column=0)
c.value="Image One"
c=ws.cell(row=0, column=1)
c.value="Image Two"
c=ws.cell(row=0, column=2)
c.value="Similarity"

for i in range(len(image_comparison_list)):
    #for j in range(len(image_comparison_list[i])):
    c=ws.cell(row=i+1, column=0)
    c.value=os.path.basename(image_comparison_list[i][0].filename)
    c=ws.cell(row=i+1, column=1)
    c.value=os.path.basename(image_comparison_list[i][1].filename)
    c=ws.cell(row=i+1, column=2)
    c.value=image_comparison_list[i][2]

wb.save(book_name)



##im2compare="compare_05.png"
##thresh=99 
##compare.compare_results_one_image(image_comparison_list,im2compare,thresh)
			


##def print_to_workbook(data_order_list,dict_to_print,source_path,tab_name):
##    
##    ## Openpyxl library imports
##    from openpyxl import Workbook
##    from openpyxl import load_workbook
##
##    ## Get the excel filename from the name of the text file that the user navigated to
##    book_name=source_path+'compare.xlsx'#jc.getFilenameFromPath(source_path)+'.xlsx'
##
##    try: ## Try opening the workbook with the same name"
##        #Found Workbook
##        wb=load_workbook(book_name)
##        new_wb=-1
##        try:
##            # Found tab
##            ws = wb.get_sheet_by_name(tab_name) #this does not error if it doesn't find what it wants
##            if ws==None:
##                1+"one"#throw error"
##            else:
##                pass
##        except:
##            #Found workbook, but didn't find tab"
##            ws=wb.create_sheet(-1,tab_name)
##            ws=wb.get_sheet_by_name(tab_name)
##            new_wb=-1
##            i=0
##            for key in data_order_list['library_info']['collection_order']:
##                c=ws.cell(row=0, column=i)
##                c.value=key
##                i=i+1
##        
##    except: ## If it doesn't exist then start a new workbook in memory
##        #Didn't find workbook
##        wb = Workbook()
##        ws = wb.create_sheet(-1,tab_name)
##        ws = wb.get_sheet_by_name(tab_name)
##        new_wb=1
##        i=0
##        for key in data_order_list['library_info']['collection_order']:
##            c=ws.cell(row=0, column=i)
##            c.value=key
##            i=i+1
##        
##    last_occ_row=ws.rows[-1][0].row
##    
##
##    i=0
##    for key in data_order_list['library_info']['collection_order']:
##
##        c=ws.cell(row=last_occ_row, column=i)
##        try:
##            c.value=dict_to_print[key].strip()
##        except:
##            #Using this area to keep track of encoding errors
##            print "This text caused an error"
##            print dict_to_print[key]
##            c.value="Raw text contained bad chars, see intepreter."
##            #c.value=dict_to_print[key]
##        i=i+1
##            
##    wb.save(book_name)
##    return book_name
##




