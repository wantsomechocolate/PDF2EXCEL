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

def blur2bnw(pil_image_handle,h_blur,v_blur):

    blur_matrix=(h_blur,v_blur)
        
    imcv2=np.array(pil_image_handle)
        
    im_blur=cv2.GaussianBlur(imcv2,blur_matrix,0)

    #im_blur=cv2.blur(imcv2,blur_matrix)

    thresh = 225
    
    im_blur_bnw = cv2.threshold(im_blur, thresh, 255, cv2.THRESH_BINARY)[1]
    
    #(thresh, im_blur_bnw) = cv2.threshold(im_blur, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

##    im_blur_bnw=cv2gray2bnw(im_blur, thresh)
    
    im=pili.fromarray(im_blur_bnw)
    
    return im
    

##def cv2gray2bnw(grayscale_np_array, thresh):
##    im=grayscale_np_array
##    #thresh=200
##    for r in range(len(im)):
##        for p in range(len(im[r])):
##            if im[r][p]>thresh:
##                im[r][p]=255
##            elif im[r][p]<thresh:
##                print "didn't meet thresh"
##                im[r][p]=0
##    return im

##file1='im2.png'
##file2='im4.png'
# read images as 2D arrays (convert to grayscale for simplicity)
#img1 = to_grayscale(imread(file1).astype(float))
#img2 = to_grayscale(imread(file2).astype(float))
# compare
##n_m, n_0 = compare_images(img1, img2)
##print "Manhattan norm:", n_m, "/ per pixel:", n_m/img1.size
##print "Zero norm:", n_0, "/ per pixel:", n_0*1.0/img1.size
 
#if __name__ == "__main__":
#    main()
