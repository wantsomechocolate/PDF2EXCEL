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


## TESTING DIRECTORY
wdir="C:/Users/James McGlynn/My Programs/Python Programs/pdf2txt/CompareExperiment/compare/images"

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
blur_count=1
blur_percent_x=0.1
blur_percent_y=0.1
blur_method=0 
blur_output_mode=0
threshold=225


time1=time()
## THIS IS WHERE THE IMAGES ARE PREPARED FOR COMPARISON
## THE IMAGES ARE BLURRED AND SHRUNKEN A CERTAIN AMOUNT OF TIMES
for i in range(len(image_handle_list)):
    ## BLUR IMAGE
    im_blur=compare.blurify(image_handle_list[i][0],blur_count,blur_percent_x,blur_percent_y,blur_output_mode,blur_method,threshold)
    ## RESIZE IMAGE TO 256x256
    im_resized=compare.resizify(im_blur,(256,256))
    ## BLUR IT AGAIN
    im_blur=compare.blurify(im_resized,blur_count,blur_percent_x,blur_percent_y,0,blur_method,220)
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
print (time3-time2)/float(60),
print " minutes"

## KEEP THIS AROUND FOR EASY PRINTING OF COMPARISON RESULTS
##for item in image_comparison_list:
##	print os.path.basename(item[0].filename),
##	print os.path.basename(item[1].filename),
##	print item[2]



im2compare="compare_05.png"
thresh=99 
compare.compare_results_one_image(image_comparison_list,im2compare,thresh)
			








