## Code below was adapted from the compare.py file offered in stack overflow user sastanin's
## answer from the discussion found at the following link
## http://stackoverflow.com/questions/189943/how-can-i-quantify-difference-between-two-images
 
import sys
from scipy.misc import imread
from scipy.linalg import norm
from scipy import sum, average
import cv2
 
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

    cv2.imwrite('asdf.png',img1)
    
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
