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
 
## Under normal usage this should take two black and white image handles
 
def compare_images(img1, img2):
    blur_weight=100
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
 
##def to_grayscale(arr):
##    "If arr is a color image (3D array), convert it to grayscale (2D array)."
##    if len(arr.shape) == 3:
##        return average(arr, -1)  # average over the last axis (color channels)
##    else:
##        return arr
 
def normalize(arr):
    rng = arr.max()-arr.min()
    amin = arr.min()
    return (arr-amin)*255/rng

def blurify(pil_image_handle,blur_count,blur_percent_x,blur_percent_y,output_mode,blur_method,thresh_or_auto):

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
