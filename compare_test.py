##Figure out how to blur convert to black and white, blur again, convert to black and white

import compare
from PIL import Image as pili
import os
import cv2
import numpy as np
from marbles import glass as useful

wdir="C:/Users/James McGlynn/My Programs/Python Programs/pdf2txt/CompareExperiment/compare/"

function="blur5x101/"

image_handle_list=[]

for item in os.listdir(wdir):
    if item[-4:]=='.png':
        image_full_path=wdir+'/'+item
        image_handle=pili.open(image_full_path)
        image_handle_list.append(image_handle)

outputDirectory=wdir+function
if not os.path.exists(outputDirectory): os.makedirs(outputDirectory)

for i in range(len(image_handle_list)):
    image_filename=os.path.basename(image_handle_list[i].filename)
    image_save_filename=useful.add_to_filename(image_filename,"_"+str(i))
    image_save_path=outputDirectory+image_filename
    
    im_blur=compare.blur(image_handle_list[i],5,101)

    im_blur=im_blur.convert('1')
    
    im_blur.save(image_save_path)

##image_path='compare_2.png'
##im=pili.open(image_path)
##im=im.resize((im.size[0]/4,im.size[1]/4))
##im=np.array(im)
##im=cv2.blur(im,(5,5))
##
##im=pili.fromarray(im)
##
##im.save('compare_2_blur.png')





####compare_list=[]
####for i in range(len(image_handle_list)):
####    for j in range(1,len(image_handle_list)):
####        if i<j:
####            m_norm, z_norm = compare.compare_images(np.array(image_handle_list[i]), np.array(image_handle_list[j]))
####            compare_list.append([os.path.basename(image_handle_list[i].filename),os.path.basename(image_handle_list[j].filename),m_norm,z_norm])
####
####for item in compare_list: print item
