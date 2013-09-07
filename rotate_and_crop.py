## Auto rotate and crop function written by James McGlynn using
## Main Goal!
## Convert only to grayscale, no black and white!

## open cv python binding (cv2)
## python image library (PIL)
## and of course, numerical python (numpy)

## Input is a PIL image handle
## Output is a PIL image handle

## This function has been tested for color images
## and Grayscale/Black&White
## It was also tested with Jpegs and png files.

## For work with images using numpy arrays to stor pixel data
import cv2

## To work with images in a more intuitive easy, but less powerful, way
from PIL import Image as pili

## A special import I use specifically for inverting images (color inversion)
import PIL.ImageOps

## I use numpy mostly for going between PIL and cv2
import numpy as np

## I use this for deleting temp files
import os

## This is the main function that gets called to crop and rotate
def rotate_and_crop(pil_image_handle):

##    ## If the image is too large, than the program has a hard time finding Hough lines and
##    ## The skew angle gets all messed up. ## Apparently this isn't true. it's because the image is black and white
##    ## and the image loses data when converted to black and white. 
##    width_cutoff=1500
##    width_replace=1000
##    ## Get image dimensions
##    imw,imh=pil_image_handle.size
##    ## Check to see if image makes the cut
##    if imw>=width_cutoff:
##        print "Image was too large: Resizing"
##        nw=width_replace
##        nh=(float(nw)/float(imw))*imh
##        pil_image_handle=pil_image_handle.resize((int(nw),int(nh)))

    
    ## If the image is a color image
    if pil_image_handle.mode=="RGB":
        ## Load the pixel data into a numpy array
        im_cv2=np.array(pil_image_handle)
        ## Convert the pixel data into grayscale using opencv
        im_cv2_gray=cv2.cvtColor(im_cv2,cv2.COLOR_BGR2GRAY)
        ##Convert image to black and white
        #(thresh, im_cv2_bw) = cv2.threshold(im_cv2_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    ## If the image is RGBA
    elif pil_image_handle.mode=='RGBA':
        ## Convert to an RGB image
        pil_image_handle=pil_image_handle.convert('RGB')
        ## Load the pixel data into a numpy array
        im_cv2=np.array(pil_image_handle)
        ## Convert the pixel data into grayscale using opencv
        im_cv2_gray=cv2.cvtColor(im_cv2,cv2.COLOR_BGR2GRAY)
        ##Convert image to black and white
        #(thresh, im_cv2_bw) = cv2.threshold(im_cv2_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    elif pil_image_handle.mode=='P':
        ## Convert to an RGB image
        pil_image_handle=pil_image_handle.convert('RGB')
        ## Save image
        pil_image_handle.save('temp.png')
        ## Open Image
        pil_image_handle=pili.open('temp.png')
        ## Load the pixel data into a numpy array
        im_cv2=np.array(pil_image_handle)
        ## Delete Temp Image
        os.remove('temp.png')
        ## Convert the pixel data into grayscale using opencv
        im_cv2_gray=cv2.cvtColor(im_cv2,cv2.COLOR_BGR2GRAY)
        ##Convert image to black and white
        #(thresh, im_cv2_bw) = cv2.threshold(im_cv2_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        
    ## if the image is grayscale already (or is this B&W image mode)
    elif pil_image_handle.mode=="L":
        ## Just grab the pixel data
        im_cv2_gray=np.array(pil_image_handle)
        ##Convert image to black and white
        #(thresh, im_cv2_bw) = cv2.threshold(im_cv2_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    ## If it doens't meet any other criteria, try to grab the pixel
    ## Data. It might not work, but whatever.
    else:
        print "image wasn't RGB, RGBA, L, or P"
        try:
            ## Convert to an RGB image
            pil_image_handle=pil_image_handle.convert('RGB')
            ## Load the pixel data into a numpy array
            im_cv2=np.array(pil_image_handle)
            ## Convert the pixel data into grayscale using opencv
            im_cv2_gray=cv2.cvtColor(im_cv2,cv2.COLOR_BGR2GRAY)
            ##Convert image to black and white
            #(thresh, im_cv2_bw) = cv2.threshold(im_cv2_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        except:
            print "Image wouldn't convert to RGB"
            ## Just grab the pixel data
            im_cv2_gray=np.array(pil_image_handle)
            ##Convert image to black and white
            #(thresh, im_cv2_bw) = cv2.threshold(im_cv2_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    ## Now that the image has been numpified and is grayscale
    ## Use "fromarray" to create a PIL image handle using the grayscale data
    ## This might actually not be necessary if the image were already gray
    ## But for right now it's getting done.
    #im_pil=pili.fromarray(im_cv2_bw)
    im_pil=pili.fromarray(im_cv2_gray)
    
    ## Use a function from this file to calculate the angle of rotate
    ## based on Probabilistic Hough Lines
    #skew_angle=get_skew_angle(im_cv2_bw)
    skew_angle=get_skew_angle(im_cv2_gray)

##    ## If the skew angle comes back wonky then just set it to 0
##    if (float('-inf') < float(skew_angle) < float('inf'))==False:
##        print "Something went wrong when finding the skew_angle, image will not be straightened"
##        skew_angle=0
    
    ## Before rotating or finding the bounding box, the image must be color inverted
    ## because image editing functions see black as an absence of data
    im_invert=PIL.ImageOps.invert(im_pil)

    ## rotate the image based on the skew angle found earlier
    im_rot=im_invert.rotate(skew_angle)

    ## Now that the image is rotated to be straightened,
    ## Find the "bounding box" using a function from below
    ## I put bounding box in quotes because the function actually finds
    ## the box that contains certain criteria for exluding noise and such
    ## that a real bounding box would not ignore.
    bounding_box=get_bounding_box(im_rot)
    
    ## Invert the image so that the final product isn't color inverted
    im_rot_fin=PIL.ImageOps.invert(im_rot)
    
    ## Crop the image by giving bounding box as an argument for crop
    im_fin=im_rot_fin.crop(bounding_box)
    
    ## Return a PIL Image Handle that points to the rotated and cropped
    ## pixel data
    return im_fin

def get_skew_angle(cv2_grayscale_np_array):


    ## If the image is too large, than the program has a hard time finding Hough lines and
    ## The skew angle gets all messed up. 
    width_cutoff=1500
    width_replace=1000
    ## Get image dimensions
    imw,imh=cv2_grayscale_np_array.shape
    ## Check to see if image makes the cut
    if imw>=width_cutoff:
        #print "Image was too large: Resizing"
        nw=width_replace
        nh=(float(nw)/float(imw))*imh
        #pil_image_handle=pil_image_handle.resize((int(nw),int(nh)))
        cv2_grayscale_np_array=cv2.resize(cv2_grayscale_np_array,(int(nw),int(nh)))


    
    ## The lengthy function arg was to be descriptive, inside the function
    ## It is shortened to im
    im = cv2_grayscale_np_array
        
    ## I HAVE NO CLUE WHAT THIS DOES
    edges = cv2.Canny(im,150,200,apertureSize = 3)

    ## Invoke the infamous probabilistic Hough Line Algorithm with these UNTUNED params
    lines = cv2.HoughLinesP(edges,1,np.pi/180,150, minLineLength = 100, maxLineGap = 10)

    ## Create a spot for the slope of each Hough Line to go
    slope_list=[]

    #The hough lines are given as a list of 4 item lists that go x1,y1,x2,y2 so...
    for x1,y1,x2,y2 in lines[0]:
        
        ## This try block is because the math will obviously fail for infinite slopes
        try:
            
            #Calculate slope (rise over run)
            slope=float(y2-y1)/float(x2-x1)
            
            #Put that slope in the slope list
            slope_list.append(slope)
            
        ## If the calculation of slope fails, just move on with life,
        ## You're going to take the average of many lines and remove outliers anyway
        except: pass

    #Calculate the average of all the slopes from all lines  
    ave_slope=np.average(slope_list)
    
    #Calculate the standard deviation for the same set
    #This is important because these slopes will most likely be very small
    #and one rogue line can completely throw off the results. Also, hopefully
    ## the algorithm finds more horizontal lines then vertical ones. Maybe I should
    ## put a limit on the slopes instead of taking the stdev....
    std_dev_slope=np.std(slope_list)
    
    #From the average and stdev, calculate bounderies to include in the
    #average slope that will be used to calculate the degrees of rotation
    #I'm currently using one standard deviation in either direction.
    upper_bound=ave_slope+std_dev_slope
    lower_bound=ave_slope-std_dev_slope

    #Make a spot for the slopes that are within one std of mean
    one_std_slope_list=[]
    
    #iterate through all the slopes
    for item in slope_list:
        
        #if the slope is less then upper
        if item < upper_bound:
            
            #and greater than lower
            if item > lower_bound:
                
                #Then it makes the final cut
                one_std_slope_list.append(item)

    #With the new list of slopes, take the new average
    one_std_ave_slope=np.average(one_std_slope_list)

    #Because you have a slope you can think of a triangle
    #that has a base of 1 and a height of whatever the slope is
    #and that means you can just use the arctan of the slope to get
    #direction correct degrees of rotation (within 90deg),
    #after converting from radians
    angle_deg=np.arctan(one_std_ave_slope)*180/np.pi

    #return angle_deg, which should be a float

    ## If the skew angle comes back wonky then just set it to 0
    if (float('-inf') < float(angle_deg) < float('inf'))==False:
        print "Something went wrong when finding the skew_angle, image will not be straightened"
        angle_deg=0

    return angle_deg

def get_bounding_box(pil_image_handle):

    ## Again, just a variable switch to be descriptive for the arg but short for the code
    im=pil_image_handle
    
    ## what percent of the linear column/row is data (non black)?
    threshold=0.0175 #1.75%
    
    ## after you find where the data starts, how far back do you want to go?
    revert_depth=30  ## This allows for a small border buffer

    revert_depth_right=100
    
    ## For how many pixels does the threshold need to be sustained?
    ## This is to prevent artifacts from scanning to throw off results
    sustained_depth=20
    
    ## Do I need a secondary threshold? As in initially meet thresh, but subsequently
    ## meet secondary thresh. Maybe the threshold should change with each step? who knows...
    secondary_threshold=.005  ## Not currently being used
    
    ## Load the pixel data
    pix=im.load()
    
    ## save the width of the image
    im_width=im.size[0]
    
    ## And the height of the image
    im_height=im.size[1]

    ## Make a place for the 4 boundaries to go - this will eventually be an argument for
    ## PIL's crop
    bounding_box=[]


    #-----------------------------------------------------------------------------
    #--------------Finding the left boundary---------------------------------------
    #-----------------------------------------------------------------------------

    ## To avoid calculating the percent data in EVERY row and EVERY column, once the
    ## criteria is met, this variable is used to stop calculating (the loop still
    ## executes but no calculation is done.)
    keep_counting=1

    ## Initialize this variable to later be cumulatively filled and re-zeroed
    ## with each iteration through the outer for loop below.
    percent_filled=0

    ## What is the index of the current boundary (either 0 or maximum image dimension)
    boundary=0

    ## A flag that is counted until hopefully reaching "sustained_depth"
    depth_flag=0

    ## For column in image
    for j in range(im_width):

        ## If the criteria have not yet been met
        if keep_counting==1:

            ## Zero percent filled for analysis of next column
            percent_filled=0

            ## for pixel in column
            for i in range(im_height):

                ## Add all pixel values (will be either 0 or 255 because image is made B&W
                ## Before reaching this point - in another function)
                percent_filled=pix[j,i]+percent_filled

            ## After adding up all the pixel values, divide by the possible maximum
            ## (All pixels 255) to get a percentage of white pixels)
            percent_filled=float(percent_filled)/(float(im_width)*255)

            ## If the threshold is met for this particular line
            if percent_filled>=threshold:

                ## Increment the depth flag by one
                depth_flag=depth_flag+1

            ## If percent filled falls below the threshold at any time before
            ## depth flag reaches sustained depth.
            elif percent_filled<threshold:

                ## Reset the depth flag counter
                depth_flag=0

            ## If/when the counter does reach the sustained depth
            if depth_flag>=sustained_depth:

                ## Set keep counting so that percent filled is no longer calculated
                ## for no reason. Ideally the loop would exit, but that's not happening
                ## right now. 
                keep_counting=0

                ## Set boundary equal to the column at which the criteria were met MINUS
                ## sustained depth, because the analysis was happening left to right
                boundary=j-sustained_depth

    ## Then also account for the revert depth (to give a small border buffer so there is no
    ## important data directly on the edges
    boundary=boundary-revert_depth

    ## If the boundary is determined to be less than 0, it just means that the analysis
    ## didn't reach a depth far enough to overcome the revert depth and sustained depth
    ## So just set the boundary to it's original value
    if boundary<0:
        boundary=0

    ## Add boundary found to the soon to be argument for cropping the image according
    ## to this analysis
    bounding_box.append(boundary)



    ## Analysis for the other three sides below is similar and is not as heavily
    ## Commented - or may contain old comments

    #-----------------------------------------------------------------------------
    #--------------Finding the top boundary---------------------------------------
    #-----------------------------------------------------------------------------

    keep_counting=1
    percent_filled=0
    boundary=0
    depth_flag=0
    
    for j in range(im_height): #j goes from top to bottom here
        if keep_counting==1: # if the criteria below haven't been met
            percent_filled=0  # reset percent filled
            for i in range(im_width): # for every pixel in row
                percent_filled=pix[i,j]+percent_filled #calc fill
            percent_filled=float(percent_filled)/(float(im_width)*255) # calc%
            if percent_filled>=threshold: # if the thres is met
                depth_flag=depth_flag+1 # increment the depth counter
            elif percent_filled<threshold: # if it falls below
                depth_flag=0 # reset the counter
            if depth_flag>=sustained_depth: #if the counter reaches the depth
                keep_counting=0 # stop calculating (just dumbly iterate through every row
                boundary=j-sustained_depth # calculate boundary based on the current row

    boundary=boundary-revert_depth
    if boundary<0:
        boundary=0
    bounding_box.append(boundary)


    #-----------------------------------------------------------------------------
    #--------------Finding the right boundary---------------------------------------
    #-----------------------------------------------------------------------------

    keep_counting=1
    percent_filled=0
    boundary=0
    depth_flag=0

    for j in range(im_width):
        if keep_counting==1:
            percent_filled=0
            for i in range(im_height):
                percent_filled=pix[im_width-j-1,i]+percent_filled
            percent_filled=float(percent_filled)/(float(im_width)*255) # calc%
            if percent_filled>=threshold: # if the thres is met
                depth_flag=depth_flag+1 # increment the depth counter
            elif percent_filled<threshold: # if it falls below
                depth_flag=0 # reset the counter
            if depth_flag>=sustained_depth: #if the counter reaches the depth
                keep_counting=0 # stop calculating (just dumbly iterate through every row
                boundary=im_width-j+sustained_depth # calculate boundary based on the current row

    boundary=boundary+revert_depth_right
    if boundary>im_width:
        boundary=im_width
    bounding_box.append(boundary)

    #-----------------------------------------------------------------------------
    #--------------Finding the bottom boundary---------------------------------------
    #-----------------------------------------------------------------------------

    keep_counting=1
    percent_filled=0
    boundary=0
    depth_flag=0
    
    for j in range(im_height): #j goes from top to bottom here
        if keep_counting==1: # if the criteria below haven't been met
            percent_filled=0  # reset percent filled
            for i in range(im_width): # for every pixel in row
                percent_filled=pix[i,im_height-j-1]+percent_filled #calc fill
            percent_filled=float(percent_filled)/(float(im_width)*255) # calc%
            if percent_filled>=threshold: # if the thres is met
                depth_flag=depth_flag+1 # increment the depth counter
            elif percent_filled<threshold: # if it falls below
                depth_flag=0 # reset the counter
            if depth_flag>=sustained_depth: #if the counter reaches the depth
                keep_counting=0 # stop calculating (just dumbly iterate through every row
                boundary=im_height-j+sustained_depth # calculate boundary based on the current row

    boundary=boundary+revert_depth
    if boundary>im_height:
        boundary=im_height
    bounding_box.append(boundary)

    #------------------------------------------------------------------------------
    
    return bounding_box

## I couldn't find a function to convert grayscale to black and white
## but didn't even get to test it before finding the cv2 way
## keeping it here for some reason - will probably delete it later. 
####def cv2gray2bw(grayscale_np_array):
####    im=grayscale_np_array
####    for r in range(len(im)):
####        for p in range(len(im[r])):
####            if im[r][p]>128:
####                im[r][p]=255
####            elif im[r][p]<128:
####                im[r][p]=0
####    return im
                
