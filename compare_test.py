##Figure out how to blur convert to black and white, blur again, convert to black and white

import compare
from PIL import Image as pili
import os
import cv2
import numpy as np
from marbles import glass as useful

wdir="C:/Users/James McGlynn/My Programs/Python Programs/pdf2txt/CompareExperiment/compare/"

function="resize_and_blur/"

image_handle_list=[]

for item in os.listdir(wdir):
    if item[-4:]=='.png':
        image_full_path=wdir+'/'+item
        image_handle=pili.open(image_full_path)
        image_handle_list.append(image_handle)

outputDirectory=wdir+function
if not os.path.exists(outputDirectory): os.makedirs(outputDirectory)

## Variables for blurring
blur_count=1
blur_percent_x=0.1
blur_percent_y=0.1
blur_method=0 
blur_output_mode=0
threshold=220

## Variables for resizing
new_width=256
new_height=256
size_tuple=(new_width,new_height)

for i in range(len(image_handle_list)):
    image_filename=os.path.basename(image_handle_list[i].filename)
    image_save_filename=useful.add_to_filename(image_filename,"_"+str(i))
    image_save_path=outputDirectory+image_filename

    ## For blurring the image
    im_blur=compare.blurify(image_handle_list[i],blur_count,blur_percent_x,blur_percent_y,blur_output_mode,blur_method,threshold)
    ## im_final=im_blur

    ## for resizing the image
    #im_resized=compare.resizify(image_handle_list[i],size_tuple)
    im_resized=compare.resizify(im_blur,size_tuple)

    im_blur=compare.blurify(im_resized,blur_count,blur_percent_x,blur_percent_y,0,blur_method,220)

    im_resized=compare.resizify(im_blur,(16,16))

    #im_blur=compare.blurify(im_resized,1,.1,.1,0,0,220)
    
    im_final=im_resized
    
    im_final.save(image_save_path)












