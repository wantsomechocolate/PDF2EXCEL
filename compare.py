## Code below was adapted from the compare.py file offered in stack overflow user sastanin's
## answer from the discussion found at the following link
## http://stackoverflow.com/questions/189943/how-can-i-quantify-difference-between-two-images
 
import sys
from scipy.misc import imread
from scipy.linalg import norm
from scipy import sum, average
import cv2
from PIL import Image as pili
import numpy as np
import os
 
## Under normal usage this should take two black and white image handles
 
def compare_images(img1, img2):
    blur_weight=20
    blur_weight=(blur_weight,blur_weight)

    # normalize to compensate for exposure difference
    img1 = normalize(img1)
    img2 = normalize(img2)

    ## Blur both images
    img1=cv2.blur(img1,blur_weight)
    img2=cv2.blur(img2,blur_weight)

    
    # calculate the difference and its norms
    diff = img1 - img2  # elementwise for scipy arrays
    m_norm = round(float(sum(abs(diff)))/float(img1.size),6)  # Manhattan norm
    z_norm = round(float(norm(diff.ravel(), 0))/float(img1.size),6)  # Zero norm
    return (m_norm, z_norm)
 
def normalize(arr):
    rng = arr.max()-arr.min()
    amin = arr.min()
    return (arr-amin)*255/rng

def blurify(pil_image_handle,blur_count):#,blur_percent_x,blur_percent_y,output_mode,blur_method,thresh_or_auto):

    ## blur_count: How many times to perform the blur process with the same blur parameters
    ## blur_percent: what percent of the image size should the blur space be?
    ## output_mode: black and white (0) or grayscale(1)
    ## blur_method: regular cv2.blur (1) or gassian blur (0)
    ## thresh or auto: either auto (0) or a number from 1 to 255 that serves as the parameter for converting from
        ## grayscale to black and white

    ## some decent values:
    ####blur_count=3
    ####blur_percent_x=0.1
    ####blur_percent_y=0.1
    ####blur_method=0 #Gaussian
    ####blur_output_mode=0 #black and white
    ####threshold=225 #0 would be auto select, this has no effect when outputting grayscale

    #blur_count1=0
    #blur_count2=1
    blur_percent_x=0.25
    blur_percent_y=0.25
    blur_method=0
    output_mode=0
    thresh_or_auto=240

    for j in range(blur_count):
        hblur=int(pil_image_handle.size[0]*blur_percent_x)
        if hblur%2==0:
            hblur=hblur+1
        vblur=int(pil_image_handle.size[1]*blur_percent_y)
        if vblur%2==0:
            vblur=vblur+1
    blur_matrix=(hblur,vblur)
        
    im_blur=np.array(pil_image_handle)

    if blur_method==0:
        for i in range(blur_count):
            im_blur=cv2.GaussianBlur(im_blur,blur_matrix,0)
            if output_mode==1: pass
            elif output_mode==0:
                if thresh_or_auto==0:
                    (thresh, im_blur) = cv2.threshold(im_blur, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
                else:
                    im_blur = cv2.threshold(im_blur, thresh_or_auto, 255, cv2.THRESH_BINARY)[1]

    elif blur_method==1:
        for i in range(blur_count):
            im_blur=cv2.blur(im_blur,blur_matrix)
            if output_mode==1: pass
            elif output_mode==0:
                if thresh_or_auto==0:
                    (thresh, im_blur) = cv2.threshold(im_blur, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
                else:
                    im_blur = cv2.threshold(im_blur, thresh_or_auto, 255, cv2.THRESH_BINARY)[1]

    else: print "Blur method not supported"
    
    im=pili.fromarray(im_blur)
    
    return im
    

def resizify(im_handle,size_tuple):
    im_resize=im_handle.resize(size_tuple)
    return im_resize

def pixel_compare(im1,im2):
    imh=im1.size[0]
    imw=im1.size[1]
    ## Expects two pictures with the same everything, black and white or grayscale.
    im1=np.array(im1)
    im2=np.array(im2)
    diff=float(sum(abs(im1-im2)))/float((imh*imw*255))
    sameness=1-diff
    return sameness


def sort_list_of_image_handles(list_to_sort):
    sorted_list=[]

    list_to_sort=set(list_to_sort)

# Strip filenames from the image handles to sort based on alphabet
    for item in list_to_sort:
        sorted_list.append(os.path.basename(item.filename))

    # Standard sort
    sorted_list.sort()

    # I don't understand why this works, but it takes the image_handle_list (list of image handles)
    # and moves its contents around to match the order of the the sorted list (list of strings)
    for item in list_to_sort:
        list_to_sort[sorted_list.index(os.path.basename(item.filename))]=item

    return list_to_sort

def compare_results_one_image_return_set(image_comparison_list,filename,percent_sim_thresh):
    #print "Below are image results for ",
    #print filename
    group=[]
    for item in image_comparison_list:
            if os.path.basename(item[0].filename) == filename:
                    if item[2]>percent_sim_thresh:
##                            print os.path.basename(item[0].filename),
##                            print os.path.basename(item[1].filename),
##                            print item[2]
                            group.append(item[0])
                            group.append(item[1])
            elif os.path.basename(item[1].filename)== filename:
                    if item[2]>percent_sim_thresh:
##                            print os.path.basename(item[0].filename),
##                            print os.path.basename(item[1].filename),
##                            print item[2]
                            group.append(item[0])
                            group.append(item[1])

    return set(group)























